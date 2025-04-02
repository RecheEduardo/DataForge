<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Century+Gothic&weight=800&size=48&pause=1000&color=F7F7F7&center=true&vCenter=true&width=435&lines=Data+Forge" alt="Typing SVG" />  
</p>

---

<h1 align="center">🚀 Plataforma Integrada de Dados de Saúde do GOV</h1>

# 1. Sobre o Projeto 📊

O projeto do **DataForge** é uma solução completa para a manipulação e análise de dados na área da saúde, integrando diversas tecnologias para oferecer funcionalidades que vão desde a extração e transformação de dados até o fornecimento de uma API REST e uma interface interativa.

O projeto é dividido em quatro grandes etapas:

- **Web Scraping:** Realiza a extração de PDFs (Anexos I e II) do site do GOV.
- **Transformação de Dados:** Utiliza os PDFs para extrair e transformar tabelas em arquivos CSV.
- **Banco de Dados:** Estrutura e importa os dados dos demonstrativos contábeis e dos cadastros das operadoras para um banco de dados, além de executar consultas analíticas.
- **API & Frontend:** Disponibiliza uma API em Flask para buscas nos cadastros das operadoras e um frontend em Vue.js para interação do usuário.

---

# 2. Funcionalidades 🛠️

- **Web Scraping:**  
  - Acessa a página do GOV e baixa os PDFs dos Anexos I e II.
  - Compacta os arquivos baixados em um arquivo ZIP.
  
- **Transformação de Dados:**  
  - Extrai tabelas do PDF do Anexo I com **pdfplumber**.
  - Substitui abreviações por descrições completas (ex.: "OD" por "Seg. Odontológica").
  - Gera um arquivo CSV estruturado com os dados processados.

- **Banco de Dados:**  
  - Organiza os dados dos demonstrativos contábeis e dos cadastros das operadoras em CSVs.
  - Utiliza scripts SQL para criar tabelas, importar os dados e realizar consultas analíticas, como:
    - Identificar as 10 operadoras com maiores despesas em sinistros médico-hospitalares no último trimestre.
    - Identificar as 10 operadoras com maiores despesas na mesma categoria no último ano.

- **API de Busca:**  
  - Disponibiliza endpoints para busca por **Modalidade**, **UF** e **Representante**.
  - Retorna respostas em JSON para integração com outros sistemas e frontend.

- **Frontend Interativo:**  
  - Desenvolvido com **Vue.js**, permite que o usuário realize buscas de forma dinâmica e exiba os resultados em uma tabela.

- **Testes e Automação:**  
  - Coleção Postman para testar os endpoints da API.
  - Script automatizado para download e extração dos arquivos de dados.

---

# 3. Estrutura do Projeto 📁

```plaintext
IntuitiveCare_Tests/
├─ api/
│  ├─ frontend/               # Interface em Vue.js
│  │  ├─ src/
│  │  │  ├─ components/       # Componentes Vue (ex.: Navbar, Search)
│  │  │  ├─ App.vue
│  │  │  └─ main.ts
│  │  ├─ index.html
│  │  └─ outros arquivos de configuração
│  └─ server/                 # Servidor Flask (API)
│     └─ server.py
├─ data-transformation/       # Scripts de transformação de dados
│  ├─ downloads/              # Arquivo compactado do CSV transformado
│  ├─ output/                 # CSV final: dados_transformados.csv
│  └─ transformData.py
├─ database/                  # Scripts e dados para o BD
│  ├─ downloads/
│  │  ├─ demonstrativos_contabeis/  # CSVs dos demonstrativos contábeis (1T2023.csv, 2T2023.csv, etc.)
│  │  └─ operadoras/                 # Relatorio_cadop.csv
│  ├─ scripts/                # Scripts SQL:
│  │  ├─ criar_tabelas.sql
│  │  ├─ importar_dados.sql
│  │  └─ consulta_analitica.sql
│  └─ downloadData.py         # Script para download e extração dos dados do BD
├─ postman/                   # Coleção e ambiente do Postman para teste da API
│  └─ API_Operadoras.postman_collection.json
└─ web-scraping/             # Scripts de Web Scraping
   ├─ downloads/             # PDFs baixados dos Anexos I e II
   ├─ anexos.zip             # Arquivo ZIP com os PDFs
   └─ scraper.py
```

# 4. 📝 Executar a API (Flask)

## Introdução

1. A API permite acessar o arquivo CSV de cadastro das operadoras da base de dados do GOV e retornar os valores conforme parâmetro de busca e rota desejada (Modalidade, UF e Representante).
    
2. Caso tenha interesse em consultar o arquivo base, o download do mesmo se encontra em: [Base de Dados GOV](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv)
    
3. A API é executada localmente (utilizando localhost) e responde a requisição em formato JSON.
    

## Endereço Base

```
http://localhost:5000

 ```

## Instalação e Execução

### 1\. Clone este repositório - [Link](https://github.com/RecheEduardo/DataForge)

### 2\. Requisitos de Sistema

- Python 3.x instalado
    
- Biblioteca Flask e Flask-CORS (API) instaladas
    
- Biblioteca Pandas, Requests, BeatifulSoup e PDFplumber instaladas ( Data Scraping e Downloads )
    

