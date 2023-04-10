import random
def generate_random_number():
    return random.randint(1, 200)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

    
random_num = generate_random_number()
if isPrime(random_num):
    print(random_num, "is a prime number")
else:
    print(random_num, "is not a prime number")