# Questão 3 – Contagem de trocas no Bubble Sort

def bubble_sort_contando_trocas(array):
    tamanho = len(array)
    trocas = 0
    for i in range(tamanho):
        for j in range(0, tamanho - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trocas += 1
    return trocas

vetor = [77, 51, 11, 37, 29, 13, 21]
trocas_realizadas = bubble_sort_contando_trocas(vetor.copy())

print("Total de trocas realizadas:", trocas_realizadas)
print("Vetor ordenado:", vetor)

# Explicação:
# O algoritmo Bubble Sort compara e troca elementos adjacentes quando necessário.
# Ao contar o número de trocas feitas até que o vetor esteja ordenado,
# obtemos a resposta da questão. No caso deste vetor, o total de trocas será 16.

# Código criado para vacilitar a contagem, porém na prova basta seguir uma contagem manual, resposta 16 trocas realizadas.
