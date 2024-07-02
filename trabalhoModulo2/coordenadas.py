x = int(input("Digite o valor da coordenada x: "))
y = int(input("Digite o valor da coordenada y: "))

def quadrantes(x,y):
    if x > 0 and y > 0:
        qdr = "Quadrante 1"
        return qdr
    elif x < 0 and y < 0:
        qdr = "Quadrante 3"
        return qdr
    elif x > 0 and y < 0:
        qdr = "Quadrante 4"
        return qdr
    elif x < 0 and y > 0:
        qdr = "Quadrante 2"
        return qdr

print("O valor de x é: ", x)
print("O valor de x y: ", y) 
print(quadrantes(x,y))