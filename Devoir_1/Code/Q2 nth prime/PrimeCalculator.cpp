#include <iostream>
#include <vector>
#include <math.h>
#include <chrono>
#include "PrimeCalculator.h"

PrimeCalculator::PrimeCalculator()
{
}

int PrimeCalculator::CountPrimes(std::vector<int>* primes, int N)
{
    primes->shrink_to_fit();
    int count = 0;
    for (int i = 2; i < primes->size(); ++i)
    {
        count += (*primes)[i];
        if (count == N)
        {
            //std::cout << "index= " << i << "\n";
            return i;
        }
    }
}

int PrimeCalculator::FindPrimes(int N, int s, std::vector<int>* primes)
{
    //std::cout << "In Find Prime" << "\n";
    int previous_size = primes->size();
    int new_size = s - previous_size;
    
    //std::cout << "Size: " << new_size << "\n";
    

    for (int i = 0; i < new_size; ++i)
    {
        primes->push_back(1);
    }
    
    //std::cout << "Primes.size= " << primes->size() << "\n" ;
    //std::cout << "Primes[1]= " << (*primes)[1] << "\n" ;

    for (int i = 2; i < s; i++)
    {
        //std::cout << "first loop" << "\n";
        if ((*primes)[i] == 1)
        {
            for (int j = i; j < s; j++)
            {
                //std::cout << s << "\n";
                //std::cout << i << "\n";
                //std::cout << j << "\n";
                //std::cout << "second loop" << "\n";
                int product = i*j;
                //std::cout << product << "\n";
                if (j <= s/i)
                {
                    //std::cout << "IN";
                    (*primes)[product] = 0;
                    //std::cout << "OUT";
                }
                else
                {
                    break;
                }
            }
        }
    }

    //std::cout << "Let's find sum";

    // Find the number of prime numbers before s without considerating 0 and 1.
    int sum = 0;
    for (int i = 2; i < s; i++)
    {
        sum += (*primes)[i];
    }
    
    //std::cout << "Sum= " << sum << "\n";

    return sum;
}

int PrimeCalculator::CalculateNthPrime(int N)
{
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    switch (N)
    {
    case 1:
        return 2;
    
    case 2:
        return 3;

    case 3:
        return 5;

    case 4:
        return 7;

    case 5:
        return 11;
    }

    int factor = ceil(N*log(N) + N*log(log(N)));
    int s = (N + factor);
    //std::cout << "Factor: " << factor << "\n";
    //std::cout << "S: " << s << "\n";
    int primesFound = 0;
    std::vector<int>* primes = new std::vector<int>();

    while (primesFound < N)
    {
        primesFound = FindPrimes(N, s, primes);
        //std::cout << "Prime Found";
        factor += 1;
        s = (N + factor);
    }
    //std::cout << "Result";

    int result = CountPrimes(primes, N);
    
    delete primes;

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();

    std::cout << "\tTime = " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << " [ms]" << "for N = " << N << std::endl;
    return result;
}