try:
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        raise Exception("Erro: Não é possível dividir por zero.")
    resultado = 10 / numero
    print("O resultado da divisão é:", resultado)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
except Exception as e:
    print(e)
