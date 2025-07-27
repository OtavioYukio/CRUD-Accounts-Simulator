from entities.user import User

def createUser(list, email, name, password):
    numberAccount = User.numberAccountGenerator(list)
    verify = True
    for v in list:
        if(email == v['email']):
            verify = False
            print("Email ja está sendo utilizado")
    if (verify):
        newUser = User(email, name, password, numberAccount)
        list.append({
            'email': newUser.email,
            'name': newUser.name,
            'password': newUser.password,
            'numberAccount': newUser.numberAccount
        })
        print("Conta criada com sucesso")

def readAllUser(list):
    print(list)

def readUser(list, user):
    listedUser = False
    for v in list:
        if(user == v['email'] or user == str(v['numberAccount'])):
            print(v)
            listedUser = True
    if(not listedUser):
        print("Conta não encontrada")

def updateUser(list, numberAccount, newEmail, newName, newPassword):
    updatedAccount = False
    for v in list:
        if (v['numberAccount'] == numberAccount):
            v['email'] = newEmail
            v['name'] = newName
            v['password'] = newPassword
            updatedAccount = True
            print("Conta atualizada com sucesso")
    if (not updatedAccount):
        print("Conta não encontrada")

def deleteUser(list, numberAccount):
    deletedAccount = False
    for v in list:
        if (v['numberAccount'] == numberAccount):
            list.remove(v)
            deletedAccount = True
            print("Conta deletada com sucesso")
    if(not deletedAccount):
        print("Conta não encontrada")
    