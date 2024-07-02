a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

delta = b**2 -((4*a)*c)

baskharaX1 = (-b + delta) / (2*a)
baskharaX2 = (-b - delta) / (2*a)

baskharaX1_lim = round(baskharaX1, 4)
baskharaX2_lim = round(baskharaX2, 4)

if delta > 0:
    print(f"O X1 é: {baskharaX1_lim}\n"
      f"O X2 é: {baskharaX2_lim}")
else:
    print("Não existe raízes reais para essa equação")    