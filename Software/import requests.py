import requests

cep = input("Digite o CEP: ")
cep = ''.join(filter(str.isdigit, cep))  # Só números

print("Escolha o que quer ver:")
print("0 - Estado")
print("1 - Rua")
print("2 - Cidade") 
print("3 - Tudo")
op = input("Digite um número: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if "erro" in data:
            print("CEP não encontrado.")
        else:
            if op == "0":
                print("Estado:", data.get("uf", "N/A"))
            elif op == "1":
                print("Rua:", data.get("logradouro", "N/A"))
            elif op == "2":
                print("Cidade:", data.get("localidade", "N/A"))
            elif op == "3":
                print(data)
            else:
                print("Opção inválida.")
    else:
        print("Erro ao consultar CEP.")
except Exception as e:
    print("Erro:", e)