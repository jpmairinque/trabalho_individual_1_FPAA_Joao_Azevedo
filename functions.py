# Implementação do algoritmo de Karatsuba com nós identificados
def karatsuba(x, y):
    # 1 
    if x < 10 or y < 10: # 2
        return x * y # 3
    
    n = max(len(str(x)), len(str(y))) # 4
    m = n // 2 # 5
    
    x_high, x_low = divmod(x, 10**m) # 6
    y_high, y_low = divmod(y, 10**m) # 7
    
    a = karatsuba(x_high, y_high) # 8
    
    b = karatsuba(x_low, y_low) # 9
    
    c = karatsuba(x_high + x_low, y_high + y_low) - a - b # 10
    
    return a * 10**(2*m) + c * 10**m + b # 11
