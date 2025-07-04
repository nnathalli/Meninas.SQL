INSERT INTO Integrante (Matricula, Nome, DataNasc, DataEntrada, Email, Telefone) VALUES
('221000001', 'Ana Silva', '2000-05-15', '2024-01-10', 'ana@unb.br', '(61) 98765-4321'),
('221000002', 'Carla Oliveira', '1999-08-22', '2024-01-10', 'carlos@unb.br', '(61) 98765-1234'),
('221000003', 'Mariana Souza', '2001-03-30', '2024-02-15', 'mariana@unb.br', '(61) 91234-5678');

INSERT INTO FrentesDeTrabalho (Codigo, Nome, Tipo, Descricao, DataCriacao) VALUES
(1, 'Desenvolvimento de Jogos', 'Extensão', 'Foco em jogos educativos', '2024-01-10'),
(2, 'Oficina de Python', 'Ensino', 'Aulas de programação para iniciantes', '2024-02-01');

INSERT INTO IntegranteFrente (Matricula, CodigoFrente, Funcao, Dt_Inicio, Dt_Fim) VALUES
('221000001', 1, 'Coordenadora', '2024-01-10', NULL),
('221000002', 1, 'Desenvolvedora', '2024-01-10', NULL),
('221000003', 2, 'Instrutora', '2024-02-15', NULL);

INSERT INTO Atividades (Codigo, Nome, Descricao, Tipo, Local, DataHora, Duracao) VALUES
(1, 'Workshop Unity', 'Introdução à engine Unity', 'Workshop', 'Sala 101', '2024-03-15 14:00:00', '02:00:00'),
(2, 'Aula de Python Básico', 'Variáveis e estruturas de controle', 'Aula', 'Lab 203', '2024-03-20 10:00:00', '01:30:00');

INSERT INTO IntegranteAtividade (Matricula, CodigoAtividade) VALUES
('221000001', 1),
('221000002', 1),
('221000003', 2);

INSERT INTO Livros (Codigo, Nome, Descricao, Editora, Estoque) VALUES
(1, 'Jogos Educativos em Unity', 'Guia prático para desenvolvimento', 'Editora UNB', 50),
(2, 'Python para Iniciantes', 'Conceitos básicos de programação', 'Editora UNB', 100);

INSERT INTO FrenteLivro (CodigoFrente, CodigoLivro) VALUES
(1, 1),
(2, 2);

INSERT INTO ArtigoPublicado (Codigo, Nome, Publicacao, Data, Autor) VALUES
(1, 'Gamificação na Educação', 'Revista de Inovação', '2024-01-20', 'Ana Silva'),
(2, 'Python no Ensino Médio', 'Congresso de Educação', '2024-02-10', 'Carlos Oliveira');

INSERT INTO FrenteArtigo (CodigoFrente, CodigoArtigo) VALUES
(1, 1),
(2, 2);

INSERT INTO EscolasParceiras (Codigo, Nome, ResponsavelEscola, NumAlunas, Dt_Inicio, Endereco, Email, Telefone) VALUES
(1, 'CEF 01 de Brasília', 'Maria Fernandes', 30, '2024-01-15', 'SQN 302', 'cef01@edu.br', '(61) 3344-5566'),
(2, 'CEM 02 de Taguatinga', 'João Santos', 45, '2024-02-01', 'QNA 10', 'cem02@edu.br', '(61) 3344-7788');

INSERT INTO FrenteEscola (CodigoFrente, CodigoEscola) VALUES
(1, 1),
(2, 2);

INSERT INTO Participante (Id, Nome, Instituicao) VALUES
(1, 'Ana Clara Silva', 'UNB'),
(2, 'Beatriz Oliveira', 'UNB'),
(3, 'Camila Santos', 'IFB'),
(4, 'Daniela Costa', 'CEFET'),
(5, 'Eduarda Pereira', 'UNB'),
(6, 'Fernanda Almeida', 'UniCEUB'),
(7, 'Gabriela Rocha', 'UniDF'),
(8, 'Helena Mendes', 'UNB');

INSERT INTO Equipe (Id_equipe, NomeEquipe) VALUES
(1, 'CodeGirls UNB'),
(2, 'Python Queens'),
(3, 'Algorithm Sisters'),
(4, 'Byte Ladies');

INSERT INTO ParticipanteEquipe (IdParticipante, Id_equipe, Email, Telefone) VALUES
(1, 1, 'ana.clara@unb.br', '(61) 98765-4321'),
(2, 1, 'beatriz@unb.br', '(61) 98765-1234'),
(3, 2, 'camila@ifb.br', '(61) 91234-5678'),
(4, 2, 'daniela@cefet.br', '(61) 93456-7890'),
(5, 3, 'eduarda@unb.br', '(61) 94567-8901'),
(6, 3, 'fernanda@uniceub.br', '(61) 95678-9012'),
(7, 4, 'gabriela@unidf.br', '(61) 96789-0123'),
(8, 4, 'helena@unb.br', '(61) 97890-1234');

INSERT INTO MaratonaProg (Codigo, Nome, Edicao, Premiacao) VALUES
(1, 'Maratona Meninas na Computação', '2024', 'Bolsa de estudos + Mentoria'),
(2, 'Hackathon Elas Programam', '2023', 'Notebook + Curso Avançado'),
(3, 'Desafio Programação para Mulheres', '2024', 'Viagem para evento internacional');

INSERT INTO FrenteMaratona (CodigoFrente, CodigoMaratona) VALUES
(1, 1),
(2, 2);

INSERT INTO EquipeMaratona (Id_equipe, CodigoMaratona, Classificacao) VALUES
(1, 1, '1º Lugar'),
(2, 1, '2º Lugar'),
(3, 2, '1º Lugar'),
(4, 3, 'Finalista');

INSERT INTO Perguntas (Codigo, Enunciado, Edicao, Gabarito, CodigoMaratona) VALUES
(1, 'Implemente uma função que calcule o fatorial de um número', '2024', 'def fatorial(n): return 1 if n==0 else n*fatorial(n-1)', 1),
(2, 'Crie um algoritmo para ordenar uma lista de nomes', '2024', 'sorted(lista)', 1),
(3, 'Desenvolva um CRUD simples em Python', '2023', 'Resposta esperada: implementação com funções create, read, update, delete', 2);

