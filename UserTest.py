import unittest
from User import User

class TestClass(unittest.TestCase):
    def teste_user_login(self):
        login=User()
        print("Digite o login de usuário:")
        self.assertTrue(login.user_login(input()))
        
    def teste_user_senha(self):
        senha=User()
        print("\nDigite a senha:")
        self.assertTrue(senha.user_senha(input()))
if __name__=="__main__":
    unittest.main()

#salvar como UserTest.py


