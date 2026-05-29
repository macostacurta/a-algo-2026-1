import random
import heapq

def gerar_grafo_aleatorio(num_nos, num_arestas, peso_maximo=20):
    """Gera um grafo não direcionado ponderado com o número especificado de nós e arestas."""
    
    grafo = {i: {} for i in range(1, num_nos + 1)}
    arestas_adicionadas = 0
    
    while arestas_adicionadas < num_arestas:
        u = random.randint(1, num_nos)
        v = random.randint(1, num_nos)
        
        
        if u != v and v not in grafo[u]:
            peso = random.randint(1, peso_maximo)
            
            grafo[u][v] = peso
            grafo[v][u] = peso
            arestas_adicionadas += 1
            
    return grafo

def dijkstra(grafo, inicio, destino):
    """Implementação do Algoritmo de Dijkstra usando fila de prioridade (Min-Heap)."""
    
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    nos_anteriores = {no: None for no in grafo}
    
    
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        
        
        if distancia_atual > distancias[no_atual]:
            continue
            
        
        if no_atual == destino:
            break
            
        
        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso
            
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                nos_anteriores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
                
    return distancias, nos_anteriores

def reconstruir_rota(nos_anteriores, inicio, destino):
    """Reconstrói a rota final navegando de trás para frente usando o dicionário de nós anteriores."""
    rota = []
    atual = destino
    
    while atual is not None:
        rota.append(atual)
        if atual == inicio:
            break
        atual = nos_anteriores[atual]
        
    
    if not rota or rota[-1] != inicio:
        return None
        
    rota.reverse()
    return rota

if __name__ == "__main__":
    
    seed = input("Escreva um numero qualquer para gerar a seed do grafo: ")

    random.seed(seed)

    
    QTD_NOS = 50
    QTD_ARESTAS = 150
    grafo_ponderado = gerar_grafo_aleatorio(QTD_NOS, QTD_ARESTAS)

    
    NO_INICIO = 1
    NO_DESTINO = 50

    
    distancias, nos_anteriores = dijkstra(grafo_ponderado, NO_INICIO, NO_DESTINO)
    rota = reconstruir_rota(nos_anteriores, NO_INICIO, NO_DESTINO)

    
    print("-" * 40)
    print(" RESULTADO DO ALGORITMO DE DIJKSTRA ")
    print("-" * 40)
    
    if rota:
        rota_formatada = " -> ".join(map(str, rota))
        print(f"Rota completa: {rota_formatada}")
        print(f"Custo total: {distancias[NO_DESTINO]}")
    else:
        print(f"Aviso: Não há caminho conectado entre o Nó {NO_INICIO} e o Nó {NO_DESTINO}.")
    print("-" * 40)