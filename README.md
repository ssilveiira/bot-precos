# 📊 Projeto: Coletando Dados Web - Mercado Livre

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 1. Resumo do Projeto 🌐
Este projeto consiste no desenvolvimento de um bot de **Web Scraping** utilizando Python. O objetivo principal é automatizar o monitoramento de preços no Mercado Livre, simulando um navegador para extrair informações competitivas sem a necessidade de trabalho manual.

## 2. Tecnologias Utilizadas 🛠️
Para a construção desta ferramenta, foi escolhida a linguagem  **Python:** para o desenolvimento do projeto. Também foram utilizadas as bibliotecas: **Requests**, **BeautifulSoup (bs4)**,  **Pandas**.

## 3. Funcionalidades Técnicas
O script executa os seguintes passos lógicos:
1. **Conexão:** Acessa a URL de busca do Mercado Livre definindo um `User-Agent` para evitar bloqueios.
2. **Varredura:** Identifica todos os containers de produtos na primeira página de resultados.
3. **Extração:** Captura o Título (Descrição) e o Preço (Valor em Reais) de cada item.
4. **Tratamento:** Limpa caracteres indesejados e formata os dados.
5. **Persistência:** Salva o resultado final em um arquivo local (`.csv`).

---

## 4. Análise Prática (Resultados) 📝
Abaixo está uma demonstração do arquivo gerado pelo bot após uma execução de teste. A planilha contém os produtos encontrados e seus respectivos preços organizados.

![Exemplo da Planilha]()

---

