class NumeroImparException(Exception):
    def __init__(self, numero):
        super().__init__(f"Erro: O número {numero} é ímpar. Digite apenas números pares.")
def verificar_numero_par():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 != 0:
            raise NumeroImparException(numero)
        print(f"O número {numero} é par.")
    except NumeroImparException as e:
        print(e)
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
verificar_numero_par()
