# Questão 5 – Melhor e Pior Caso do Selection Sort

# a) Pior caso:
# O pior caso do Selection Sort ocorre quando o vetor está em ordem decrescente,
# pois o algoritmo terá que procurar o menor elemento em todas as posições em cada iteração.

vetor_pior_caso = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Comparações no pior caso:
# O algoritmo faz sempre (n - i - 1) comparações a cada iteração externa.
# Total de comparações: (n-1) + (n-2) + ... + 1 = n(n - 1)/2
# Para 9 elementos: 9 * (9 - 1) / 2 = 36 comparações

# b) Melhor caso:
# O melhor caso também realiza o mesmo número de comparações,
# pois o Selection Sort não verifica se o vetor já está ordenado.
# Mesmo com a lista em ordem crescente, ele continua procurando o menor elemento.
# A única diferença é que não haverá trocas desnecessárias.

vetor_melhor_caso = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Comparações no melhor caso:
# Mesmo cálculo: 9 * (9 - 1) / 2 = 36 comparações

# Conclusão:
# O número de comparações no Selection Sort é fixo: n(n - 1)/2, independentemente da ordem dos dados.
# O que muda entre melhor e pior caso é a quantidade de trocas, que será máxima no pior caso e mínima no melhor.
