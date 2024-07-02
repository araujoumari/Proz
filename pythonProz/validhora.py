from datetime import datetime
format = False
repetir = "s"

while format == False and repetir == "s":
    hora = input("Digite a hora: ")
    
    try: 
        datetime.strptime(hora, '%H:%M')#tenta converter data para o HH:MM
        format = True
    except:
        format = False
        print("Formato inválido")