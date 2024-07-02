a = float(input("Digite o sua altura: "))
b = float(input("Digite a seu peso:"))
while(a == 0 and b == 0):
    print("Peso e altura devem ser maiores que zero")

calc = b / a ** 2
print("Seu IMC é este: ", calc)

if (calc >= 16 and calc < 17):
    print("Você está muito abaixo do peso")
elif (calc >= 17 and calc < 18.5):
    print("Você está abaixo do peso")
elif (calc >= 18.5 and calc < 25):
    print("Você está com peso normal")    
elif (calc >= 25 and calc < 30):
    print("Você está acima do peso")
elif (calc >= 30 and calc < 35):
    print("Você está com Obesidade de Grau I")
elif (calc >= 35 and calc < 40):
    print("Você está com Obesidade de Grau II")
