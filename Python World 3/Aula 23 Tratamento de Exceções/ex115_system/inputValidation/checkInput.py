from dataFormatting.cor import red, reset

def leiaInt(msg):
    while True:
        try:
            numI = int(input(msg))
            return numI
        except (ValueError, TypeError):
            print(f"{red}Informe um inteiro válido!{reset}", flush=True)
        except KeyboardInterrupt:
            print(f"{red}O usuário preferiu não informar esse valor!{reset}", flush=True)
            return 0

def leiaFloat(msg):
    while True:
        try:
            numR = input(msg)
            if numR.count(".") == 0 or numR.count(".") > 1 or numR[0] == "." or numR[-1] == ".":
                raise ValueError
        except (ValueError, TypeError):
            print(f"{red}Informe um real válido!{reset}", flush=True)
        except KeyboardInterrupt:
            print(f"{red}O usuário preferiu não informar esse valor!{reset}", flush=True)
            return 0
        else:
            return float(numR)

def leiaString(msg):
    while True:
        try:
            nome = input(msg)
            if nome.isnumeric() or nome == "":
                raise ValueError
        except (ValueError, TypeError):
            print(f"{red}ERRO! Você deve usar apenas caracteres alfabeticos!{reset}", flush=True)
        except KeyboardInterrupt:
            print(f"{red}O usuário preferiu não informar esse valor!{reset}", flush=True)
            return "Desconhecido"
        else:
            return nome