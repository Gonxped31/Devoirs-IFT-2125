import time
import math

def get_nth_prime(N):
  """ Returns the n-th prime number """
  total_primes = 0
  trivial_primes = {
     1:2, 2:3, 3:5, 4:7, 5:11
  }
  if N in trivial_primes:
     return trivial_primes[N]
  
  size_factor = math.ceil(N*math.log(N) + N*math.log(math.log(N)))
  s = (N + size_factor)
  while total_primes < N:
    primes = get_primes(s)
    total_primes = sum(primes[2:])
    size_factor += 1
    s = (N + size_factor)
  nth_prime = count_primes(primes, N)
  return nth_prime


def get_primes(s):
  """ Generates primes using the Sieve of Eratosthenes
      Includes the optimization where for every prime p, only factors p >= p^2
      are verified.
      The list of primes is represented with a bytearray. Each index corresponds
      to an integer in the list. A value of "1" at the index location indicates
      the integer is a prime.
  """
  primes = bytearray([1]*s)
  for i in range(2, s):
    if primes[i] == 1:
        for j in range(i, s):
            if j < s/i:
                primes[i*j] = 0
            else:
                break
    
  
  return primes


def count_primes(primes, nth):
  """ Returns the n-th prime represented by the index of the n-th "1" in the
      bytearray.
  """
  #print(list(primes))
  count = 0
  for k in range(2, len(primes)):
    count += primes[k]
    #print(k)
    if count == nth:
      return k
    
start_time = time.time()
res = get_nth_prime(10000000)
end_time = time.time()
print(f'Result: {res}  Time: {round(end_time-start_time, 2)}')