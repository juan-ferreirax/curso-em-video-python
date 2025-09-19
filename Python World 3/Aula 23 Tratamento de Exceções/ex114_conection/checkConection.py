import socket
from ex114_conection import checkInput

def acess_domain(domain, port=8080):
    candy_socket = None
    try:
        candy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        candy_socket.settimeout(5)
        candy_socket.connect((domain, port))
        print(f"Acessando {domain}...")
        print(f"{checkInput.green}Conexão realizada com sucesso!")
    except ValueError:
        print("Informe um domínio válido!")
    except TimeoutError:
        #TimeoutError: [Errno 110] Connection timed out
        print(f"{checkInput.red}A conexão atingiu o tempo limite...")
        print(f"Verifique a porta {port} e tente novamente!")
    except ConnectionRefusedError:
        #ConnectionRefusedError: [Errno 111] Connection refused
        print(f"{checkInput.red}A conexão foi recusada pelo servidor.")
        print(f"Verifique se a porta {port} está correta e aberta no servidor.")
    except socket.gaierror as e:
        match e.errno:
            case -2:
                #[Errno -2] Name or service not known
                print(f"{checkInput.red}Problema na resolução do domínio {domain} informado...")
                print(f"Verifique a ortográfia e tente novamente!")
            case -3:
                #[Errno -3] Temporary failure in name resolution
                print(f"{checkInput.red}Falha temporária na resolução de nome...")
            case _:
                print(f"{checkInput.red}Problema na resolução de DNS")
                print("Verifique sua conexão e as configurações de DNS e tente novamente!")
    except OSError as e:
        # Captura outros erros de rede/SO, como 'No route to host'
        print(f"{checkInput.red}Ocorreu um erro inesperado de rede ou sistema: {e}")
    finally:
        if candy_socket:
            candy_socket.close()