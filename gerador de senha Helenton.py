
## Aluno : Helenton Schranck
## matricula: 2019309379

import random

senha = ''
vezes = 0
# Estas inha de comando verifica se 'enquanto' é menor que zero 
# E esecuta o codigo enquanto for verdade
while vezes <= 5:
    # O inport.randint serve para sortear numerros aleatorios.
    num_sorteado = random.randint(0, 9)
        # Transforma  os numerros sorteados en estring, acrecentando 
    #O numerro sorteado ao resultado gerando a sequencia da senha.
    senha = str(senha) + str(num_sorteado)
    vezes  += 1    
t = (senha)


def verificação(y, t):
    # Foi definido uma função para verificar a senha.
    r = []
    y = str(y)
    for i in range(len(y)):
    # A função lé a senha sorteada
        if y[i] in t:
            # Inporta o numero selecionado para a variavel 'i'
            if y[i] == t[i]:
                #Identifica se o numero esta no lugar
                r.append(1)
                #É se a linha anterior for verdade '1' sera adisionado alista
            else:
                # Se a linha anterior for falsa sera esecutada esta linha
                r.append(0)
                # O '0' sera idicionado a lista
        else:
            # Caso a primeira linha de codigo for falsa.
            r.append(-1)
            #append adisiona o numero sorteado a lista 'r'
            # O '-1' sera sera adicionado a lista 
    return r
    # A variavel 'r' resetara seu valor


y = input("digitea senha:")
# Foi definido a variavel 's'
print(verificação(y, t))
# Mostrara oresultado do codigo
