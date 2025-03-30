-- pegando dados para demonstracoes_contabeis
copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/1T2023.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/2t2023.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/3T2023.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/4T2023.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/1T2024.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/2T2024.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/3T2024.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

copy demonstracoes_contabeis from 'database/downloads/demonstrativos_contabeis/4T2024.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';

-- pegando dados para operadoras_ativas
copy operadoras_ativas from 'database/downloads/operadoras/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER encoding 'LATIN1';
