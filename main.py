from cadastro import cad_usuario
from login import login_usuario


while True:
    print("Bem Vindo!")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Sair")
    resp = int(input("Digite a opção desejada: "))


    if resp == 1:
        cad_usuario()
    elif resp == 2:
        login_usuario()

    elif resp == 3:
        print("\nAté a próxima...")
        break
    else:
        print("\nresposta inválida.")
    
