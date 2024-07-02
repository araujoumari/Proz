tamanho = False
repetir = "s"

while not tamanho and repetir == "s":
    cpf =  input("Digite o seu cpf: ")

    if len(cpf) == 11:
        tamanho = True
    if not tamanho:
        print("CPF inválido") 
        repetir = input("Deseja repetir? s/n")          
