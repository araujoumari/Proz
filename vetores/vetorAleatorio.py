import random #importei biblioteca que vai gerar os valores aleatórios
vetor = [] 

for _ in range(5): #criei um laçõ de repetição onde a variável "_" vai receber 5 valores aleatórios
    numero = random.randint(0,100) #a variável número vai receber os valores aleatórios gerados de 0 a 100
    vetor.append(numero) #guardei a variável número com os valores gerados dentro do vetor

print("Números aleatórios gerados no vetor: ")

print(vetor) #mostrei o vetor com os números aleatórios gerados