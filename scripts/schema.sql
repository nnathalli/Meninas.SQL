CREATE TABLE Curso (
    Codcurso INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Instituicao VARCHAR(100) NOT NULL,
    Departamento VARCHAR(100) NOT NULL
);

CREATE TABLE Professora (
    Matricula VARCHAR(20) PRIMARY KEY,
    AreaAtuacao VARCHAR(100) NOT NULL,
    Curriculo TEXT NOT NULL,
    Instituicao VARCHAR(100) NOT NULL
);

CREATE TABLE Aluna (
    Matricula VARCHAR(20) PRIMARY KEY,
    Bolsa BOOLEAN NOT NULL,
    CodCurso INT NOT NULL,
    FOREIGN KEY (CodCurso) REFERENCES Curso(Codigo)
);

CREATE TABLE Integrante (
    Matricula VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNasc DATE NOT NULL,
    DataEntrada DATE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(20) NOT NULL
);

CREATE TABLE FrentesDeTrabalho (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Descricao TEXT NOT NULL,
    DataCriacao DATE NOT NULL
);

CREATE TABLE Producoes (
    Codigo INT PRIMARY KEY,
    Tipo VARCHAR(50) NOT NULL
);

CREATE TABLE Livros (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Editora VARCHAR(100) NOT NULL,
    Estoque INT NOT NULL,
    Arquivo_pdf BYTEA
);

CREATE TABLE Atividades (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Local VARCHAR(100) NOT NULL,
    DataHora DATE NOT NULL,
    Duracao INT NOT NULL
);

CREATE TABLE EscolasParceiras (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    ResponsavelEscola VARCHAR(100) NOT NULL,
    NumAlunas INT NOT NULL,
    Endereco TEXT NOT NULL,
    Dt_Inicio DATE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(20) NOT NULL
);

CREATE TABLE MaratonaProg (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Edicao VARCHAR(20) NOT NULL,
    Premiacao VARCHAR(100) NOT NULL
);

CREATE TABLE ArtigoPublicado (
    Codigo INT PRIMARY KEY,
    Data DATE NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Publicacao VARCHAR(100) NOT NULL,
    Autor VARCHAR(100) NOT NULL,
    Arquivo_pdf BYTEA
);

CREATE TABLE Perguntas (
    Codigo INT PRIMARY KEY,
    Enunciado TEXT NOT NULL,
    Edicao VARCHAR(20) NOT NULL,
    CodigoMaratona INT NOT NULL,
    FOREIGN KEY (CodMaratona) REFERENCES MaratonasProg(Codigo)
);

CREATE TABLE Equipe (
    Id_equipe INT PRIMARY KEY,
    NomeEquipe VARCHAR(100) NOT NULL
);

CREATE TABLE IntegranteFrente (
    Matricula VARCHAR(20),
    CodigoFrente INT,
    Funcao VARCHAR(50) NOT NULL,
    Dt_Inicio DATE NOT NULL,
    Dt_Fim DATE,
    PRIMARY KEY (Matricula, CodigoFrente),
    FOREIGN KEY (Matricula) REFERENCES Integrantes(Matricula) ON DELETE CASCADE,
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo) ON DELETE CASCADE
);

CREATE TABLE FrenteAtividade (
    CodigoFrente INT,
    CodigoAtividade INT,
    PRIMARY KEY (CodigoFrente, CodigoAtividade),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo) ON DELETE CASCADE,
    FOREIGN KEY (CodigoAtividade) REFERENCES Atividades(Codigo) ON DELETE CASCADE
);

CREATE TABLE FrenteProducoes (
    CodigoFrente INT,
    CodigoProducao INT,
    PRIMARY KEY (CodigoFrente, CodigoProducao),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo) ON DELETE CASCADE
);

CREATE TABLE FrenteEscola (
    CodigoFrente INT,
    CodigoEscola INT,
    PRIMARY KEY (CodigoFrente, CodigoEscola),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo) ON DELETE CASCADE,
    FOREIGN KEY (CodigoEscola) REFERENCES EscolasParceiras(Codigo) ON DELETE CASCADE
);

CREATE TABLE LivroAutor (
    CodigoLivro INT,
    Matricula VARCHAR(20),
    PRIMARY KEY (CodigoLivro, Matricula),
    FOREIGN KEY (CodigoLivro) REFERENCES Livros(Codigo),
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula)
);

CREATE TABLE ParticipanteEquipe (
    Id_equipe INT,
    Id_participante INT,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    Telefone VARCHAR(20),
    PRIMARY KEY (Id_equipe, Id_participante),
    FOREIGN KEY (Id_equipe) REFERENCES Equipe(Id_equipe)
);

CREATE TABLE EquipeMaratona (
    Id_equipe INT,
    CodigoMaratona INT,
    Classificacao VARCHAR(50),
    PRIMARY KEY (Id_equipe, CodigoMaratona),
    FOREIGN KEY (Id_equipe) REFERENCES Equipe(Id_equipe),
    FOREIGN KEY (CodigoMaratona) REFERENCES MaratonasProg(Codigo)
);

CREATE TABLE IntegranteAtividade (
    Matricula VARCHAR(20),
    CodigoAtividade INT,
    PRIMARY KEY (Matricula, CodigoAtividade),
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula),
    FOREIGN KEY (CodigoAtividade) REFERENCES Atividades(Codigo)
);