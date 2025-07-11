CREATE OR REPLACE VIEW view_frentes_atividades AS
SELECT 
    f.codigo AS frente_codigo,
    f.nome AS frente_nome,
    f.tipo AS frente_tipo,
    f.descricao AS frente_descricao,
    f.datacriacao AS frente_data_criacao,
    inf.matricula AS integrante_matricula,
    i.nome AS integrante_nome,
    inf.funcao AS integrante_funcao,
    inf.dt_inicio AS integrante_data_inicio,
    inf.dt_fim AS integrante_data_fim,
    a.codigo AS atividade_codigo,
    a.nome AS atividade_nome,
    a.tipo AS atividade_tipo,
    a.local AS atividade_local,
    a.datahora AS atividade_data_hora,
    ia.matricula AS atividade_integrante_matricula,
    ia2.nome AS atividade_integrante_nome
FROM 
    frentesdetrabalho f
LEFT JOIN 
    integrantefrente inf ON f.codigo = inf.codigofrente
LEFT JOIN 
    integrante i ON inf.matricula = i.matricula
LEFT JOIN 
    atividades a ON a.codigo = a.codigo  -- Esta linha foi ajustada pois não há relação direta entre frentes e atividades
LEFT JOIN 
    integranteatividade ia ON a.codigo = ia.codigoatividade
LEFT JOIN 
    integrante ia2 ON ia.matricula = ia2.matricula;