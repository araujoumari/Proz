maiusc = False
repetir = "s"

while repetir == "s" and maiusc == False:
    nome = input("Digite o seu nome: ")
    
    if nome and nome[0].isupper():
        maiusc = True   
        repetir = "n"
    else:
        maiusc = False
        repetir = input("Nome inválido, repetir o processo? s/n")     