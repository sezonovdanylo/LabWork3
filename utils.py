def faktorial(a):
    if a ==0 or a ==1:
        return 1
    else:
        return a*faktorial(a-1)

def five(b):
    if b<1:
        return False
    else:
        if b ==5:
            return True
        else:
            return five(b/5)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

