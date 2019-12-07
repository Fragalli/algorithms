def calculate(x, y, mdc):
    a, b, aPrevious, bPrevious = 0, 1, 1, 0
    aNext, bNext = 0, 0
    module = 0
    
    while module != mdc:
        module = x % y
        q = x // y
        
        aNext = aPrevious - (q * a)
        bNext = bPrevious - (q * b)
        x, y = y, module
        
        aPrevious, bPrevious = a, b
        a, b = aNext, bNext
    
    print("O MDC É: ", mdc, " E OS MULTIPLOS SÃO ", a, " E", b)

def mdc(m, n):
    module = m % n
    return n if module == 0 else mdc(n, module)

def main():
    x = int(input("ENTRE COM O PRIMEIRO NÚMERO: "))
    y = int(input("ENTRE COM O SEGUNDO NUMERO: "))
    
    calculate(x, y, mdc(x, y)) if x > y else calculate(y, x, mdc(y, x))
    

if __name__ == "__main__":
    main()