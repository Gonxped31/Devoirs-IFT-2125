#include <vector>

//Gbian Bio Samir, 20250793
//Sourou Johann, 20227958

// ce fichier contient les declarations des methodes de la classe PrimeCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the PrimeCalculator class
// can be modified if you wish to add other methods to the class

class PrimeCalculator{
    public :
        PrimeCalculator();
        int CountPrimes(std::vector<int>* primes, int N);
        int FindPrimes(int N, int s, std::vector<int>* primes);
        int CalculateNthPrime(int N);
};
