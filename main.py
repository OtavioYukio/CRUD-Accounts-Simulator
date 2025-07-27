from controllers.userController import *
from entities.user import User

dataList = []
loop = True

while (loop):
    option = int(input("\n\n-------------\n\nO que você deesja fazer?\n1 - Criar usuário\n2 - Listar usuários\n3 - Editar usuário\n4 - Deletar usuário\n0 - Sair\n"))

    match(option):
        case 1:
            email = input("Insira seu endereço de email: ")
            name = input("Insira seu nome: ")
            password = input("Insira sua senha: ")
            createUser(dataList, email, name, password)
        case 2:
            readOption = int(input("O que deseja?\n1 - Ler um usuário\n2 - Ler todos os usuários\n"))
            if(readOption == 1):
                n = input("Insira o endereço de email ou o numero da conta do usuário: ")
                readUser(dataList, n)
            elif(readOption == 2):
                readAllUser(dataList)
        case 3:
            n = int(input("Digite o numero da conta: "))
            print("Caso não queira alterar algum dado, mantenha o que estava anteriormente\n")
            newEmail = input("Insira o novo endereço de email: ")
            newName = input("Insira o novo nome: ")
            newPassword = input("Insira a nova senha: ")
            updateUser(dataList, n, newEmail, newName, newPassword)
        case 4:
            n = int(input("Digite o numero da conta: "))
            deleteUser(dataList, n)
        case 0:
            print("Saindo...")
            loop = False
            break
