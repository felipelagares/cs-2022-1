class LoginInvalidoException(Exception):
    pass


class Login:

    def __init__(self):
        self.usuario = 'gilmar'
        self.senha = '12345'

    def Fazer_login(self, user, sen):
        try:
            if not (user == self.usuario and sen == self.senha):
                raise LoginInvalidoException
        except LoginInvalidoException:
            print('login invalido')
