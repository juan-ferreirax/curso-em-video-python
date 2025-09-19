from time import sleep
from dataFormatting.cor import blue, green, red, reset, yellow

def mensagem(msg):
    print("-" * 50)
    print(f"{msg}".center(50))
    print("-" * 50)

def menu():
    while True:
        mensagem("MENU PRINCIPAL")
        print(f"{yellow}1 - " + f"{blue}Ver pessoas cadastradas", flush=True)
        print(f"{yellow}2 - " + f"{blue}Cadastrar nova pessoa", flush=True)
        print(f"{yellow}3 - " + f"{blue}Sair do sistema", flush=True)
        print(f"{reset}-" * 50, flush=True)
        try:
            op = int(input(f"{yellow}Escolha uma opção: {reset}"))
            match op:
                case 1:
                    verCadastros()
                    sleep(0.5)
                case 2:
                    cadastro()
                    sleep(0.5)
                case 3:
                    print(f"{green}PROGRAMA FINALIZADO COM SUCESSO!")
                    break
                case _:
                    print(f"{red}ERRO!Informe uma opção válida!{reset}")
        except (ValueError, TypeError):
            print(f"{red}ERRO!Informe uma opção válida!{reset}")
        except KeyboardInterrupt:
            print(f"{red}O usuário preferiu não informar esse valor!{reset}", flush=True)
            break

pessoa = {}
pessoas_cadastradas = []
def cadastro():
    mensagem("NOVO CADASTRO")
    from inputValidation.checkInput import leiaString, leiaInt
    pessoa["Nome"] = leiaString("Informe o seu nome: ")
    pessoa["Idade"] = leiaInt("Informe a sua idade: ")
    with open("Cadastros.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pessoa["Nome"]:<25}" + f"{pessoa["Idade"]:>14} anos\n")
    print(f"{green}CADASTRO REALIZADO COM SUCESSO!{reset}")
    sleep(0.5)

def verCadastros():
    mensagem("PESSOAS CADASTRADAS")
    try:
        with open("Cadastros.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print(f"{yellow}Nenhuma pessoa foi cadastrada até o momento!{reset}")
    sleep(0.5)