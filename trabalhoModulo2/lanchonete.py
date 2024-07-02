tabela = {
    1 : 5.00,
    2 : 3.50,
    3 : 4.80,
    4 : 8.90,
    5 : 7.32
}

codigo = int(input("Digite o código do profuto comprado: "))
quant = int(input("Digite a quantidade comprada: "))

valor = tabela[int(codigo)] * quant

print(valor)