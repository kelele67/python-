from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def get_primes():
    primes = []
    for i in range(1, 1000):
        if is_prime(i):
            primes.append(i)
    return primes

def countSum(n):
    count = 0
    primes = get_primes()
    for prime in primes:
        if prime <= n / 2:
            if n-prime in primes:
                count = count + 1
        else:
            break
    return count

n = int(raw_input())
print countSum(n)
