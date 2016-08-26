def is_prime(n):
    if n <= 1:
        return False
        
    # Exceptions to efficency factor below
    if n <= 9:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
    else:
        # If n is not prime => n = a * b iff a >= sqrt(n) where b <= sqrt(n) or b >= sqrt(n) where a <= sqrt(n),
        # so for efficency we only need to check upto sqrt(n) to find another factor, (Either a or b) to prove 'isPrime'. 
        for i in range(2, int(round(n ** 0.5)) + 1):
            if n % i == 0:
                return False
        return True
