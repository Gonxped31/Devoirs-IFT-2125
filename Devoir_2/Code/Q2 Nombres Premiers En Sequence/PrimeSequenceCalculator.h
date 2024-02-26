// Nom, Matricule
// Nom, Matricule

#include <vector>

// ce fichier contient les declarations des methodes de la classe PrimeSequenceCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the PrimeSequenceCalculator class
// can be modified if you wish to add other methods to the class

class PrimeSequenceCalculator{
    public :
        PrimeSequenceCalculator();
        std::vector<std::vector<int>> CalculatePrimeSequences(const int N);
};