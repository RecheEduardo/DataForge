-- 10 operadoras com maiores despesas em sinistros medico-hospitalares no ultimo trimestre
Select 
    o.razao_social, sum(d.vl_saldo_final - d.vl_saldo_inicial) as total_despesas
from 
    demonstracoes_contabeis d
join 
    operadoras_ativas o 
    on d.reg_ans = o.registro_ans
where 
    d.descricao = 'eventos/ sinistros conhecidos ou avisados de assistência a saúde médico hospitalar'
    and d.data >= (current_date - interval '3 months')
group by 
    o.razao_social
order by 
    total_despesas desc
limit 
    10;



-- 10 operadoras com maiores despesas no ultimo ano
Select 
    o.razao_social, 
    sum(d.vl_saldo_final - d.vl_saldo_inicial) as total_despesas
from 
    demonstracoes_contabeis d
join 
    operadoras_ativas o 
    on d.reg_ans = o.registro_ans
where 
    d.descricao = 'eventos/ sinistros conhecidos ou avisados de assistência a saúde médico hospitalar'
    and d.data >= (current_date - interval '1 year')
group by 
    o.razao_social
order by 
    total_despesas desc
limit 
    10;