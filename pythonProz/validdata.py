from datetime import datetime
format = False
repetir = "s"

while format == False and repetir == "s":
    data = input("Digite a data: ")
    
    try: 
        datetime.strptime(data, '%d/%m/%Y')#tenta converter data para o formato dd/mm/yyyy
        format = True
    except:
        format = False
        print("Formato inválido")