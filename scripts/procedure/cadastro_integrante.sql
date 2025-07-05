CREATE OR REPLACE PROCEDURE cadastro_integrante(
    p_matricula VARCHAR,
    p_nome VARCHAR,
    p_data_nasc DATE,
    p_data_entrada DATE,
    p_email VARCHAR,
    p_telefone VARCHAR,
    p_tipo VARCHAR,
    p_extra JSON,
    p_codigo_frente INT DEFAULT NULL,
    p_funcao VARCHAR DEFAULT 'Participante',
    p_associar_atividades BOOLEAN DEFAULT FALSE
)
LANGUAGE plpgsql
AS $$
DECLARE
    atividade_id INT;
BEGIN
    IF EXISTS (
        SELECT 1 FROM integrante WHERE email = p_email
    ) THEN
        RAISE EXCEPTION 'Já existe um integrante com este email.';
    END IF;

    IF p_tipo = 'aluna' AND EXISTS (
        SELECT 1 FROM professora WHERE matricula = p_matricula
    ) THEN
        RAISE EXCEPTION 'Esta matrícula já pertence a uma professora.';
    ELSIF p_tipo = 'professora' AND EXISTS (
        SELECT 1 FROM aluna WHERE matricula = p_matricula
    ) THEN
        RAISE EXCEPTION 'Esta matrícula já pertence a uma aluna.';
    END IF;

    INSERT INTO integrante (matricula, nome, datanasc, dataentrada, email, telefone)
    VALUES (p_matricula, p_nome, p_data_nasc, p_data_entrada, p_email, p_telefone);

    IF p_tipo = 'aluna' THEN
        INSERT INTO aluna (
            matricula, bolsa, nomecurso, instituicaocurso, departamento, instituicao
        )
        VALUES (
            p_matricula,
            COALESCE((p_extra->>'bolsa')::BOOLEAN, FALSE),
            p_extra->>'nomecurso',
            p_extra->>'instituicaocurso',
            p_extra->>'departamento',
            p_extra->>'instituicao'
        );

    ELSIF p_tipo = 'professora' THEN
        INSERT INTO professora (
            matricula, areaatuacao, curriculo, instituicao
        )
        VALUES (
            p_matricula,
            p_extra->>'areaatuacao',
            p_extra->>'curriculo',
            p_extra->>'instituicao'
        );
    ELSE
        RAISE EXCEPTION 'Tipo de integrante inválido: deve ser "aluna" ou "professora".';
    END IF;

    IF p_codigo_frente IS NOT NULL THEN
        IF EXISTS (
            SELECT 1 FROM integrantefrente
            WHERE matricula = p_matricula
              AND codigofrente = p_codigo_frente
              AND dt_fim IS NULL
        ) THEN
            RAISE EXCEPTION 'Já existe vínculo ativo com essa frente.';
        END IF;

        INSERT INTO integrantefrente (matricula, codigofrente, funcao, dt_inicio, dt_fim)
        VALUES (p_matricula, p_codigo_frente, p_funcao, CURRENT_DATE, NULL);

        IF p_associar_atividades THEN
            FOR atividade_id IN
                SELECT DISTINCT a.codigo
                FROM atividades a
                JOIN integranteatividade ia ON ia.codigoatividade = a.codigo
                JOIN integrantefrente inf ON inf.matricula = ia.matricula
                WHERE inf.codigofrente = p_codigo_frente
                  AND a.datahora > CURRENT_DATE - INTERVAL '30 days'
            LOOP
                IF NOT EXISTS (
                    SELECT 1 FROM integranteatividade
                    WHERE matricula = p_matricula AND codigoatividade = atividade_id
                ) THEN
                    INSERT INTO integranteatividade (matricula, codigoatividade)
                    VALUES (p_matricula, atividade_id);
                END IF;
            END LOOP;
        END IF;
    END IF;

    RAISE NOTICE 'Integrante cadastrado com sucesso.';
END;
$$;
