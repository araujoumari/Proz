bimestreUm = float(input("Digite a suas notas do primeiro bimestre: "))
bimestreDois = float(input("Digite suas notas do segundo bimestre: "))

soma = bimestreUm + bimestreDois
soma_limitada = round(soma, 1)

print(f"Nota final: {soma_limitada}")

if soma_limitada > 60:
    print("Aprovado")
else:
    print("Reprovado")    