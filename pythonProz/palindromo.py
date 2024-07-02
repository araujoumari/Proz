numero = input("Digite um número: ")

quant = len(numero) #quantidade recebe o tamanho do número, ex: 34543 (quant = 5)
print(quant) 

palindromo = True
fim = quant - 1 #variável "fim" recebe quantidade menos 1, ex: quant = 4

for x in range(0, int(quant/2)): #contador que começa do 0 e vai até o número da variável quant dividida por 2, ex: quant = 2
    if numero[x] != numero[fim]: #se numero recebe x(números em 'numero') for diferente de numero recebe fim(quant - 1(ex: quant = 4))...
        palindromo = False

    fim -= 1 # fim recebe ele mesmo menos 1, ex: fim = 4, agora o fim = 3
if palindromo: #se palindromo não for falso ele é verdaddeiro, logo este bloco será executado
    print("É um número palíndromo")        