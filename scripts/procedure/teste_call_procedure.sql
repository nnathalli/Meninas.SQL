CALL cadastro_integrante(
    '221000009',
    'Juliana Souza',
    '2001-10-20',
    '2025-01-15',
    'juliana@unb.br',
    '(61)91234-7890',
    'aluna',
    '{
        "bolsa": true,
        "nomecurso": "Engenharia de Software",
        "instituicaocurso": "UnB",
        "departamento": "Computação",
        "instituicao": "UnB"
    }',
    2, 'Instrutora', TRUE
);

CALL cadastro_integrante(
    '221000010',
    'Luciana Ribeiro',
    '1985-03-12',
    '2025-02-01',
    'luciana@unb.br',
    '(61)99876-5432',
    'professora',
    '{
        "areaatuacao": "Algoritmos",
        "curriculo": "Doutora em Ciência da Computação",
        "instituicao": "UnB"
    }'
);

CALL cadastro_integrante(
    '221000013',
    'Ana Teste',
    '2002-05-20',
    '2023-08-25',
    'ana.teste@unb.br',
    '(61)99999-9999',
    'aluna',
    '{
        "bolsa": false,
        "nomecurso": "Ciência da Computação",
        "instituicaocurso": "UnB",
        "departamento": "Ciência da Computação",
        "instituicao": "UnB"
    }',
    1
);

-- Esta chamada irá falhar, pois Juliana já está vinculada à frente 2
CALL cadastro_integrante(
    '221000009',
    'Juliana Souza',
    '2001-10-20',
    '2025-01-15',
    'juliana@unb.br',
    '(61)91234-7890',
    'aluna',
    '{
        "bolsa": true,
        "nomecurso": "Engenharia de Software",
        "instituicaocurso": "UnB",
        "departamento": "Computação",
        "instituicao": "UnB"
    }',
    2, 'Instrutora', TRUE
);
