"""
Módulo de exemplo contendo funções matemáticas simples.
Este arquivo serve como uma biblioteca para ser importada por outros programas.
"""

def calcular_fatorial(n):
  """
  Calcula o fatorial de um número inteiro não negativo.
  """
  if not isinstance(n, int) or n < 0:
    return "Erro: O número deve ser um inteiro não negativo."
  elif n == 0:
    return 1
  else:
    resultado = 1
    for i in range(1, n + 1):
      resultado *= i
    return resultado

def calcular_dobro(n):
  """
  Calcula o dobro de um número.
  """
  return n * 2

def calcular_triplo(n):
  """
  Calcula o triplo de um número.
  """
  return n * 3

# O código abaixo só será executado se este arquivo for rodado diretamente,
# não quando for importado. É útil para testes rápidos do próprio módulo.
if __name__ == '__main__':
    print("Testando o módulo de cálculos...")
    num_teste_interno = 4
    print(f"Fatorial de {num_teste_interno} é {calcular_fatorial(num_teste_interno)}")
    print(f"Dobro de {num_teste_interno} é {calcular_dobro(num_teste_interno)}")
    print(f"Triplo de {num_teste_interno} é {calcular_triplo(num_teste_interno)}")