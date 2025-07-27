import random

class User:
    def __init__(self, email, name, password, numberAccount):
        self.email = email
        self.name = name
        self.password = password
        self.numberAccount = numberAccount
    @staticmethod
    def numberAccountGenerator(list):
        generatorController = False
        while(not generatorController):
            n = random.randint(100000, 999999)
            verifyNumberAccount = True
            for v in list:
                if(n == v['numberAccount']):
                    verifyNumberAccount = False
            if(verifyNumberAccount):
                return n