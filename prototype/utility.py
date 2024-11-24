def factors(num:int):
    if abs(num) == 1:
        return [1]
    
    factors = [n+1 for n in range(int(abs(num)/2)) if num % (n+1) == 0]
    factors += [int(abs(num)/f) for f in factors if int(abs(num)/f) not in factors]
    return sorted(factors)