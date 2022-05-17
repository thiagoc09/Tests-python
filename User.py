class User:
    def user_login(self,login):
        return login<=login[0:8]
        
    def user_senha(self,senha):
        return senha<=senha[0:6]
