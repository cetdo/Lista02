# Carlos Eduardo T. de Oliveira Matrícula: 1715310030
#Média entre 4 números
print('Média entre 4 notas bimestrais')
try:
    n1 = input('Entre com a nota do Primeiro Bimestre: ') #Entrada de nota via teclado
    n1 = int(n1) #conversão do valor de String para int
    n2 = input('Entre com a nota do Segundo Bimestre: ') #Entrada de nota via teclado
    n2 = int(n2) #conversão do valor de String para int
    n3 = input('Entre com a nota do Terceiro Bimestre: ') #Entrada de nota via teclado
    n3 = int(n3) #conversão do valor de String para int
    n4 = input('Entre com a nota do Quarto Bimestre: ') #Entrada de nota via teclado
    n4 = int(n4) #conversão do valor de String para int
    nf = (n1 + n2 + n3+ n4)/4 #fazendo o calculo da média
    print('A média final do aluno é: ', nf)
except ValueError: #caso algum dos valores de notas tenha sido colocadod e maneira errada o programa avisa que houve erro
    print('Somento números são aceitos, tente novamente!') #mensagem de erro