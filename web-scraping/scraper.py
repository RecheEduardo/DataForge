import os
# lib para requisições HTTP
import requests
# lib de acesso aos dados do html do GOV
from bs4 import BeautifulSoup
# lib para operar arquivos, será utilizada para compactação
import shutil


## (1) primeira parte - acesso para a pagina do GOV

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(URL)

if response.status_code == 200: # 200 - solicitacao aconteceu
    soup = BeautifulSoup(response.text, "html.parser")
    print("Página acessada!")
else:
    print(f"ERRO! Não foi possivel acessar a página: {response.status_code}")
    exit() # encerra o script se nao tiver acesso


## (2) segunda parte - buscar todos os links da pagina

pdf_links = []
anex_names = ("Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf")

# loop que busca todas as tags de link do html 
# e se tiver href de um pdf, adiciona o link no array
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.endswith(anex_names):
        pdf_links.append(href)

# mostra na tela os links encontrados
print("links dos arquivos PDF encontrados: ", pdf_links)


## (3) terceira parte - baixar os pdfs encontrados

# cria a pasta 'downloads' caso nao exista
os.makedirs("downloads", exist_ok=True)

# loop que percorre o array de links dos arquivos pdf
for pdf_url in pdf_links:
    if pdf_url.startswith("/"):                     # se o link for relativo ao dominio do GOV 
        pdf_url = "https://www.gov.br" + pdf_url    # o if transforma ele em um link completo
    
    # cria o arquivo dentro de downloads
    file_name = os.path.join("downloads", pdf_url.split("/")[-1])
    # a url é parseada e pega o nome após o ultimo '/' ou seja, o nome do arquivo PDF no site

    pdf_response = requests.get(pdf_url) # realiza o método GET para baixar cada PDF da pagina

    if pdf_response.status_code == 200: # 200 - download aconteceu
        with open(file_name, "wb") as pdf_file:
            # abre o arquivo criado e grava o conteudo do PDF baixado
            pdf_file.write(pdf_response.content)

        print(f"Arquivo baixado! -> {file_name}")
    else:
        print(f"ERRO! Não foi possível baixar {pdf_url}")

# uso da lib shutil para zipar os arquivos pdf baixados do GOV
shutil.make_archive("anexos", 'zip', "downloads")

print("seus arquivos foram compactados em: downloads/anexos.zip!")