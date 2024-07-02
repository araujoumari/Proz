tem_arroba = False
tem_ponto = False

while not tem_arroba or not tem_ponto:
    nome = input("Digite o seu email: ")
    for letra in nome:
        if nome == letra:
            tem_arroba = True
        if letra == ".":
            tem_ponto = True
    if not tem_arroba or not tem_ponto:
        print("Email inválido")    