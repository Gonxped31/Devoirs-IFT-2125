// Gbian Bio Samir 20250793
// Sourou Johann 20227958

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <math.h>
#include <set>

// ce fichier contient les declarations des methodes de la classe PrimeSequenceCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the PrimeSequenceCalculator class
// can be modified if you wish to add other methods to the class

class PrimeSequenceCalculator{
    public :
        PrimeSequenceCalculator();
        //std::vector<std::vector<int>> CalculatePrimeSequences(const int N);
        //std::string CalculateCodePermut(int N);
        bool IsPrime(int num);
        std::vector<std::string> GeneratePrimes(int N);
        std::set<std::string> Permuts(const std::string& prime);
        std::vector<int> FilterAndConvert(const std::set<std::string>& perms, int N);
        int GetK(int permut, int prime, int i);
        std::vector<std::vector<int>> CalculatePrimeSequences(const int N);


};