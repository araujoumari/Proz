cf = input("Você vai digitar a temperatura em qual escala? C/F: ")

cf = "c" or "f"

if cf == "c":
    celsius = float(input("Digite a temperatura em Celsius: "))
    farenheit = (celsius * 1.8) + 32
    print(f"A temperatura em Farenheit é: {farenheit}")
else: 
    farenheit = float(input("Digite a temperatura em Farenheit"))
    celsius = (farenheit - 32) / 1.8