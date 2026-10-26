# ==========================================
# CLASSE GRAFO MATRIZ DE ADJACÊNCIA
# Autores: Guilherme Melo de Jesus e Rafael de Souza Barbosa
# ==========================================

import matplotlib.pyplot as plt
import networkx as nx


class GrafoMatriz:
    def __init__(self, ponderado=False, direcionado=False):
        # Configurações iniciais do grafo
        self.ponderado = ponderado  # Define se as arestas aceitam pesos diferentes de 1
        self.direcionado = direcionado  # Define se as arestas possuem direção única
        self.vertices = []  # Armazena os rótulos dos vértices (ex: ['A', 'B', 'C'])
        self.matriz = []  # Matriz de adjacência em formato de lista de listas

    def existeVertice(self, rotulo):
        # Validação simples para checar se o rótulo já consta na lista de vértices
        return rotulo in self.vertices

    def inserirVertice(self, rotulo):
        # Se o vértice já existir, aborta a operação retornando False
        if self.existeVertice(rotulo):
            return False

        # Adiciona o novo rótulo na lista de vértices
        self.vertices.append(rotulo)

        # Como adicionamos um novo vértice, a matriz precisa crescer (ganhar uma nova coluna em cada linha existente)
        for linha in self.matriz:
            linha.append(0)  # 0 significa que inicialmente não há ligação com o novo vértice

        # Agora criamos a linha correspondente ao vértice recém-adicionado
        # O tamanho da linha deve ser igual ao número total de vértices atuais
        nova_linha = [0] * len(self.vertices)
        self.matriz.append(nova_linha)

        return True

    def removerVertice(self, rotulo):
        # Garante que o vértice realmente existe antes de tentar apagar
        if not self.existeVertice(rotulo):
            return False

        # Descobre qual é a posição (índice) numérica do vértice na lista
        idx = self.vertices.index(rotulo)

        # Remove o vértice da lista de rótulos
        self.vertices.pop(idx)

        # Remove a linha inteira correspondente a esse vértice na matriz
        self.matriz.pop(idx)

        # Remove a coluna correspondente a esse vértice em todas as outras linhas restantes
        for linha in self.matriz:
            linha.pop(idx)

        return True

    def rotulaVertice(self, rotulo, novo_rotulo):
        # Verifica se o vértice antigo existe e se o novo nome escolhido já não está em uso
        if not self.existeVertice(rotulo) or self.existeVertice(novo_rotulo):
            return False

        # Localiza o índice e substitui o nome antigo pelo novo na lista de vértices
        idx = self.vertices.index(rotulo)
        self.vertices[idx] = novo_rotulo
        return True

    def existeAresta(self, origem, destino):
        # Só podemos verificar a aresta se ambos os vértices existirem no grafo
        if self.existeVertice(origem) and self.existeVertice(destino):
            # Mapeia os rótulos para os índices da matriz
            idx_origem = self.vertices.index(origem)
            idx_destino = self.vertices.index(destino)

            # Se o valor na matriz for diferente de 0, significa que a aresta existe
            return self.matriz[idx_origem][idx_destino] != 0

        return False

    def inserirAresta(self, origem, destino, peso=1):
        # Verifica se os dois vértices informados existem
        if self.existeVertice(origem) and self.existeVertice(destino):
            idx_origem = self.vertices.index(origem)
            idx_destino = self.vertices.index(destino)

            # Insere o peso na posição de ida (origem -> destino)
            self.matriz[idx_origem][idx_destino] = peso

            # Se o grafo NÃO for direcionado, a aresta vale para os dois lados (matriz simétrica)
            if not self.direcionado:
                self.matriz[idx_destino][idx_origem] = peso

            return True
        return False

    def removerAresta(self, origem, destino):
        # Usa a verificação de existência para garantir que a aresta pode ser apagada
        if self.existeAresta(origem, destino):
            idx_origem = self.vertices.index(origem)
            idx_destino = self.vertices.index(destino)

            # Zera a posição na matriz (removendo a conexão)
            self.matriz[idx_origem][idx_destino] = 0

            # Se o grafo não for direcionado, zera também a volta
            if not self.direcionado:
                self.matriz[idx_destino][idx_origem] = 0

            return True
        return False

    def retornarPeso(self, origem, destino):
        # Checa se a aresta existe para evitar erros de índice ou valores inválidos
        if self.existeAresta(origem, destino):
            idx_origem = self.vertices.index(origem)
            idx_destino = self.vertices.index(destino)
            # Retorna exatamente o número salvo na matriz
            return self.matriz[idx_origem][idx_destino]
        return None

    def retornarVizinhos(self, origem):
        vizinhos = []
        if self.existeVertice(origem):
            idx_origem = self.vertices.index(origem)

            # Percorre todas as colunas da linha do vértice de origem
            for i in range(len(self.vertices)):
                # Se o valor for diferente de 0, há uma aresta conectando ao vértice da coluna 'i'
                if self.matriz[idx_origem][i] != 0:
                    vizinhos.append(self.vertices[i])

        return vizinhos

    def imprimirGrafo(self):
        # Imprime o cabeçalho superior com os nomes dos vértices alinhados às colunas
        print("\n   ", "  ".join(self.vertices))
        # Imprime cada linha da matriz precedida pelo rótulo do vértice correspondente
        for i, linha in enumerate(self.matriz):
            print(f"{self.vertices[i]} {linha}")

    def bfs(self, inicio):
        # Busca em Largura (Breadth-First Search)

        # Lista de vértices visitados
        visitados = []
        # Fila de controle para visitar os nós por ordem de chegada (FIFO)
        fila = [inicio]
        visitados.append(inicio)

        while len(fila) > 0:
            # Pega o primeiro elemento da fila para processar
            vertice = fila.pop(0)

            # Olha todos os vizinhos conectados a ele
            for vizinho in self.retornarVizinhos(vertice):
                # Se o vizinho ainda não foi visitado, adiciona na lista e joga no final da fila
                if vizinho not in visitados:
                    visitados.append(vizinho)
                    fila.append(vizinho)

        return visitados

    def dfs(self, inicio, visitados=None):
        # Busca em Profundidade (Depth-First Search) utilizando recursão
        if visitados is None:
            visitados = []

        # Se o vértice atual ainda não foi visitado, marca ele
        if inicio not in visitados:
            visitados.append(inicio)

            # Para cada vizinho, chama a DFS recursivamente aprofundando o caminho
            for vizinho in self.retornarVizinhos(inicio):
                self.dfs(vizinho, visitados)

        return visitados

    def fechoTransitivoDireto(self, vertice):
        # O fecho transitivo direto utiliza a lógica da BFS para encontrar tudo o que é alcançável partindo do vértice
        return self.bfs(vertice)

    def fechoTransitivoInverso(self, vertice):
        visitados = []
        fila = [vertice]
        visitados.append(vertice)

        while len(fila) > 0:
            atual = fila.pop(0)
            idx_atual = self.vertices.index(atual)

            # Diferente do direto, aqui varremos as LINHAS da coluna do vértice atual
            # para descobrir quem aponta PARA ele (origens)
            for i in range(len(self.vertices)):
                if self.matriz[i][idx_atual] != 0:
                    v_origem = self.vertices[i]
                    if v_origem not in visitados:
                        visitados.append(v_origem)
                        fila.append(v_origem)

        return visitados

    def verificarPlanaridade(self):
        v = len(self.vertices)
        if v <= 2:
            return True  # Grafos com até 2 vértices são sempre planares

        # Conta o total de arestas presentes na matriz
        e = 0
        for i in range(v):
            for j in range(v):
                if self.matriz[i][j] != 0:
                    e += 1

        # Se o grafo for não-direcionado, dividimos por 2 porque cada aresta foi contada duas vezes (ida e volta)
        if not self.direcionado:
            e = e // 2

        # Aplicação da fórmula de Euler simplificada para grafos simples: e <= 3*v - 6
        return e <= (3 * v - 6)

    def verificarConexo(self):
        if len(self.vertices) == 0:
            return {"conexo": True, "componentes": []}

        # Pega o primeiro vértice como ponto de partida
        inicio = self.vertices[0]
        # Roda a BFS para ver quais vértices conseguem ser alcançados a partir dele
        alcancaveis = self.bfs(inicio)

        # O grafo é considerado conexo se conseguimos alcançar todos os vértices existentes
        conexo = len(alcancaveis) == len(self.vertices)
        return {"conexo": conexo, "componentes": [alcancaveis]}

    def plotarColoracao(self, coloracao):
        """Desenha o grafo usando as cores calculadas por coloracaoGrafo()."""
        if not self.vertices:
            print("Grafo sem vértices para desenhar.")
            return

        # Para grafos direcionados, as setas são preservadas no desenho.
        G = nx.DiGraph() if self.direcionado else nx.Graph()
        G.add_nodes_from(self.vertices)

        # Constrói as arestas a partir da matriz de adjacência.
        for i, origem in enumerate(self.vertices):
            for j, destino in enumerate(self.vertices):
                peso = self.matriz[i][j]
                if peso != 0:
                    if self.direcionado:
                        G.add_edge(origem, destino, weight=peso)
                    elif j > i:
                        G.add_edge(origem, destino, weight=peso)

        # Converte os números das cores em cores visuais distintas.
        paleta = [
            "#4E79A7", "#F28E2B", "#59A14F", "#E15759", "#B07AA1",
            "#76B7B2", "#EDC948", "#FF9DA7", "#9C755F", "#BAB0AC"
        ]
        cores_nos = [paleta[(coloracao[v] - 1) % len(paleta)] for v in G.nodes()]
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(9, 6))
        nx.draw_networkx_nodes(
            G, pos, node_color=cores_nos, node_size=1200,
            edgecolors="black", linewidths=1.2
        )
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

        if self.direcionado:
            nx.draw_networkx_edges(
                G, pos, arrows=True, arrowsize=20,
                connectionstyle="arc3,rad=0.08"
            )
        else:
            nx.draw_networkx_edges(G, pos, width=1.8)

        # Mostra os pesos somente se o grafo foi configurado como ponderado.
        if self.ponderado:
            rotulos_arestas = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, pos, edge_labels=rotulos_arestas)

        plt.title(f"Coloração do Grafo ({max(coloracao.values())} cores)")
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def coloracaoGrafo(self):
        # Algoritmo Guloso de Coloração
        coloracao = {}  # Dicionário que guarda a cor atribuída a cada vértice (ex: {'A': 1})

        for vertice in self.vertices:
            if self.direcionado:
                # Na coloração, uma aresta cria conflito independentemente
                # do sentido; considera vizinhos de entrada e de saída.
                idx = self.vertices.index(vertice)
                vizinhos = [
                    outro for j, outro in enumerate(self.vertices)
                    if outro != vertice and
                    (self.matriz[idx][j] != 0 or self.matriz[j][idx] != 0)
                ]
            else:
                vizinhos = self.retornarVizinhos(vertice)

            # Cria uma lista com as cores que os vizinhos diretos já estão usando
            cores_vizinhos = []
            for vizinho in vizinhos:
                if vizinho in coloracao:
                    cor = coloracao[vizinho]
                    if cor not in cores_vizinhos:
                        cores_vizinhos.append(cor)

            # Procura a menor cor inteira positiva disponível (começando de 1)
            # que não entre em conflito com as cores dos vizinhos
            cor_livre = 1
            while cor_livre in cores_vizinhos:
                cor_livre += 1

            # Atribui a cor escolhida ao vértice atual
            coloracao[vertice] = cor_livre

        return coloracao
