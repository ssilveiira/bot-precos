import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Configurações Iniciais
url = "https://lista.mercadolivre.com.br/iphone"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("1. Acessando o Mercado Livre...")
resposta = requests.get(url, headers=headers)


site = BeautifulSoup(resposta.text, 'html.parser')

print("2. Procurando produtos...")

# Pegando os Títulos e usando a classe 
titulos = site.find_all(class_='poly-component__title')

# Pegando os Preços (usando a classe padrão nova)
precos = site.find_all(class_='poly-price__current')

# Lista para guardar os dados
dados = []

# pegando o menor tamanho entre as duas listas para não dar erro
quantidade = min(len(titulos), len(precos))

print(f"3. Encontrei {quantidade} produtos. Organizando...")

for i in range(quantidade):
    nome_produto = titulos[i].text
    preco_produto = precos[i].text
    
    # Adiciona na lista
    dados.append([nome_produto, preco_produto])

# Criando o Excel (CSV)
df = pd.DataFrame(dados, columns=['Nome do Produto', 'Preço'])
df.to_csv('meu_primeiro_bot.csv', index=False, encoding='utf-8-sig')

print("-" * 30)
print("SUCESSO! 🚀")
print("O arquivo 'meu_primeiro_bot.csv' foi criado na sua pasta.")
print("-" * 30) 