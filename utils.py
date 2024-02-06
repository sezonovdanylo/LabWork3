def faktorial(a):
    if a ==0 or a ==1:
        return 1
    else:
        return a*faktorial(a-1)



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a