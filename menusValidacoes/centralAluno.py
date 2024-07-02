import os
from unittest import case
opcao = 0
continuar = "s"

print("Central do Aluno")
nomeAluno = input("Digite o seu nome: ")
while continuar == "s":
    while opcao < 1 or opcao > 3:
        print("\n1-Verificar notas e faltas")
        print("2-Dúvidas")
        print("3-Sair")
        opcao = int(input("\nQual é a sua opção?"))
        if opcao < 1 or opcao > 3:
            print("Opção Inválida!")
    os.system("cls")

    match (opcao):
        case 1: 
            print("Notas e faltas\n", nomeAluno,
                   "\nGeografia         Quant.Faltas: 5  Nota: 10",
                   "\nFilosofia         Quant.Faltas: 2  Nota: 4",
                   "\nSociologia        Quant.Faltas: 3  Nota: 6")
        case 2: 
            print("Dúvidas") 
            duvida = input("Digite aqui a sua dúvida")
            os.system("cls")
            print("Sua dúvida foi enviada ao professor, por favor, aguarde uma resposta dele.")

        case 3: 
            print("Sessão finalizada!")
    
    continuar = input("\nDeseja realizar outro procedimento?")
    opcao = 0    
                        

   