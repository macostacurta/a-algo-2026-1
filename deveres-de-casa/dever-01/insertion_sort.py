import time
import random


def insertion_sort (lista):

    start_time = time.time()

    tamanho = len(lista)

    for i in range(1, tamanho):

        pivot = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > pivot:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = pivot 

    end_time = time.time()
    total_time = end_time - start_time

    print(f"O Tempo total da execução utilizando insertion_sort de uma lista de tamanho {tamanho} é: {total_time} segundos")


def insertion_sort_py(lista):
    start_time = time.time()

    lista = sorted(lista)

    end_time = time.time()

    total_time = end_time - start_time

    print(f"O Tempo total da execução utilizando sorted() do python em uma lista de tamanho {len(lista)} é: {total_time} segundos")

def generate_rand_list (n):
    list = []

    for i in range(n):

        list.append(random.randrange(10000))

    return list

def benchmark_sorters():
    list_sizes= [1000, 5000, 10000, 20000, 50000]

    for i in range(len(list_sizes)):
        random_list = generate_rand_list(list_sizes[i])

        insertion_sort_py(random_list)
        insertion_sort(random_list)

        print(114*"=")
        

        random_list.clear

benchmark_sorters()





            