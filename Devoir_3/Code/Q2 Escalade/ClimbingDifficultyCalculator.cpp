// Gbian Bio Samir, 20250793
// Sourou Johann, 20227958

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
// #include <unordered_set>
// #include <math.h>
#include <algorithm>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe ClimbingDifficultyCalculator
// this file contains the definitions of the methods of the ClimbingDifficultyCalculator class

ClimbingDifficultyCalculator::ClimbingDifficultyCalculator()
{
}

std::vector<std::vector<int>> ClimbingDifficultyCalculator::Reader(std::string filename)
{
    std::vector<std::vector<int>> data;
    std::vector<int> currentRow;
    char ch;
    int currentNum = 0;
    std::ifstream file(filename);

    //Print an error if the file can not be opened
    if (!file.is_open())
    {
        std::cerr << "Unable to open the file\n";
        return data;
    }

    while (file.get(ch))
    {
        if (ch == ',' || ch == '\n' || file.eof())
        {
            currentRow.push_back(currentNum);
            currentNum = 0;

            // Check if we are at the end of a line
            if (ch == '\n' || file.eof())
            {
                data.push_back(currentRow);
                currentRow.clear();
            }
        }
        else if (ch >= '0' && ch <= '9') {
            // Build the current number
            currentNum = currentNum * 10 + (ch - '0');
        }
    }

    // Add the last number/row if file does not end with a newline
    if (!currentRow.empty()) {
        data.push_back(currentRow);
    }

    return data;
}

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    std::vector<std::vector<int>> data = Reader(filename);
    int lines = data.size();
    int columns = data[0].size();
    std::vector<std::vector<int>> distTab(lines, std::vector<int>(columns));
    
    for (int i = 1; i < lines; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            int actualLine = lines - 1 - i;

            int min = distTab[i-1][j] + data[actualLine][j];

            if (j > 0)
            {
                int left = distTab[i][j - 1] + data[actualLine][j];
                min = std::min(min, left);
            }

            int rightSum = 0;
            for (int k = j + 1; k < columns; k++)
            {
                rightSum += data[actualLine][k];
                int dist = distTab[i - 1][k] + rightSum + data[actualLine][j];
                min = std::min(min, dist);
            }
            distTab[i][j] = min;
        }
        
    }

    return *std::min_element(distTab.back().begin(), distTab.back().end());
}
