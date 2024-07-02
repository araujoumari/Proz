inicio = float(input("Digite quantas horas o jogo começou: "))

fim = float(input("Digite quantas horas o jogo terminou:"))

duracao = inicio - fim

if duracao < 1:
    print("O jogo durou menos que uma hora")
elif duracao > 24 :     
    print("O jogos durou mais que 1 dia")
else:
    print(f"O jogo durou {duracao} horas")    

