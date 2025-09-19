def aumentar(valor, p=0, format=False):
    p /= 100
    valor += (valor * p)
    if format==False:
        return valor
    elif format==True:
        return f"R$ {valor:.2f}".replace(".", ",")

def diminuir(valor, p=0, format=False):
    p /= 100
    valor -= (valor * p)
    if format==False:
        return valor
    elif format==True:
        return f"R$ {valor:.2f}".replace(".", ",")

def dobro(valor, format=False):
    valor *= 2
    if format==False:
        return valor
    elif format==True:
        return f"R$ {valor:.2f}".replace(".", ",")

def metade(valor, format=False):
    valor /= 2
    if format==False: 
        return valor
    elif format==True:
        return f"R$ {valor:.2f}".replace(".", ",")

def moeda(function):
    return f"R$ {function:.2f}".replace(".", ",")

def resumo(valor, au=0, sub=0):
    print("-" * 32)
    print("RESUMO DO VALOR".center(32))
    print("-" * 32)
    print(f"Preço analisado:    {moeda(valor)}")
    print(f"Dobro do preço:     {dobro(valor, True)}")
    print(f"Metade do preço:    {metade(valor, True)}")
    print(f"{au}% de aumento:     {aumentar(valor, au, True)}")
    print(f"{sub}% de redução:     {diminuir(valor, sub, True)}")
    print("-" * 32)