CREATE OR REPLACE VIEW view_dashboard_gerencial AS
SELECT 
    f.Codigo AS CodigoFrente,
    f.Nome AS Frente,
    f.Tipo,
    COUNT(DISTINCT if.Matricula) AS TotalIntegrantes,
    ARRAY_AGG(DISTINCT i.Nome) AS Integrantes,
    COUNT(DISTINCT a.Codigo) AS TotalAtividades,
    ARRAY_AGG(DISTINCT a.Nome) AS Atividades,
    COUNT(DISTINCT l.Codigo) AS TotalLivros,
    ARRAY_AGG(DISTINCT l.Nome) AS Livros,
    COUNT(DISTINCT ap.Codigo) AS TotalArtigos,
    ARRAY_AGG(DISTINCT ap.Nome) AS Artigos,
    MAX(a.DataHora) AS UltimaAtividade,
    STRING_AGG(DISTINCT e.Nome, ', ') AS EscolasParceiras
FROM 
    FrentesDeTrabalho f
LEFT JOIN 
    IntegranteFrente if ON f.Codigo = if.CodigoFrente AND (if.Dt_Fim IS NULL OR if.Dt_Fim >= CURRENT_DATE)
LEFT JOIN 
    Integrante i ON if.Matricula = i.Matricula
LEFT JOIN 
    IntegranteAtividade ia ON if.Matricula = ia.Matricula
LEFT JOIN 
    Atividades a ON ia.CodigoAtividade = a.Codigo
LEFT JOIN 
    FrenteLivro fl ON f.Codigo = fl.CodigoFrente
LEFT JOIN 
    Livros l ON fl.CodigoLivro = l.Codigo
LEFT JOIN 
    FrenteArtigo fa ON f.Codigo = fa.CodigoFrente
LEFT JOIN 
    ArtigoPublicado ap ON fa.CodigoArtigo = ap.Codigo
LEFT JOIN 
    FrenteEscola fe ON f.Codigo = fe.CodigoFrente
LEFT JOIN 
    EscolasParceiras e ON fe.CodigoEscola = e.Codigo
GROUP BY 
    f.Codigo, f.Nome, f.Tipo;
