Aluno:Helenton Alan Schranck
matricula:2019309379


import math

resultado = ''
h = float(input('digite o valor a ser trans formado em numero binario:'))
s = h
while h > 0:
    #o codigo vai se repetir enquanto h for maior que 0 
    h = h / 2
    if h % 2 == 0:
    # h vai ser dividido pros dois, só o resto da divisão vai ser conputado
        h = h / 2
        resultado = '0' + str(resultado)
    else:
      # se o if for falso sera asecutado:
        h = h / 2
        resultado = '1' + str(resultado)

resultado = str(str('o valor de: ') + str(s)) + ('O numero em  binario:') +str(resultado)
print(resultado)
print(" O valor digitado foi:",s )
