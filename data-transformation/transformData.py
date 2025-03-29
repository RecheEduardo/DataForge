import os
# lib pdfplumber para pegar info de arquivos PDF
import pdfplumber
# pandas para manipulacao e analise de dados
import pandas as pd
# shutil para operar arquivos, será utilizada para compactação
import shutil


# (1) primeira parte - extração dos dados das tabelas do anexo I

data = [] # lista que vai receber os dados

# caminho para o diretorio do anexo I
pdf_file_path = "../web-scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# abre o anexo I salvo no scraper
with pdfplumber.open(pdf_file_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table() # procura uma estrutura de tabela na página do pdf
        if table:
            for row in table:
                # substitui quebras de linha ("\n") por espaços em celulas que são strings.
                row = [cell.replace("\n", " ") if isinstance(cell, str) else cell for cell in row]
                # adiciona a linha para a lista de dados
                data.append(row)


# (2) segunda parte - substituiçao das abreviaçoes da tabela

# primeira linha como cabeçalho
header = data[0]  

# remove a primeira linha dos dados para evitar duplicação do cabeçalho
data = data[1:]  

abreviacoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
    "HCO": "Seg. Hospitalar Com Obstetrícia",
    "HSO": "Seg. Hospitalar Sem Obstetrícia",
    "REF": "Plano Referência",
    "PAC": "Procedimento de Alta Complexidade",
    "DUT": "Diretriz de Utilização"
}

# substitui as abreviações no header
header = [abreviacoes.get(col, col) for col in header]

for row in data:
    for i, cell in enumerate(row):
        # para cada celula das linhas da tabela
        # se o dado for igual a abreviação, sera substituido
        if cell in abreviacoes:
            row[i] = abreviacoes[cell]


# (3) terceira parte - salvar os dados obtidos em um arquivo csv

os.makedirs("output", exist_ok=True) # cria o diretorio para salvar o csv
csv_file = os.path.join("output", "dados_transformados.csv")

# usando o DataFrame do pandas para extrair um csv da lista de dados
df = pd.DataFrame(data, columns=header)  # utiliza o header para definir os cabecalhos do csv
df.to_csv(csv_file, index=False, encoding="utf-8")
# index=false remove existência de possíveis índices

print(f"Dados salvos em {csv_file}")


# (4) quarta parte - salva a planilha csv num arquivo compactado

os.makedirs("downloads", exist_ok=True) # cria o diretorio para zipar o arquivo
zip_name = os.path.join("downloads", "Teste_EduardoReche")

# grava o csv num arquivo .zip
shutil.make_archive(zip_name, "zip", "output", "dados_transformados.csv")

print("Arquivo compactado em: 'Teste_EduardoReche.zip'")