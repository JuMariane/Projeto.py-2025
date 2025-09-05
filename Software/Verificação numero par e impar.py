def verificar_par_impar(numero):

  if numero % 2 == 0:
    return "par"
  else:
    return "ímpar"
try:
  numero_usuario = int(input("Digite um número inteiro para verificar: "))
  resultado_usuario = verificar_par_impar(numero_usuario)
  print(f"O número que você digitou é {resultado_usuario}.")
except ValueError:
  print("Entrada inválida. Por favor, digite um número inteiro.")