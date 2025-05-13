# Questão 7 – Implementação recursiva do Insertion Sort

def insertion_sort_recursivo(v, n=None):
    if n is None:
        n = len(v)

    # Caso base: vetor com 0 ou 1 elemento já está ordenado
    if n <= 1:
        return

    # Chamada recursiva para ordenar os primeiros n-1 elementos
    insertion_sort_recursivo(v, n - 1)

    # Inserção do último elemento (v[n - 1]) no local correto
    ultimo = v[n - 1]
    i = n - 2

    # Desloca elementos maiores que o último para a direita
    while i >= 0 and v[i] > ultimo:
        v[i + 1] = v[i]
        i -= 1

    v[i + 1] = ultimo

lista = [8, 3, 5, 2, 9]
insertion_sort_recursivo(lista)
print("Lista ordenada:", lista)  

# Explicação:
# A função trata vetores pequenos diretamente (caso base).
# Depois, ordena recursivamente os primeiros n - 1 elementos.
# Por fim, insere o último elemento na posição correta usando deslocamento.
# O vetor é ordenado in-place, sem criar novos vetores.
