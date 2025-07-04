CREATE OR REPLACE VIEW view_maratona AS
SELECT 
    m.Codigo AS id_maratona,
    m.Nome AS nome_maratona,
    m.Edicao AS edicao,
    m.Premiacao AS premiacao,
    
    (SELECT COUNT(*) FROM EquipeMaratona WHERE CodigoMaratona = m.Codigo) AS total_equipes,
    
    (SELECT STRING_AGG(e.NomeEquipe, ', ' ORDER BY e.NomeEquipe)
    FROM Equipe e
    JOIN EquipeMaratona em ON e.Id_equipe = em.Id_equipe
    WHERE em.CodigoMaratona = m.Codigo) AS equipes_participantes,
    
    (SELECT COUNT(*) FROM Perguntas WHERE CodigoMaratona = m.Codigo) AS total_perguntas,
    
    (SELECT COALESCE(
        JSON_AGG(
            JSON_BUILD_OBJECT(
                'id', p.Codigo,
                'enunciado', p.Enunciado,
                'dificuldade', p.Edicao
            ) ORDER BY p.Codigo
        ), 
        '[]'::json) 
    FROM Perguntas p
    WHERE p.CodigoMaratona = m.Codigo) AS perguntas_detalhadas,
    
    (SELECT STRING_AGG(e.NomeEquipe || ' - ' || em.Classificacao, ' | ')
    FROM Equipe e
    JOIN EquipeMaratona em ON e.Id_equipe = em.Id_equipe
    WHERE em.CodigoMaratona = m.Codigo) AS classificacao

FROM MaratonaProg m
ORDER BY m.Codigo;
