# flask utilizado para criar as rotas do servidor de busca
from flask import Flask, request, jsonify

from flask_cors import CORS

# pandas para analisar os dados do csv e retorná-los via api
import pandas as pd

# cria a aplicacao flask
app = Flask(__name__)

# Adicione o CORS para permitir requisições de qualquer origem
CORS(app)

# carrega os dados do csv para um dataframe do pandas
# transformando o arquivo em uma tabela dentro do python
data = pd.read_csv('../../database/downloads/operadoras/Relatorio_cadop.csv', encoding='utf-8', delimiter=';')

# cria uma rota chamada /search que responde a requisiçoes GET
@app.route('/searchModalidade', methods=['GET'])
def search_modalidade():
    # tratamento de dados - pega o que foi passado na url como query e remove espaços
    query = request.args.get('query', '').strip()
    
    # verifica se foi passado alguma coisa na query
    if query:
        # filtra os dados buscando na coluna 'Modalidade' todas as linhas que contem a query
        
        filtered = data[data['Modalidade'].str.contains(query, case=False, na=False)]
        # case=False - desabilita o case sensitive
        # na=False   - evita erro caso tenha valores nulos na coluna
        
        # transforma os dados filtrados em uma lista de dicionarios
        records = filtered.to_dict(orient='records')

        # tratamento de dados: 
        # itera sobre os registros e substitui cada valor NaN por uma string vazia('')
        cleaned_records = [
            { key: ('' if pd.isna(value) else value) for key, value in record.items() }
            for record in records
        ]
        
        # pega a lista de dicionario e retorna convertendo pro formato json
        return jsonify(cleaned_records)
    
    # se nao tiver query nenhuma, retorna lista vazia
    return jsonify([])

# mesma lógica para outras categorias de pesquisa: UF e Região

@app.route('/searchUF', methods=['GET'])
def search_UF():
    # tratamento de dados - pega o que foi passado na url como query e remove espaços
    query = request.args.get('query', '').strip()
    
    # verifica se foi passado alguma coisa na query
    if query:
        # filtra os dados buscando na coluna 'UF' todas as linhas que contem a query
        filtered = data[data['UF'].str.contains(query, case=False, na=False)]

        records = filtered.to_dict(orient='records')

        cleaned_records = [ # limpeza de NaN para ''
            { key: ('' if pd.isna(value) else value) for key, value in record.items() }
            for record in records
        ]
        
        # pega a lista de dicionario e retorna convertendo pro formato json
        return jsonify(cleaned_records)
    
    return jsonify([])

@app.route('/searchRegiao', methods=['GET'])
def search_Regiao():
    # tratamento de dados - pega o que foi passado na url como query e remove espaços
    query = request.args.get('query', '').strip()
    
    # verifica se foi passado alguma coisa na query
    if query:
        # filtra os dados buscando na coluna 'Regiao' todas as linhas que contem a query
        filtered = data[data['Regiao_de_Comercializacao'].str.contains(query, case=False, na=False)]

        records = filtered.to_dict(orient='records')

        cleaned_records = [ # limpeza de NaN para ''
            { key: ('' if pd.isna(value) else value) for key, value in record.items() }
            for record in records
        ]
        
        # pega a lista de dicionario e retorna convertendo pro formato json
        return jsonify(cleaned_records)
    
    return jsonify([])

# modo debug pra mostrar erros no terminal
if __name__ == '__main__':
    app.run(debug=True)

