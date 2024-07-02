vazio = False
repetir = "s"

while vazio == False and repetir == "s":
    campo = input("Preencha este campo: ")

    if not campo:
        vazio = False
        print("Campo vazio")
    if campo:
        vazio = True
