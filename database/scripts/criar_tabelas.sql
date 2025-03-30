-- criando da tabela de demonstraçoes contabeis
create table demonstracoes_contabeis (
    data date,
    reg_ans varchar(10),
    cd_conta_contabil varchar(10),
    descricao text,
    vl_saldo_inicial numeric(15,2),
    vl_saldo_final numeric(15,2)
);

-- criando da tabela de operadoras ativas
create table operadoras_ativas (
    registro_ans varchar(10) primary key,
    cnpj varchar(20),
    razao_social text,
    nome_fantasia text,
    modalidade text,
    logradouro text,
    numero text,
    complemento text,
    bairro text,
    cidade text,
    uf char(2),
    cep varchar(10),
    ddd varchar(3),
    telefone varchar(15),
    fax varchar(15),
    endereco_eletronico text,
    representante text,
    cargo_representante text,
    regiao_comercializacao int,
    data_registro_ans date
);