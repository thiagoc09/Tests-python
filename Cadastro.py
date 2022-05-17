from datetime import date
import re

class Cadastro:

    def cad_genero(self, genero):
        if genero =="M" or genero=="F" or genero=="O":
            return True
        else:
            return False

    def cad_nome(self,nome):
        if nome == re.sub('[0-9]','',nome):
            return True
        else:
            return False 
    def cad_cpf(self,cpf):
        cpf=[int(char)for char in cpf if char.isdigit()]
        if len(cpf)!=11:
            return False
        if cpf ==cpf[::-1]:
            return False

        for i in range(9,11):
            valor=sum((cpf[num]*((i+1)-num) for num in range (0,i))) #realizar o calculo de validação do ((primeiro digito)) 
            #e quando terminar vai rodar a verificação do (((segundo)))
            validar=((valor*10)%11)%10 #variável de validação do ((primeiro)) e do segundo
            if validar!=cpf[i]: #if de validação do cpf, então se o numero não existir dentro do cpf ele é falso, agora senão ele é verdadeiro 
                return print("Não foi possível")
            else:
                return print("Validado com sucesso")
   
    def cad_dataNasc(self,ano,mes,dia):
        dataNasc=date(ano,mes,dia)
        anoN=dataNasc.year
        mesN=dataNasc.month
        diaN=dataNasc.day
        print(f"Data de nascimento:{diaN}-{mesN}-{anoN}")
        if mes>=13 or 1950>ano<2022  or dia>31:
            return False + print("Não foi possível")
        else:
            return True

#Salvar como Cadastro.py
