import os
import tkinter as tk

# Caminho do arquivo
pasta = "C:\\Python"
arquivo = os.path.join(pasta, "exemplo_tkinter.txt")

mensagens = []

# 1. Criar pasta se não existir
if not os.path.exists(pasta):
    os.makedirs(pasta)
    mensagens.append(f"Pasta criada em: {pasta}")
else:
    mensagens.append(f"Pasta já existia em: {pasta}")

# 2. Criar arquivo e escrever conteúdo
f = open(arquivo, "w")
f.write("Linha 1: Arquivo criado com Tkinter.\n")
f.write("Linha 2: Aprendendo Python com interface gráfica.\n")
f.close()
mensagens.append("Arquivo criado e conteúdo inicial escrito.")

# 3. Adicionar nova linha
f = open(arquivo, "a")
f.write("Linha 3: Conteúdo adicionado depois.\n")
f.close()
mensagens.append("Linha adicionada ao arquivo.")

# 4. Ler o conteúdo do arquivo
f = open(arquivo, "r")
conteudo = f.read()
f.close()
mensagens.append("Arquivo lido com sucesso.")

# 5. Obter tamanho do arquivo
tamanho = os.path.getsize(arquivo)
mensagens.append(f"Tamanho do arquivo: {tamanho} bytes")
mensagens.append(f"Caminho completo do arquivo: {arquivo}")

# 6. Criar janela com tkinter
janela = tk.Tk()
janela.title("Manipulação de Arquivos em Python")
janela.geometry("600x400")

# Título
titulo = tk.Label(janela, text="Resultado da Manipulação de Arquivo", font=("Arial", 14))
titulo.pack(pady=10)

# Caixa de texto para exibir informações
caixa_texto = tk.Text(janela, wrap=tk.WORD, font=("Courier New", 10))
caixa_texto.pack(expand=True, fill="both", padx=10, pady=10)

# Inserir mensagens e conteúdo do arquivo na caixa de texto
caixa_texto.insert("1.0", "\n".join(mensagens) + "\n\nConteúdo do Arquivo:\n" + conteudo)
caixa_texto.config(state="disabled")  # deixar como somente leitura

# Executar janela
janela.mainloop()