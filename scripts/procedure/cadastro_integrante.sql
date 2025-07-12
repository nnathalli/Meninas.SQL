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
    p_funcao VARCHAR DEFAULT 'Participante'
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_curso_existe BOOLEAN;
BEGIN
    -- Validação de campos únicos
    IF EXISTS (SELECT 1 FROM integrante WHERE matricula = p_matricula) THEN
        RAISE EXCEPTION 'Matrícula já cadastrada no sistema.';
    END IF;
    
    IF EXISTS (SELECT 1 FROM integrante WHERE email = p_email) THEN
        RAISE EXCEPTION 'Já existe um integrante com este email.';
    END IF;
    
    IF EXISTS (SELECT 1 FROM integrante WHERE telefone = p_telefone) THEN
        RAISE EXCEPTION 'Telefone já cadastrado no sistema.';
    END IF;

    -- Validação de tipo (aluna/professora)
    IF p_tipo NOT IN ('aluna', 'professora') THEN
        RAISE EXCEPTION 'Tipo de integrante inválido: deve ser "aluna" ou "professora".';
    END IF;

    -- Validações específicas para alunas
    IF p_tipo = 'aluna' THEN
        -- Verifica se a matrícula já existe como professora
        IF EXISTS (SELECT 1 FROM professora WHERE matricula = p_matricula) THEN
            RAISE EXCEPTION 'Esta matrícula já pertence a uma professora.';
        END IF;
        
        -- Verifica se o curso existe (se estiver usando codcurso como FK)
        IF (p_extra->>'codcurso') IS NOT NULL THEN
            SELECT EXISTS (SELECT 1 FROM curso WHERE codcurso = (p_extra->>'codcurso')::INT) 
            INTO v_curso_existe;
            
            IF NOT v_curso_existe THEN
                RAISE EXCEPTION 'Curso não encontrado.';
            END IF;
        END IF;
    END IF;

    -- Validações específicas para professoras
    IF p_tipo = 'professora' THEN
        -- Verifica se a matrícula já existe como aluna
        IF EXISTS (SELECT 1 FROM aluna WHERE matricula = p_matricula) THEN
            RAISE EXCEPTION 'Esta matrícula já pertence a uma aluna.';
        END IF;
    END IF;

    -- Inicia transação
    BEGIN
        -- Insere dados básicos do integrante
        INSERT INTO integrante (matricula, nome, datanasc, dataentrada, email, telefone)
        VALUES (p_matricula, p_nome, p_data_nasc, p_data_entrada, p_email, p_telefone);

        -- Insere dados específicos
        IF p_tipo = 'aluna' THEN
            INSERT INTO aluna (
                matricula, 
                bolsa, 
                codcurso  -- Usando codcurso como FK conforme seu CRUD original
            )
            VALUES (
                p_matricula,
                (p_extra->>'bolsa')::BOOLEAN,
                (p_extra->>'codcurso')::INT
            );
        ELSE
            INSERT INTO professora (
                matricula, 
                areaatuacao, 
                curriculo, 
                instituicao
            )
            VALUES (
                p_matricula,
                p_extra->>'areaatuacao',
                p_extra->>'curriculo',
                p_extra->>'instituicao'
            );
        END IF;

        -- Associação com frente (se solicitado)
        IF p_codigo_frente IS NOT NULL THEN
            -- Verifica se a frente existe
            IF NOT EXISTS (SELECT 1 FROM frentesdetrabalho WHERE codigo = p_codigo_frente) THEN
                RAISE EXCEPTION 'Frente de trabalho não encontrada.';
            END IF;
            
            -- Verifica vínculo ativo
            IF EXISTS (
                SELECT 1 FROM integrantefrente
                WHERE matricula = p_matricula
                  AND codigofrente = p_codigo_frente
                  AND dt_fim IS NULL
            ) THEN
                RAISE EXCEPTION 'Já existe vínculo ativo com essa frente.';
            END IF;

            -- Cria o vínculo
            INSERT INTO integrantefrente (
                matricula, 
                codigofrente, 
                funcao, 
                dt_inicio, 
                dt_fim
            )
            VALUES (
                p_matricula, 
                p_codigo_frente, 
                p_funcao, 
                CURRENT_DATE, 
                NULL
            );
        END IF;

        COMMIT;
        RAISE NOTICE 'Integrante cadastrado com sucesso.';
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            RAISE EXCEPTION 'Erro no cadastro: %', SQLERRM;
    END;
END;
$$;