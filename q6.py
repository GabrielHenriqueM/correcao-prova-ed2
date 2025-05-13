# Questão 6 – Correção do algoritmo de ordenação por inserção

def insertion_sort(v):
    n = len(v)
    for j in range(1, n):
        x = v[j]
        i = j - 1
        while i >= 0 and v[i] > x:
            v[i + 1] = v[i]
            i -= 1
        v[i + 1] = x 

# Explicação:
# A implementação original apresenta erro na ordem das instruções:
# O decremento de 'i' (i -= 1) está fora do laço while, e a inserção de 'x' está sendo feita em v[i],
# mas nesse momento 'i' já foi decrementado. Isso faz com que o valor seja inserido na posição errada.
# A correção adequada é inserir 'x' em v[i + 1], pois essa será a posição correta após deslocar os elementos maiores.

lista = [9, 3, 7, 1, 5]
insertion_sort(lista)
print("Lista ordenada:", lista)  
