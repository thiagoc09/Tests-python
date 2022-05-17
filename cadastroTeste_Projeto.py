import unittest
from cadastro_projeto import Cadastro

class Test(unittest.TestCase):
        def teste_cad_nome(self):
                nomeC=Cadastro()
                print("Digite o seu nome:")
                self.assertTrue(nomeC.cad_nome(input()))
                
        def teste_cad_sobrenome(self):
                sobrenomeC=Cadastro()
                print("Digite o seu sobrenome:")
                self.assertTrue(sobrenomeC.cad_sobrenome(input()))
                
        def teste_cad_cpf(self):
                cpfC=Cadastro()
                print("Digite o seu cpf:")
                self.assertTrue(cpfC.cad_cpf(input()))
        
        def teste_cad_dataNasc(self):
                dataNascC=Cadastro()
                print("Digite a data de nascimento(YYYY MM DD):")
                self.assertTrue(dataNascC.cad_dataNasc(int(input()),int(input()),int(input())))
        
        def teste_cad_username(self):
                users=Cadastro()
                print("Digite o seu username:")
                self.assertTrue(users.cad_user(input()))
                
        def teste_cad_pass(self):
                passC=Cadastro()
                print("Digite a senha:")
                self.assertTrue(passC.cad_password(input()))

if __name__ == '__main__':
    unittest.main()
        