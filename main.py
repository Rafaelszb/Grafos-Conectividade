# Trabalho de Grafos Python
# Guilherme Melo de Jesus e Rafael de Souza Barbosa

import GrafoMatriz

# MENU DO GRAFO CRIADO
def menu():
    print("\n" + "=" * 30)
    print("1 - Inserir Vértice")
    print("2 - Remover Vértice")
    print("3 - Rotular Vértice")
    print("4 - Imprimir Grafo")
    print("5 - Inserir Aresta")
    print("6 - Remover Aresta")
    print("7 - Existe Aresta")
    print("8 - Peso Aresta")
    print("9 - Retorna Vizinhos")
    print("10 - BUSCAS")
    print("11 - Fecho Transitivo Direto")
    print("12 - Fecho Transitivo Inverso") 
    print("0 - SAIR DO GRAFO")
    print("=" * 30)

    try:
        menuGrafo = int(input("Escolha uma opção: "))
        return menuGrafo
    except ValueError:
        return -1


def gerenciar_grafo(grafo, ponderado, direcionado):
    """Executa o loop de operações para o grafo criado."""
    menuGrafo = menu()
    while menuGrafo != 0:

        # 1 - INSERIR VÉRTICE
        if menuGrafo == 1:
            rotulo = str(input("Insira um rótulo para o Vértice: ")).strip()
            if grafo.existeVertice(rotulo):
                print("\nVÉRTICE JÁ EXISTENTE!")
            else:
                if grafo.inserirVertice(rotulo):
                    print("\nVértice inserido com sucesso!")
                else:
                    print("\nErro ao inserir vértice!")

        # 2 - REMOVER VÉRTICE
        elif menuGrafo == 2:
            rotulo = str(input("Insira o rótulo do vértice a ser excluído: ")).strip()
            if grafo.removerVertice(rotulo):
                print("\nVértice removido com sucesso!")
            else:
                print("\nVértice não existe!")

        # 3 - ROTULAR VÉRTICE
        elif menuGrafo == 3:
            rotulo = str(input("Insira o vértice a ser editado: ")).strip()
            novo_rotulo = str(input("Insira o novo rótulo: ")).strip()
            if grafo.rotulaVertice(rotulo, novo_rotulo):
                print("\nVértice editado com sucesso!")
            else:
                print("\nFalha ao renomear (vértice de origem não existe ou novo rótulo é duplicado).")

        # 4 - IMPRIMIR GRAFO
        elif menuGrafo == 4:
            grafo.imprimirGrafo()

        # 5 - INSERIR ARESTA
        elif menuGrafo == 5:
            origem = str(input("Insira o Vértice de Origem: ")).strip()
            destino = str(input("Insira o Vértice de Destino: ")).strip()
            peso = 1

            if ponderado:
                try:
                    peso = int(input("Insira o Peso da Aresta: "))
                except ValueError:
                    print("Peso inválido. Usando valor 1.")

            if grafo.inserirAresta(origem, destino, peso):
                print(f"\nAresta inserida com sucesso entre '{origem}' e '{destino}'!")
            else:
                print("\nFALHA AO INSERIR ARESTA (Verifique se os vértices existem).")

        # 6 - REMOVER ARESTA
        elif menuGrafo == 6:
            origem = str(input("Insira o Vértice de Origem: ")).strip()
            destino = str(input("Insira o Vértice de Destino: ")).strip()

            if grafo.removerAresta(origem, destino):
                print(f"\nAresta entre '{origem}' e '{destino}' removida com sucesso!")
            else:
                print(f"\nNão foi possível remover (verifique se a aresta ou os vértices existem).")

        # 7 - EXISTE ARESTA
        elif menuGrafo == 7:
            origem = str(input("Insira o Vértice de Origem: ")).strip()
            destino = str(input("Insira o Vértice de Destino: ")).strip()

            if grafo.existeAresta(origem, destino):
                print(f"\nExiste aresta entre '{origem}' e '{destino}'.")
            else:
                print(f"\nNÃO existe aresta entre '{origem}' e '{destino}'.")

        # 8 - PESO ARESTA
        elif menuGrafo == 8:
            origem = str(input("Insira o Vértice de Origem: ")).strip()
            destino = str(input("Insira o Vértice de Destino: ")).strip()

            peso = grafo.retornarPeso(origem, destino)
            if peso is not None and peso != 0:
                print(f"\nO peso da aresta ({origem} -> {destino}) é: {peso}")
            else:
                print(f"\nNÃO existe aresta entre '{origem}' e '{destino}'.")

        # 9 - RETORNA VIZINHOS
        elif menuGrafo == 9:
            origem = str(input("Insira o Vértice de Origem: ")).strip()
            if grafo.existeVertice(origem):
                vizinhos = grafo.retornarVizinhos(origem)
                print(f"\nVizinhos de '{origem}': {vizinhos}")
            else:
                print("\nVértice não encontrado no grafo.")

        # 10 - BUSCAS
        elif menuGrafo == 10:
            inicio = str(input("Insira o Vértice de Início para a busca: ")).strip()
            if not grafo.existeVertice(inicio):
                print("\nVértice de início não existe no grafo!")
            else:
                print("\n1 - Busca em Largura (BFS)")
                print("2 - Busca em Profundidade (DFS)")
                tipo_busca = input("Escolha o tipo de busca: ").strip()

                if tipo_busca == "1":
                    resultado = grafo.bfs(inicio)
                    print(f"\nOrdem de visita (BFS a partir de '{inicio}'): {' -> '.join(resultado)}")
                elif tipo_busca == "2":
                    resultado = grafo.dfs(inicio)
                    print(f"\nOrdem de visita (DFS a partir de '{inicio}'): {' -> '.join(resultado)}")
                else:
                    print("\nOpção de busca inválida.")

        # 11 - FECHO TRANSITIVO DIRETO
        elif menuGrafo == 11:
            vertice = input("Insira o Vértice: ").strip()
            if grafo.existeVertice(vertice):
                ftd = grafo.fechoTransitivoDireto(vertice)
                print(f"\nFecho Transitivo Direto de '{vertice}': {set(ftd)}")
            else:
                print("\nVértice não existe!")

        # 12 - FECHO TRANSITIVO INVERSO
        elif menuGrafo == 12:
            vertice = input("Insira o Vértice: ").strip()
            if grafo.existeVertice(vertice):
                fti = grafo.fechoTransitivoInverso(vertice)
                print(f"\nFecho Transitivo Inverso de '{vertice}': {set(fti)}")
            else:
                print("\nVértice não existe!")

        menuGrafo = menu()


