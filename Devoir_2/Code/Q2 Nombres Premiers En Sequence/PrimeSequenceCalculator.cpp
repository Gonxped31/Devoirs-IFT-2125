#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

// Nom, Matricule
// Nom, Matricule

#include "PrimeSequenceCalculator.h"
#include <vector>
#include <unordered_set>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <set>

// ce fichier contient les definitions des methodes de la classe PrimeSequenceCalculator
// this file contains the definitions of the methods of the PrimeSequenceCalculator class

PrimeSequenceCalculator::PrimeSequenceCalculator()
{
}

bool PrimeSequenceCalculator::IsPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= std::sqrt(num); ++i) {
        if (num % i == 0) return false;
    }
    return true;
}

std::vector<std::string> PrimeSequenceCalculator::GeneratePrimes(int N) {
    std::vector<std::string> primes;
    for (int num = 2; num < N; ++num) {
        if (IsPrime(num)) {
            std::string numStr = std::to_string(num);
            if (numStr.length() >= 3) {
                primes.push_back(numStr);
            }
        }
    }
    return primes;
}

std::set<std::string> PrimeSequenceCalculator::Permuts(const std::string& prime) {
    std::string temp = prime;
    std::sort(temp.begin(), temp.end());
    std::set<std::string> perms;
    do {
        perms.insert(temp);
    } while (std::next_permutation(temp.begin(), temp.end()));
    return perms;
}

std::vector<int> PrimeSequenceCalculator::FilterAndConvert(const std::set<std::string>& perms, int N) {
    std::vector<int> filtered;
    for (const auto& perm : perms) {
        int num = std::stoi(perm);
        if (IsPrime(num) && perm.length() == perms.begin()->length() && num < N) {
            filtered.push_back(num);
        }
    }
    return filtered;
}

int PrimeSequenceCalculator::GetK(int permut, int prime, int i) {
    int k = (permut - prime) / i;
    return (k % i == 0 && k > 0) ? k : -1;
}

std::vector<std::vector<int>> PrimeSequenceCalculator::CalculatePrimeSequences(const int N) {
    const std::vector<std::string> primes = GeneratePrimes(N);
    std::vector<std::vector<int>> valid_sequences;
    for (const auto& prime : primes) {
        auto permsSet = Permuts(prime);
        auto validPerms = FilterAndConvert(permsSet, N);
        std::set<int> sequences;
        sequences.insert(std::stoi(prime));
        for (int perm : validPerms) {
            if (perm == std::stoi(prime)) continue;
            int i = sequences.size();
            int k = GetK(perm, std::stoi(prime), i);
            if (k != -1) {
                int S = std::stoi(prime) + (i + 1) * k;
                if (std::find(validPerms.begin(), validPerms.end(), S) != validPerms.end()) {
                    sequences.insert(perm);
                    sequences.insert(S);
                }
            }
        }
        if (sequences.size() >= 3) {
            valid_sequences.push_back(std::vector<int>(sequences.begin(), sequences.end()));
        }
    }

    // Printing valid sequences
    for (const auto& seq : valid_sequences) {
        for (int num : seq) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    return valid_sequences;
}