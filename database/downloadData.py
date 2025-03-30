import os
# requests para requisição http
import requests
# zipfile para lidar com arquivos compactados
import zipfile


# diretorios de download dos arquivos csv
base_dir = os.path.join("database", "downloads")
demo_dir = os.path.join(base_dir, "demonstrativos_contabeis")
operadoras_dir = os.path.join(base_dir, "operadoras")

# criando diretorio
os.makedirs(demo_dir, exist_ok=True)
os.makedirs(operadoras_dir, exist_ok=True)

# url do relatorio cadop
operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"

# url dos demonstrativos contabeis de 23 e 24
demonstrativos_urls = [
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/1T2023.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/2T2023.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/3T2023.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/4T2023.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/1T2024.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/2T2024.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/3T2024.zip",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/4T2024.zip"
]

# funcao para baixar os arquivos
def download_file(url, dest_folder):
    # acessa o arquivo passado como parametro
    filename = os.path.join(dest_folder, os.path.basename(url))
    
    print(f"baixando {url} para: {filename}...")
    
    # faz a requisição de download
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            # baixando por 1024 bytes (ou 1kb) para evitar sobrecarga
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"download feito: {filename}")
    else:
        print(f"erro ao baixar: {url}")
    return filename

# baixar arquivo das operadoras
operadoras_file = download_file(operadoras_url, operadoras_dir)

# baixa os demonstrativos contabeis e joga para a lista
demo_files = []
for url in demonstrativos_urls:
    file_path = download_file(url, demo_dir)
    demo_files.append(file_path)

# extrai todos os arquivos zip na pasta dos demonstrativos
for zip_path in demo_files:
    # checa se o arquivo é compactado
    if zipfile.is_zipfile(zip_path):
    
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # cada arquivo do diretorio é extraido
            zip_ref.extractall(demo_dir) 
        print(f"extraido: {zip_path}")

        # assim que for extraido, remove o .zip inutilizado
        os.remove(zip_path)
        print(f"removido: {zip_path}")
    else:
        print(f"erro! arquivo {zip_path} não é um zip valido")

print("sucesso, todos os arquivos foram baixados!")
