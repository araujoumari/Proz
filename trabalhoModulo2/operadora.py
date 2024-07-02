minutos = int(input("Digite a quantidade de minutos: "))

if minutos <= 100:
    total = 50
    print(f"O valor total a pagar é: R${total}")
else: 
    total = 50 + ((minutos - 100) * 2)
    print(f"O valor total a pagar é: R${total}")  