import random
import heapq

def gerar_grafo_aleatorio(num_nos, num_arestas, peso_maximo=20):
    """Gera um grafo não direcionado ponderado com o número especificado de nós e arestas."""
    # Inicializa o grafo com dicionários vazios para cada nó (Lista de Adjacência)
    grafo = {i: {} for i in range(1, num_nos + 1)}
    arestas_adicionadas = 0
    
    while arestas_adicionadas < num_arestas:
        u = random.randint(1, num_nos)
        v = random.randint(1, num_nos)
        
        # Evita auto-loops e arestas duplicadas
        if u != v and v not in grafo[u]:
            peso = random.randint(1, peso_maximo)
            # Como é um grafo não direcionado, a aresta vai nos dois sentidos
            grafo[u][v] = peso
            grafo[v][u] = peso
            arestas_adicionadas += 1
            
    return grafo

def dijkstra(grafo, inicio, destino):
    """Implementação do Algoritmo de Dijkstra usando fila de prioridade (Min-Heap)."""
    # Inicializa distâncias com infinito e o caminho anterior com None
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    nos_anteriores = {no: None for no in grafo}
    
    # Fila de prioridade: armazena tuplas (distancia_acumulada, no_atual)
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        
        # Se encontrou um caminho mais longo do que o já registrado, ignora
        if distancia_atual > distancias[no_atual]:
            continue
            
        # Otimização: se chegou no destino, pode parar a busca
        if no_atual == destino:
            break
            
        # Verifica os vizinhos do nó atual
        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso
            
            # Se encontrou um caminho mais curto para o vizinho, atualiza
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
        
    # Se a rota estiver vazia ou não chegar ao nó de início, o caminho não existe
    if not rota or rota[-1] != inicio:
        return None
        
    rota.reverse()
    return rota

if __name__ == "__main__":
    # Fixando a seed para que a execução de teste seja reprodutível (opcional)
    seed = input("Escreva um numero qualquer para gerar a seed do grafo: ")

    random.seed(seed)

    # 1. Gerar o grafo (50 nós, 150 arestas)
    QTD_NOS = 50
    QTD_ARESTAS = 150
    grafo_ponderado = gerar_grafo_aleatorio(QTD_NOS, QTD_ARESTAS)

    # 2. Configurar nós de início e destino
    NO_INICIO = 1
    NO_DESTINO = 50

    # 3. Executar o Dijkstra e extrair rota/custo
    distancias, nos_anteriores = dijkstra(grafo_ponderado, NO_INICIO, NO_DESTINO)
    rota = reconstruir_rota(nos_anteriores, NO_INICIO, NO_DESTINO)

    # Imprimir saída no terminal
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