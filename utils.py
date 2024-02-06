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