# INÍCIO DO PROGRAMA
while True:
    print("\n--- TRABALHO DE GRAFOS ---")
    print("1 - Criar Grafo em Matriz Manualmente")
    print("2 - Criar Grafo Automaticamente (Matriz)")
    print("0 - SAIR DO PROGRAMA")

    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida.")
        continue

    if opcao == 0:
        print("Saindo do programa...")
        break

    dir_input = str(input("O Grafo é Direcionado? (S/N): ")).strip().upper()
    pond_input = str(input("O Grafo é Ponderado? (S/N): ")).strip().upper()

    direcionado = (dir_input == "S")
    ponderado = (pond_input == "S")

    # 1 - MATRIZ MANUAL
    if opcao == 1:
        grafo = GrafoMatriz.GrafoMatriz(ponderado, direcionado)
        gerenciar_grafo(grafo, ponderado, direcionado)

    # 2 - MATRIZ AUTOMÁTICO
    elif opcao == 2:
        grafo = GrafoMatriz.GrafoMatriz(ponderado, direcionado)
        for v in ["A", "B", "C", "D", "E"]:
            grafo.inserirVertice(v)

        grafo.inserirAresta("A", "B", 15)
        grafo.inserirAresta("A", "C", 10)
        grafo.inserirAresta("B", "C", 10)
        grafo.inserirAresta("C", "D", 15)
        grafo.inserirAresta("D", "E", 10)

        print("\n[Grafo em Matriz gerado com sucesso!]")
        gerenciar_grafo(grafo, ponderado, direcionado)
