class GrafoMatriz:
    def __init__(self, ponderado=False, direcionado=False):
        self.vertices = []          # Lista de rótulos dos vértices
        self.matriz = []            # Matriz de adjacência
        self.ponderado = ponderado
        self.direcionado = direcionado

    # INSERIR VÉRTICE
    def inserirVertice(self, rotulo):

        self.vertices.append(rotulo)

        # Adiciona nova linha e coluna na matriz
        tamanho = len(self.vertices)
        for linha in self.matriz:
            linha.append(0)
        self.matriz.append([0] * tamanho)
        return True

    # REMOVER VÉRTICE
    def removerVertice(self, rotulo):
        if rotulo not in self.vertices:
            return False
        indice = self.vertices.index(rotulo)

        # Remove linha e coluna da matriz
        self.matriz.pop(indice)
        for linha in self.matriz:
            linha.pop(indice)

        # Remove vértice da lista
        self.vertices.remove(rotulo)
        return True

    # INSERIR ARESTA
    def inserirAresta(self, origem, destino, peso=1):

        # Verifica se os vértices de origem e destino existe no gráfico
        if origem not in self.vertices or destino not in self.vertices:
            return False

        # Pega o valor de índice da origem e destino
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)

        # Atribui o valor do peso na aresta se for ponderado, do contrário atribui 1
        valor = peso if self.ponderado else 1
        self.matriz[i][j] = valor

        # Se não for direcionado atribui do destino à origem também
        if not self.direcionado:
            self.matriz[j][i] = valor
        return True

    # REMOVER ARESTA
    def removerAresta(self, origem, destino):

        # Se o vértice de Origem ou Destino não existir na lista de vértices
        if origem not in self.vertices or destino not in self.vertices:
            return False

        # Pega o índice na lista auxiliar para usar na matriz
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)

        # Remove aresta zerando a célula da matriz
        self.matriz[i][j] = 0

        # Se não for um grafo direcionado
        if not self.direcionado:

            # Também remove aresta no sentido inverso na matriz
            self.matriz[j][i] = 0

        return True

    # EXISTE ARESTA
    def existeAresta(self, origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            return False
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)
        return self.matriz[i][j] != 0

    def pesoAresta(self, origem, destino):

        # Define a linha i e coluna j
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)

        return self.matriz[i][j]

    # RETORNAR PESO
    def retornarPeso(self, origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            return None
        i = self.vertices.index(origem)
        j = self.vertices.index(destino)
        return self.matriz[i][j]

    # RETORNAR VIZINHOS
    def retornarVizinhos(self, vertice):
        if vertice not in self.vertices:
            return []
    
        vizinhos = []
        idx_origem = self.vertices.index(vertice)
    
        for idx_destino, peso in enumerate(self.matriz[idx_origem]):
            if peso is not None and peso != 0:
                vizinhos.append(self.vertices[idx_destino])
    
        return vizinhos  # Recuado dentro do bloco do def

    def retornaVertice(self, origem):
        pass

    # IMPRIMIR MATRIZ
    def imprimirGrafo(self):
        print("\nMatriz de Adjacência:")
        print("   " + " ".join(self.vertices))
        for idx, linha in enumerate(self.matriz):
            print(self.vertices[idx], linha)

    # FUNÇÃO EXISTE VÉRTICE
    def existeVertice(self, rotulo):
        return rotulo in self.vertices

    def rotulaVertice(self, rotulo, novo_rotulo):
        # Verifica se o vértice existe no Grafo
        # Para cada Vértice no Grafo
        for vertice in self.vertices:

            # Se o vértice existir
            if vertice.rotulo == rotulo:
                # Atualiza Rótulo
                vertice.rotulo = novo_rotulo
                return True

        # Senão retorna Falso
        return False
        
    # BUSCA EM LARGURA (BFS)
    def bfs(self, inicio):
        if inicio not in self.vertices:
            return []

        visitados = []
        fila = [inicio]

        while fila:
            vertice = fila.pop(0)  # Remove do início (FIFO)
            if vertice not in visitados:
                visitados.append(vertice)
                # Adiciona vizinhos não visitados à fila
                for vizinho in self.retornarVizinhos(vertice):
                    if vizinho not in visitados and vizinho not in fila:
                        fila.append(vizinho)

        return visitados

    # BUSCA EM PROFUNDIDADE (DFS)
    def dfs(self, inicio, visitados=None):
        if inicio not in self.vertices:
            return []

        if visitados is None:
            visitados = []

        if inicio not in visitados:
            visitados.append(inicio)
            for vizinho in self.retornarVizinhos(inicio):
                if vizinho not in visitados:
                    self.dfs(vizinho, visitados)

        return visitados
        
    # OBTER TRANSPOSTO
    def obterTransposto(self):
        transposto = GrafoMatriz(self.ponderado, self.direcionado)
        transposto.vertices = list(self.vertices)
        n = len(self.vertices)
        transposto.matriz = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                transposto.matriz[j][i] = self.matriz[i][j]

        return transposto

    # TRANSITIVO DIRETO
    def fechoTransitivoDireto(self, v):
        if not self.existeVertice(v):
            return []
        return self.dfs(v)

    # TRASITIVO INVERSO
    def fechoTransitivoInverso(self, v):
        if not self.existeVertice(v):
            return []
        grafo_inv = self.obterTransposto()
        return grafo_inv.dfs(v)
        
