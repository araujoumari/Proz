tamanho = False
repetir = "s"

while not tamanho and repetir == "s":
    rg =  input("Digite o seu rg: ")

    if len(rg) == 9:
        tamanho = True
    if not tamanho:
        print("RG inválido") 
        repetir = input("Deseja repetir? s/n")          
