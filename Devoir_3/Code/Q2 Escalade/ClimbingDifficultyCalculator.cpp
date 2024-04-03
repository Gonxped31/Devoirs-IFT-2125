// Gbian Bio Samir, 20250793
// Sourou Johann, 20227958

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <sstream>
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

std::vector<std::vector<int>> ClimbingDifficultyCalculator::Reader(std::string input_file) {
    std::ifstream file(input_file);
    std::vector<std::vector<int>> inputs;
    std::string line;

    if (!file.is_open()) {
        std::cerr << "Unable to open file\n";
        return inputs;
    }

    while (std::getline(file, line)) {
        std::vector<int> row;
        std::stringstream ss(line);
        std::string item;
        while (std::getline(ss, item, ',')) {
            row.push_back(std::stoi(item)); // Convert string to int
        }
        inputs.push_back(row);
    }

    return inputs;
}
/*
for(int i = 0; i <= data.size(); i++){
        for(int j = 0; j <= data[i].size(); j++){
       std::cout << data[i][j] << std::endl;
       }
    }
    
*/

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    std::vector<std::vector<int>> data = Reader(filename);
    int lines = data.size();
    int columns = data[0].size();
    std::vector<std::vector<int>> distTab = {{data[data.size() - 1]}};
    std::vector<int> zeros;

    for (int i = 0; i < data[0].size(); i++)
    {
        zeros.push_back(0);
    }


    for (int i = 1; i < data.size(); i++)
    {
        distTab.push_back(zeros);
    }


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