import time

# Fatorial é o produto de um numero inteiro por todos os numeros anteriores a ele.
def recursivefactorial (n):
    #A primeira verificação que é feita é se n é igual a 1, que indica se o fatorial acabou
    if n == 1:
        return n
    else:
        #Aqui ocorre o calculo do fatorial. O next_number pega o proximo numero a ser calculado e o factorial multiplica o numero atual pelo fatorial do proximo numero 
        next_number = n - 1
        factorial = n * recursivefactorial(next_number)
        return factorial
    

def main():
    
    #input para o usuario escolher o nomero que sera calculado
    n_str = input("Escolha um numero de 1 a 900. (numeros maiores que isso podem quebrar o programa) \n")
    n = int(n_str)

    if n <= 900 and n >= 1:

        start_time = time.time()

        result = recursivefactorial(n)

        end_time = time.time()
        #conta para saber o tempo que levou para o algoritimo ser executado
        total_time = end_time - start_time

        print(f"O resultado do fatorial de {n} é {result} que levou {total_time} segundos para ser executado.")

    else: print("Esse numero é muito grande ou menor que 1")

    #A complexidade assintotica deste codigo é O(N). Ou seja, linear, ja que a quantidade de operações realizadas é proporcional ao tamanho da entrada.
    #Se n = 1000 a função recursiva vai rodar 1000 vezes que nesse caso chega a quebrar o codigo ja que execede o maximo de recurções que o python aguenta.

if __name__ == "__main__":
    main()