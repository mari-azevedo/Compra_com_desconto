#Entrada dos dados
valor = float(input())
desconto = float(input())

#Aplicando o desconto
valordescontado = valor - (valor * (desconto / 100))

#Imprimindo o valor original
print('%.2f' % valor)

#Imprimindo o valor descontado
print('%.2f' % valordescontado)

#Imprimindo a diferença
print('%.2f' % (valor - valordescontado))
