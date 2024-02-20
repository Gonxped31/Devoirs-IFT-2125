//Nom, Matricule
//Nom, Matricule
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include "PrimeCalculator.h"
using namespace std;
// #include <vector>
// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class


PrimeCalculator::PrimeCalculator()
{
}

int PrimeCalculator::CalculateNthPrime(int N)
{
    
    // a completer
    // TODO
    map<int, int> allNumbers;
    vector<int> primeNumber = {1};
    int limit = static_cast<int>(N*log(N*log(N)));
    int result = 0;

    for(int i = 2; i<limit+1; i++){
        allNumbers[i] = 1;
    }


    limit = static_cast<int>(N*log(N*log(N)));

    for(int i = 2; i < static_cast<int>((pow(limit, 0.5)) + 1) ; i++){
        if(allNumbers[i] == 1){
            //cout << "i : " << i << endl;   
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
            cout << "i : " << i << endl;
            primeNumber.push_back(i);
        }
    }
    
    result = primeNumber[N]; 
    cout << "result " << result << endl;
    
    return result;

}