### 3\. Instalação das Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```
pip install flask flask-cors pandas requests beautifulsoup4 pdfplumber

 ```

### 4\. Execução dos Scripts de Python

Execute o seguinte script em DataForge/database/downloadData.py para instalar as planilhas necessárias:

``` python
py downloadData.py

 ```

### 5\. Estrutura do Projeto base onde a API é consumida

```
DataForge/
├─ api/
│  ├─ frontend/
│  ├─ server/
│  │  └─ server.py
├─ database/
│  ├─ downloads/
│  │  └─ operadoras/
│  │     └─ Relatorio_cadop.csv
│  ├─ scripts/
│  └─ downloadData.py
└─ .gitignore

 ```

### 6\. Executando o Servidor

Para iniciar o servidor Flask, execute o seguinte comando no diretório `server/`:

```
python server.py

 ```

O servidor será iniciado em `http://localhost:5000`.

## Rotas Disponíveis

### 1\. Buscar por Modalidade

**Endpoint:**

```
GET /searchModalidade?query=<nome_da_modalidade>

 ```

**Parâmetro:**

- `query`: Nome parcial ou completo da modalidade desejada.
    

**Exemplo de Requisição:**

```
GET http://localhost:5000/searchModalidade?query=Medicina

 ```

**Resposta:**

``` json
[
    {
        "CNPJ": "12345678901234",
        "Nome": "Operadora Exemplo",
        "Modalidade": "Medicina de Grupo",
        "UF": "SP",
        "Representante": "João Silva"
    }
]

 ```

### 2\. Buscar por UF

**Endpoint:**

```
GET /searchUF?query=<sigla_da_UF>

 ```

**Parâmetro:**

- `query`: Sigla do estado (UF) desejado.
    

**Exemplo de Requisição:**

```
GET http://localhost:5000/searchUF?query=SP

 ```

**Resposta:**

``` json
[
    {
        "CNPJ": "12345678901234",
        "Nome": "Operadora Exemplo",
        "Modalidade": "Medicina de Grupo",
        "UF": "SP",
        "Representante": "João Silva"
    }
]

 ```

### 3\. Buscar por Representante

**Endpoint:**

```
GET /searchRepresentante?query=<nome_do_representante>

 ```

**Parâmetro:**

- `query`: Nome parcial ou completo do representante.
    

**Exemplo de Requisição:**

```
GET http://localhost:5000/searchRepresentante?query=Joao

 ```

**Resposta:**

``` json
[
    {
        "CNPJ": "12345678901234",
        "Nome": "Operadora Exemplo",
        "Modalidade": "Medicina de Grupo",
        "UF": "SP",
        "Representante": "João Silva"
    }
]

 ```

### Considerações da API

- Os valores `NaN` no CSV são substituídos por strings vazias (`""`) na resposta JSON.
    
- A pesquisa é **case-insensitive (porém considera acentos em nomes, por exemplo)**.
    
- Caso não sejam encontrados resultados para a consulta, a API retorna uma lista vazia `[]`.

---

# 🚀 Tecnologias Utilizadas

<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white" height="35"  />

A linguagem de consulta principal utilizada no projeto. SQL (Structured Query Language) é uma linguagem padrão para gerenciar e manipular bancos de dados relacionais. Com SQL, é possível realizar operações como inserir, consultar, atualizar e excluir dados, além de definir estruturas de tabelas e relacionamentos. Sua sintaxe é robusta e eficiente, permitindo a realização de operações complexas de maneira clara e concisa.

##

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="35"  />

A linguagem de programação principal utilizada no projeto. Python é uma linguagem de alto nível, versátil e de fácil leitura, muito utilizada em diversas áreas como desenvolvimento web, automação e análise de dados. Sua sintaxe simples e rica em bibliotecas permite um desenvolvimento rápido e eficiente, além de ser uma das preferidas para projetos de ciência de dados e aprendizado de máquina.

##

<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" height="35"  />

Framework micro utilizado para estruturar a aplicação. Flask é um framework web minimalista para Python que fornece os componentes essenciais para desenvolver aplicações web, permitindo flexibilidade na escolha de bibliotecas e ferramentas. Com sua simplicidade e extensibilidade, Flask é ideal para projetos de pequeno a médio porte, oferecendo controle total sobre a arquitetura da aplicação.

##

<img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white" height="35"  />

Framework JavaScript progressivo utilizado para criar interfaces de usuário dinâmicas. Vue.js é projetado para ser adaptável e fácil de integrar com outras bibliotecas ou projetos existentes. Ele facilita o desenvolvimento de interfaces interativas, com foco na reatividade dos dados e na organização do código, tornando o processo de desenvolvimento mais ágil e a manutenção da aplicação mais eficiente.

##

<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" height="35"  />

Framework CSS utilizado para estilizar e tornar a interface da aplicação mais agradável e responsiva. O Bootstrap facilita o design da aplicação, proporcionando uma interface limpa e consistente em dispositivos móveis e desktop sem a necessidade de criar CSS do zero. Ele inclui componentes como botões, formulários, modais e grids, que são amplamente utilizados para garantir uma experiência de usuário rica e adaptável.

##

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" height="35"  />

Linguagem de programação usada para adicionar tipagem estática ao JavaScript. TypeScript melhora a qualidade e a escalabilidade do código, proporcionando verificação de tipos durante o desenvolvimento e facilitando a manutenção de grandes aplicações. Ele é amplamente adotado em projetos de frontend modernos, oferecendo uma sintaxe robusta e compatibilidade com bibliotecas e frameworks populares como React e Vue.js.

##

<img src="https://img.shields.io/badge/Postman-FF6C37.svg?style=for-the-badge&logo=Postman&logoColor=white" height="35" />

<p>Postman é uma ferramenta popular para testar e documentar APIs. Ele permite que desenvolvedores enviem requisições HTTP, analisem respostas, e automatizem testes de integração com facilidade. Com uma interface intuitiva, o Postman também oferece recursos como coleções, variáveis e ambientes, ajudando a organizar e otimizar o fluxo de desenvolvimento de APIs.</p>
