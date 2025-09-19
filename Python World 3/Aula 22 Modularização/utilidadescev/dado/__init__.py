def leiaDinheiro(msg):
    while True:
        #substitui o primeiro pela segundo
        valor = input(msg).replace(",", ".").strip()
        #Verifica se a condição é favorável para conversão de String para float
        if valor.count(".") <= 1 and valor.replace(".", "").isdigit():
            valor = float(valor)
            break
        else:
            print("ERRO! Digite um valor válido!")
    return valor

# substitui , por .
# verifica se tem 1 . ou nenhum, se tiver tira ele, e em seguida verifica se a str.isdigit() == True
# se sim, converte o original pra float
# se não exibe o erro