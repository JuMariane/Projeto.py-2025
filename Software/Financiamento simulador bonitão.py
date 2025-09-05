# Ex 2 – Python Code - Tkinter Library

import tkinter as tk
from tkinter import messagebox

def calcular_financiamento():
    try:
        valor_carro = float(entry_valor_carro.get())
        entrada = float(entry_entrada.get())
        taxa_juros_mensal = float(entry_juros.get())
        meses = int(entry_meses.get())

        if entrada > valor_carro:
            messagebox.showerror("Erro", "A entrada não pode ser maior que o valor do carro.")
            return

        valor_financiado = valor_carro - entrada
        i = taxa_juros_mensal / 100
        if i == 0:
            prestacao = valor_financiado / meses
        else:
            prestacao = valor_financiado * (i * (1 + i) * meses) / ((1 + i) * meses - 1)

        total_pago = prestacao * meses
        juros_total = total_pago - valor_financiado

        resultado.set(
            f"Valor financiado: R$ {valor_financiado:.2f}\n"
            f"Prestação mensal: R$ {prestacao:.2f}\n"
            f"Total pago: R$ {total_pago:.2f}\n"
            f"Total de juros: R$ {juros_total:.2f}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

janela = tk.Tk()
janela.title("Simulador de Financiamento de Carro")
janela.geometry("400x400")
janela.resizable(False, False)

tk.Label(janela, text="Simulador de Financiamento", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(janela)
frame.pack(pady=5)

tk.Label(frame, text="Valor do carro (R$):").grid(row=0, column=0, sticky="w")
entry_valor_carro = tk.Entry(frame)
entry_valor_carro.grid(row=0, column=1)
tk.Label(frame, text="Entrada (R$):").grid(row=1, column=0, sticky="w")
entry_entrada = tk.Entry(frame)
entry_entrada.grid(row=1, column=1)

tk.Label(frame, text="Juros mensais (%):").grid(row=2, column=0, sticky="w")
entry_juros = tk.Entry(frame)
entry_juros.grid(row=2, column=1)

tk.Label(frame, text="Prazo (meses):").grid(row=3, column=0, sticky="w")
entry_meses = tk.Entry(frame)
entry_meses.grid(row=3, column=1)

tk.Button(janela, text="Calcular", command=calcular_financiamento, bg="green", fg="white", font=("Arial", 12)).pack(pady=15)

resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado, justify="left", font=("Arial", 12))
label_resultado.pack(pady=10)

janela.mainloop()