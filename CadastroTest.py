import unittest
from Cadastro import Cadastro
class CadastroTest(unittest.TestCase):

    def teste_cad_nome(self):
        nome=Cadastro()
        print("\nDigite o seu nome:")
        self.assertTrue(nome.cad_nome(input()))
    
    def teste_cad_cpf(self):
        cpf=Cadastro()
        print("\nDigite o seu cpf: pode ser com ou sem pontuação")
        self.assertTrue(cpf.cad_cpf(input()))

    def teste_cad_dataNasc(self):
        dataNasc=Cadastro()
        print("\nDigite sua data de nascimento de acordo com o formato: (YYYY MM DD):")
        self.assertTrue(dataNasc.cad_dataNasc(int(input()),int(input()),int(input())))

    def teste_cad_genero(self):
        genero=Cadastro()
        print("\nDigite o seu genêro: M, F or O")
        self.assertTrue(genero.cad_genero(input().upper()))

if __name__=="__main__":
    unittest.main()

#salvar como CadastroTest.py