//**************************************************************
// Given the length and width of a rectangle, this C++ program
// computes and outputs the perimeter and area of the rectangle.
//**************************************************************
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <chrono>
#include "PrimeCalculator.h"
using namespace std;


int main()
{ 
    map<int, int> allNumbers;
    vector<int> primeNumber = {1};
    int n;
    int limit;

    n = 10000;
    limit = static_cast<int>(n*log(n*log(n)));
   

    //cout << "allNumbersSize() : " << allNumbers.size() << endl;

    auto start_time = std::chrono::high_resolution_clock::now();

    for(int i = 2; i<limit+1; i++){
        allNumbers[i] = 1;
    }


    /*cout << "limit : " << limit << endl;
    cout << "limit pow : " <<  static_cast<int>((pow(limit, 0.5)) + 1)  << endl;*/

    for(int i = 2; i < static_cast<int>((pow(limit, 0.5)) + 1) ; i++){
        if(allNumbers[i] == 1){
            // cout << "i : " << i << endl;   
            primeNumber.push_back(i);

            for(int j = 2; j < (static_cast<int>(limit + 1)); j++){
                //cout << "i : " << i << "j : " << j  << endl;
                if(j%i == 0){
                    allNumbers[j] = 0;
                }
            } 
        }
    }

    for(int i = 3; i<allNumbers.size(); i++){
        if(allNumbers[i] == 1){
            primeNumber.push_back(i);
        }
    }
    
    cout << n <<" th prime Number : " << primeNumber[n] << endl;  

    auto end_time = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::seconds>(end_time - start_time);
    cout << "Temps d'execution : " << duration.count() << " seconds" << endl;
    return 0;
 
} 