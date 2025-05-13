# Questão 1 – Verificação de lista ordenada

# A função abaixo tem como objetivo verificar se uma lista de números inteiros está em ordem crescente.
# No entanto, o uso da variável 'sim' dentro do laço não é necessário e pode causar confusão.
# A cada iteração, ela é atualizada mesmo que a lista esteja parcialmente correta,
# e só será confiável se o laço for interrompido corretamente.
# Além disso, o código percorre toda a lista mesmo quando já é possível concluir que a ordem foi quebrada.

# Uma forma mais eficiente e clara de resolver isso é retornar 'False' assim que for encontrado um par fora de ordem.
# Se todas as comparações forem válidas, a função retorna 'True' ao final.

def verifica(lista):
    for i in range(1, len(lista)):
        if lista[i - 1] > lista[i]:
            return False
    return True

teste1 = [1, 2, 3, 4, 5]
teste2 = [10, 5, 8, 12]

print("Lista 1 está ordenada?", verifica(teste1))
print("Lista 2 está ordenada?", verifica(teste2))  
