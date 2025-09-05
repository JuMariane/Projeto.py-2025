#Função para calcular
def calcular_financiamento():
    print("===== Simulador de Financiamento de Carro =====\n")

    #definição calculos
    valor_carro = float(input("Informe o valor total do carro (R$): "))
    entrada = float(input("Informe o valor da entrada (R$): "))
    taxa_juros_mensal = float(input("Informe a taxa de juros mensal (%): "))
    meses = int(input("Informe o número de parcelas (meses): "))

    valor_financiado = valor_carro - entrada

    i = taxa_juros_mensal / 100
    
    #calcular definição de calculos
    # PMT = P * [i * (1 + i)^n] / [(1 + i)^n - 1]
    if i == 0:
       prestacao = valor_financiado / meses
    else:
       prestacao = valor_financiado * (i * (1 + i) ** meses) / ((1 + i) ** meses - 1)

    total_pago = prestacao * meses

    juros_total = total_pago - valor_financiado

    #saida de dados, 2f significa dois digitos casa decimais no financiamento
    print("\n===== Resultado da Simulação =====")
    print(f"Valor do carro: R$ {valor_carro:.2f}")
    print(f"Entrada: R$ {entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Prazo: {meses} meses")
    print(f"Taxa de juros mensal: {taxa_juros_mensal:.2f}%")
    print(f"Prestação mensal: R$ {prestacao:.2f}")
    print(f"Total pago ao final: R$ {total_pago:.2f}")
    print(f"Total de juros pagos: R$ {juros_total:.2f}")
    print("===================================")

def aplic__juros(valor, porcentual):
   juros = valor * porcentual
#chamando a execução da função def
calcular_financiamento()