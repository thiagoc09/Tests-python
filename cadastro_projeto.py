from datetime import date
import re

class Cadastro:
    def cad_nome(self,nome):
        if nome==re.sub('[0-9]','',nome):
            print("Nome validado com sucesso!")
            return True
        else:
            print("Nome invalido!")
            return False
    def cad_sobrenome(self,sobrenome):
        if sobrenome==re.sub('[0-9]','',sobrenome):
            print("Sobrenome validado com sucesso!")
            return True
        else:
            print("Sobrenome invalido!")
            return False
    def cad_cpf(self,cpf):
        cpf=[int(char)for char in cpf if char.isdigit()]
        if len(cpf)!=11:
            return False
        if (cpf==cpf[::-1]):
            return False
        for i in range(9,11):
            valor=sum((cpf[num]*((i+1)-num) for num in range (0,i)))            
            validar=((valor*10)%11)%10
            if validar!=cpf[i]:
                print("CPF invalido!")
                return False
            else:
                print("CPF validado!")
                return True
    def cad_dataNasc(self,ano,mes,dia):
        dataNasc=date(ano,mes,dia)
        anoN=dataNasc.year
        mesN=dataNasc.month
        diaN=dataNasc.day
        print(f"Data de nascimento:{diaN}/{mesN}/{anoN}")
        if mes>=13 or ano>=2012 or dia>31:
            print("Data de nascimento invalido!")
            return False 
        else:
            print("Data de nascimento validado!")
            return True
        
    def cad_user(self,username):
        if(username<=username[0:8]):
            print("Usuário validado!")
            return True
        else:
            print("Usuário invalido!")
            return False
        
    def cad_password(self,password):
        l, u, p, d = 0, 0, 0, 0
        if (len(password) >= 8):    
            for i in password: 
                if (i.islower()): 
                    l+=1            
                if (i.isupper()): 
                    u+=1            
                if (i.isdigit()): 
                    d+=1            
                if(i=='@'or i=='$' or i=='_'): 
                    p+=1           
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)): 
                    print("Valid Password") 
                    return True
            else:
                return False