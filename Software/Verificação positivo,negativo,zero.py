def verificar_se_positivo_negativo():
    numero = int(input("Digite um número: "))

    if numero > 0:
        print(f"{numero} é positivo.")
    elif numero < 0:
        print(f"{numero} é negativo.")
    else:
        print(f"{numero} é zero.")
    return ""

verificar_se_positivo_negativo()