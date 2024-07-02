glicose = float(input("Digite o valor da sua glicose: "))

if glicose < 100:
    print("Normal")
elif glicose >= 100 and glicose <= 140:
    print("Elevado")
else: 
    print("Diabetes")        