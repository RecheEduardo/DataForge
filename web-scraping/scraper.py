import requests
# lib de acesso aos dados do html do GOV
from bs4 import BeautifulSoup 

## primeira parte - acesso para a pagina do GOV

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(URL)

if response.status_code == 200: # 200 - solicitacao aconteceu
    soup = BeautifulSoup(response.text, "html.parser")
    print("Página acessada!")
else:
    print(f"ERRO! Não foi possivel acessar a página: {response.status_code}")
    exit() # encerra o script se nao tiver acesso


## segunda parte - buscar todos os links da pagina

pdf_links = []

# loop que busca todas as tags de link do html 
# e se tiver href de um pdf, adiciona o link no array
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.endswith(".pdf"):
        pdf_links.append(href)

# mostra na tela os links encontrados
print("links dos arquivos PDF encontrados: ", pdf_links)