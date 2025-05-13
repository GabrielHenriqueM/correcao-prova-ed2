# Questão 2 – Bubble Sort com verificação de parada antecipada

def bubble_sort(array):
    tamanho = len(array)
    for i in range(tamanho):
        houve_troca = False 
        for j in range(0, tamanho - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                houve_troca = True
        if not houve_troca:
            break  

# Explicação:
# A variável 'houve_troca' permite detectar se o vetor já está ordenado.
# Se em uma passagem completa nenhuma troca for realizada, o algoritmo termina antes do fim.
# Isso reduz o número de comparações em casos onde o vetor está totalmente ou parcialmente ordenado,
# tornando o algoritmo mais eficiente nessas situações.

lista1 = [7, 4, 3, 8, 1]
lista2 = [1, 2, 3, 4, 5] 

bubble_sort(lista1)
bubble_sort(lista2)

print("Lista 1 ordenada:", lista1)
print("Lista 2 ordenada:", lista2) 
