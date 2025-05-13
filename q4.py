# Questão 4 – Análise de alterações no Selection Sort

# Alteração A:
# Alterar for i in range(0, n - 1) para for i in range(1, n - 1)
# Impacto: O algoritmo ignora a posição 0, ou seja, não posiciona o menor elemento na primeira posição.
# Isso compromete a ordenação correta. A primeira posição pode ficar incorreta.

# Alteração B:
# Alterar for i in range(0, n - 1) para for i in range(0, n)
# Impacto: Neste caso, na última iteração o índice 'i' será n-1.
# Isso faz com que o laço interno for j in range(i + 1, n) tente acessar fora dos limites do vetor.
# Pode gerar erro em tempo de execução (IndexError).

# Alteração C:
# Alterar if array[j] < array[min_index] para if array[j] <= array[min_index]
# Impacto: O algoritmo ainda funciona corretamente, mas passa a ser estável.
# Isso porque, em caso de valores iguais, ele não troca a posição atual, mantendo a ordem original dos iguais.
# Essa mudança não compromete a ordenação, apenas melhora a estabilidade do algoritmo.

# Resumo do algoritmo:
# O Selection Sort percorre o vetor encontrando o menor elemento e trocando com a posição atual.
# Ele realiza (n - 1) passagens, sendo eficiente em memória, mas com complexidade O(n²).
# É um algoritmo simples, porém pouco eficiente para grandes volumes de dados.
