valores = []
continuar = 's'

while continuar == 's':
    valores.append(int(input("Digite um valor: ")))
    continuar = input("Deseja digitar outro valor? ")

menor = min(valores)
print(menor)
