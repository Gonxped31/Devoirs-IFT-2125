// Nom, Matricule
// Nom, Matricule

#include "PrimeSequenceCalculator.h"
#include <vector>
#include <unordered_set>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <string>

// ce fichier contient les definitions des methodes de la classe PrimeSequenceCalculator
// this file contains the definitions of the methods of the PrimeSequenceCalculator class

PrimeSequenceCalculator::PrimeSequenceCalculator()
{
}

std::vector<std::vector<int>> PrimeSequenceCalculator::CalculatePrimeSequences(const int N)
{
    PrimeSequenceCalculator aCalculator = PrimeSequenceCalculator();

    
    //Cal.CalculateCodePermut(N);

    // TODO
    // À compléter / To be completed
    std::vector<std::vector<int>> result {};
    int number = N;
    std::vector<int> primeNumber(number+1);
    std::vector<int> primeNumberOnly = {2};


    for(int i = 0; i < primeNumber.size(); i++){
        primeNumber[i] = 1;
    }
     
    for(int i = 2; i < sqrt(primeNumber.size()); i++){
       if(primeNumber[i] == 1){

        for(int j = i+1; j < primeNumber.size() ; j++){
            if(j%i == 0){
                primeNumber[j] = 0;
            }   
        }
      }
    }

    for(int j = 3; j < primeNumber.size() ; j++){
            if(primeNumber[j] == 1){
                primeNumberOnly.push_back(j);
            }   
        }


    for(int i = 0; i < primeNumberOnly.size() ; i++){
        
        for(int j = i+1; j < primeNumberOnly.size() ; j++){
             

            if(aCalculator.CalculateCodePermut(primeNumberOnly[i]) == aCalculator.CalculateCodePermut(primeNumberOnly[j])){
                  
               int c = 2*(primeNumberOnly[j]) - primeNumberOnly[i];
              
            if( std::count(primeNumberOnly.begin(),primeNumberOnly.end(), c) == 1){
               if(aCalculator.CalculateCodePermut(primeNumberOnly[j]) == aCalculator.CalculateCodePermut(c)){

                    /*  std::cout << " code "<< primeNumberOnly[i] << " : " << aCalculator.CalculateCodePermut(primeNumberOnly[i]) << std::endl;
                        std::cout << " code "<< primeNumberOnly[j] << " : " << aCalculator.CalculateCodePermut(primeNumberOnly[j]) << std::endl;
                        std::cout << " code "<< c << " : " << aCalculator.CalculateCodePermut(c) << std::endl;
                        std::cout << " : " << std::endl; */

                std::vector<int> aSequence = {primeNumberOnly[i], primeNumberOnly[j], c};
                result.push_back(aSequence);

                 }
               }
            }
        }
    }
     

    return result;
}



std::string PrimeSequenceCalculator::CalculateCodePermut(int N)
{
    std::string base10Numbers = "0123456789";
    std::string s = std::to_string(N); 
    std::string result = "";


    for (int i = 0; i < base10Numbers.length(); i++){

    int occurence = 0;

    for (int j = 0; j < s.length(); j++){

      if(base10Numbers[i] == s[j]){
         occurence++;
      }

    }
      
    result += std::to_string(occurence);

    }

    return  result;
}

