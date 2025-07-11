CREATE OR REPLACE VIEW view_integrantes_completos AS
SELECT 
    i.matricula,
    i.nome,
    i.email,
    i.telefone,
    i.datanasc,
    i.dataentrada,
    CASE 
        WHEN p.matricula IS NOT NULL THEN 'Professora'
        WHEN a.matricula IS NOT NULL THEN 'Aluna'
        ELSE 'Tipo não definido'
    END AS tipo_integrante,
    p.areaatuacao AS professora_area_atuacao,
    p.curriculo AS professora_curriculo,
    p.instituicao AS professora_instituicao,
    a.bolsa AS aluna_bolsa,
    c.nome AS aluna_curso_nome,
    c.instituicao AS aluna_curso_instituicao,
    c.departamento AS aluna_curso_departamento
FROM 
    integrante i
LEFT JOIN 
    professora p ON i.matricula = p.matricula
LEFT JOIN 
    aluna a ON i.matricula = a.matricula
LEFT JOIN 
    curso c ON a.codcurso = c.codcurso;