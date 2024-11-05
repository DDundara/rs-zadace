#1.dio
def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, int(broj ** 0.5) + 1):
        if broj % i == 0:
            return False 
    return True
print(isPrime(7))   
print(isPrime(10))  
#2.dio
def primes_in_range(start, end):
    prosti_brojevi = []
    for broj in range(start, end + 1):
        if isPrime(broj): 
            prosti_brojevi.append(broj) 
    return prosti_brojevi
print(primes_in_range(1, 10)) 

