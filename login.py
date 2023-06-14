import hashlib
import json
from cadastro import Usuario

def login_usuario():
    email = input("\nDigite o seu endereço de e-mail: ")
    senha = input("Digite a sua senha: ")

    senhaHash = hashlib.sha256(senha.encode()).hexdigest()

    def dictUsuario(d):
        return Usuario(**d)

    with open('registros.json', 'r') as arquivo:
        lista_json = arquivo.read()
        lista_dict = json.loads(lista_json)
        lista = list(map(dictUsuario, lista_dict))

        for cont in lista:
            if email == cont.login and senhaHash == cont.senha:
                print("\nlogin realizado!\n")
                return cont
        print("\nRegistro desconhecido\n")