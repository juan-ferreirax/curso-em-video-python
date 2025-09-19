red = "\033[31m"
white = "\033[37m"
green = "\033[32m"

def leiaInt(msg):
    while True:
        try:
            numI = int(input(msg))
            return numI
        except (ValueError, TypeError):
            print(f"{red}Informe um inteiro válido!", flush=True)

def leiaFloat(msg):
    while True:
        try:
            numR = input(msg)
            if numR.count(".") == 0 or numR.count(".") > 1 or numR[0] == "." or numR[-1] == ".":
                raise ValueError
            else:
                return float(numR)
        except (ValueError, TypeError):
            print(f"{red}Informe um real válido!", flush=True)