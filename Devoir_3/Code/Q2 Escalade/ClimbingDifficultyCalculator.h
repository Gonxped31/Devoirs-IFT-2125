// Gbian Bio Samir, 20250793
// Sourou Johann, 20227958

//#include <vector>
#include <string>
#include <vector>

// ce fichier contient les declarations des methodes de la classe ClimbingDifficultyCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the ClimbingDifficultyCalculator class
// can be modified if you wish to add other methods to the class

class ClimbingDifficultyCalculator{
    public :
        ClimbingDifficultyCalculator();
        std::vector<std::vector<int>> Reader(std::string);
        int CalculateClimbingDifficulty(std::string);
};

