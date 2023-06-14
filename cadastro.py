from dataclasses import dataclass,asdict
import json
import hashlib

lista=[] 

@dataclass
class Usuario:
    login: str
    senha: str
    
def cad_usuario():
    email = str(input("\nInsira seu e-mail: "))
    password = str(input("Insira sua senha: "))

    senhaHash = hashlib.sha256(password.encode()).hexdigest()

    usuario_obj = Usuario(login=email, senha= senhaHash)
    lista.append(usuario_obj)

    with open('registros.json', 'w') as arquivo:
        lista_dict = list(map(asdict, lista))
        lista_json = json.dumps(lista_dict, indent=4) 
        arquivo.write(lista_json)
        print("\nUsuário Registrado!\n")

    return usuario_obj
            
        
