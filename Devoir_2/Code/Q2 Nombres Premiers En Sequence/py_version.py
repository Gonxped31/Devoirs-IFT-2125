from itertools import permutations
import math
import time

'''def get_all_sequences(sequences) -> list:
    if len(sequences) == 3:
        return sequences
    else:
        res = []
        for i in range(1, len(sequences)):
            for j in range(i+1, len(sequences)):
                seq = (sequences[0], sequences[i])
                seq += (sequences[j],)
                res.append(seq)
            
        return res'''

def permuts(prime) -> tuple:
    perms = tuple([''.join(p) for p in permutations(prime)])
    perm_set = set()
    for elem in perms:
        perm_set.add(elem)
    return tuple(perm_set)

def get_K(permut, prime, i) -> int:
    k = int((permut - prime) / i)
    return k if k % 1 == 0 and k > 0 else None

    
def is_prime(num) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(N) -> list:
    """Generate prime numbers up to N-1."""
    primes = []
    for num in range(2, N):  # Check numbers from 2 to N-1
        if is_prime(num):
            primes.append(num)
    res = list(filter(lambda x: len(x) >= 3, list(map(lambda y: str(y), primes))))
    return res

def algorithm(N, primes) -> None:
    valid_sequences = []
    for prime in primes:
        permutations = permuts(prime)
        valid_perms = list(filter(lambda x: is_prime(x) and len(str(x)) == len(prime) and x < N, list(map(lambda y: int(y), permutations))))
        valid_perms.remove(int(prime))
        sequences = set()
        sequences.add(int(prime))
        for perm in valid_perms:
            i = len(sequences)
            k = get_K(int(perm), int(prime), i)
            if k != None:
                S = int(prime) + (i+1)*k
                if S in valid_perms:
                    sequences.add(int(perm))
                    sequences.add(int(S))
        if len(sequences) >= 3:
            sequences = tuple(sorted(sequences))
            valid_sequences.append(sequences)
        
    print(valid_sequences)

N = 100000
primes = generate_primes(N)
start = time.time()
algorithm(N, primes)
end = time.time()
print('time =', end - start)