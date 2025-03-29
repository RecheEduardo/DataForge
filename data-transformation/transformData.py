# lib pdfplumber para pegar info de arquivos PDF
import pdfplumber


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