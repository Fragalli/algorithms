def mdc(m, n):
    module = m % n
    print("O MDC É ", n) if module == 0 else mdc(n, module)

def main():
    x = int(input("ENTRE COM O PRIMEIRO NÚMERO: "))
    y = int(input("ENTRE COM O SEGUNDO NUMERO: "))
    
    mdc(x, y) if x > y else mdc(y, x)

if __name__ == "__main__":
    main()