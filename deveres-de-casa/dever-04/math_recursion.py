import math

def recursive_pow(n):

    if n == 1:
        return 2
    else:
        return 2 * recursive_pow (n-1) + math.pow(n,2)

def closed_pow(n):
    return 6.5 * math.pow(2,n) - math.pow(n,2) - (4*n) - 6
    

def main():

    n = input('Digite um numero\n')

    n_int = int(n)

    result = recursive_pow(n_int)
    result2 = closed_pow(n_int)
    
    print(f'O valor de POW por recursão é: {result} \n')
    print(f'O valor de POW fechado é: {result2} \n')

if __name__ == '__main__':
    main()