
def max_factor(n):
   
    factor = 2
    while factor * factor <= n:
        while num % factor == 0:
            n /= factor
        factor += 1
    if (n > 1):
        return n
    return factor

print max_factor(13195)



#alternate

# kn_primes = [2,3]
# def is_prime(n):
#     total_primes = len(kn_primes)
#     for i in range(0, total_primes):
#         in(n % kn_primes[i] == 0):
#         return False

#     else:
#         continue
#     kn_primes.append(n)
#     return True

