#Aluno: Caua Veloso Oliveira
#//Matricula: 2021026568
#BICT - UFMA
#Disciplina: Inteligencia Artificial - 2025.1
#Docente: Prof.Dr. Thales Levi Azevedo Valente

#Grafos gerados pela plataforma online COLAB


from graphviz import Digraph
from IPython.display import display, Image
import os

def coin_change_greedy_with_graph(coins, amount, filename='grafo_troco'):
    """
    Algoritmo guloso do troco mínimo com geração de grafo
    Versão otimizada para o Colab sem warnings
    """
    coins = sorted(coins, reverse=True)
    num_coins = 0
    combination = []

    # Cria o objeto do grafo com configurações seguras
    dot = Digraph(comment='Grafo de Decisões do Troco Mínimo')
    dot.attr(rankdir='TB', engine='dot')
    dot.attr('node', shape='ellipse', style='filled', fillcolor='lightblue', fontname='Arial')
    dot.attr('edge', fontname='Arial')

    # Nó inicial seguro (sem caracteres especiais)
    current_node = f"Inicio_{amount}"
    dot.node(current_node, label=f"Início\n{amount}")

    for coin in coins:
        if amount == 0:
            break

        count = amount // coin
        if count > 0:
            combination.append((coin, count))
            num_coins += count
            new_amount = amount - count * coin

            # Cria nós com IDs seguros e labels amigáveis
            next_node = f"Node_{coin}_{count}_{new_amount}"
            dot.node(next_node, label=f"Usar {count}×{coin}\nResto: {new_amount}")
            dot.edge(current_node, next_node)

            current_node = next_node
            amount = new_amount

    # Configurações de renderização
    dot.format = 'png'

    # Caminho completo para salvar o arquivo
    filepath = f"/content/{filename}"
    dot.render(filepath, cleanup=True)

    # Exibe a imagem
    display(Image(filename=f"{filepath}.png"))

    if amount != 0:
        return -1, []

    return num_coins, combination

# Exemplo de uso no Colab
print("=== EXEMPLO 1 ===")
coins1 = [1, 5, 10, 25]
amount1 = 63
num_coins1, combination1 = coin_change_greedy_with_graph(coins1, amount1, 'troco_exemplo1')

print("\nNúmero mínimo de moedas:", num_coins1)
print("Combinação de moedas:")
for coin, count in combination1:
    print(f"{count} moeda(s) de {coin}")

print("\n=== EXEMPLO 2 ===")
coins2 = [1, 3, 4]
amount2 = 6
num_coins2, combination2 = coin_change_greedy_with_graph(coins2, amount2, 'troco_exemplo2')

print("\nNúmero mínimo de moedas:", num_coins2)
print("Combinação de moedas:")
for coin, count in combination2:
    print(f"{count} moeda(s) de {coin}")



##Saida Esperada:

""""
=== EXEMPLO 1 ===


Número mínimo de moedas: 6
Combinação de moedas:
2 moeda(s) de 25
1 moeda(s) de 10
3 moeda(s) de 1

=== EXEMPLO 2 ===


Número mínimo de moedas: 3
Combinação de moedas:
1 moeda(s) de 4
2 moeda(s) de 1
