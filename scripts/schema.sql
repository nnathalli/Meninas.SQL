CREATE TABLE Integrante (
    Matricula VARCHAR(9) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNasc DATE NOT NULL,
    DataEntrada DATE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(15) NOT NULL
);
 
CREATE TABLE Professora (
    Matricula VARCHAR(9) PRIMARY KEY,
    AreaAtuacao VARCHAR(100) NOT NULL,
    Curriculo TEXT NOT NULL,
    Instituicao VARCHAR(100) NOT NULL,
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula)
);
 
CREATE TABLE Aluna (
    Matricula VARCHAR(9) PRIMARY KEY,
    Bolsa BOOLEAN NOT NULL,
    NomeCurso VARCHAR(100) NOT NULL,
    InstituicaoCurso VARCHAR(100) NOT NULL,
    Departamento VARCHAR(100) NOT NULL,
    Instituicao VARCHAR(100) NOT NULL,
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula)
);
 
CREATE TABLE FrentesDeTrabalho (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Descricao TEXT NOT NULL,
    DataCriacao DATE NOT NULL
);
 
CREATE TABLE Atividades (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Local VARCHAR(100),
    DataHora TIMESTAMP,
    Duracao INTERVAL
);
 
CREATE TABLE IntegranteAtividade (
    Matricula VARCHAR(9) NOT NULL,
    CodigoAtividade INT NOT NULL,
    PRIMARY KEY (Matricula, CodigoAtividade),
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula),
    FOREIGN KEY (CodigoAtividade) REFERENCES Atividades(Codigo)
);
 
CREATE TABLE IntegranteFrente (
    Matricula VARCHAR(9) NOT NULL,
    CodigoFrente INT NOT NULL,
    Funcao VARCHAR(100) NOT NULL,
    Dt_Inicio DATE NOT NULL,
    Dt_Fim DATE,
    PRIMARY KEY (Matricula, CodigoFrente),
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo)
);
 
CREATE TABLE EscolasParceiras (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    ResponsavelEscola VARCHAR(100) NOT NULL,
    NumAlunas INT CHECK (NumAlunas >= 0),
    Dt_Inicio DATE NOT NULL,
    Endereco TEXT NOT NULL
    Email VARCHAR(100) NOT NULL
    Telefone VARCHAR(15) NOT NULL
);
 
CREATE TABLE TelefoneEscola (
    Id SERIAL PRIMARY KEY,
    CodigoEscola INT NOT NULL,
    Telefone VARCHAR(15) NOT NULL,
    FOREIGN KEY (CodigoEscola) REFERENCES EscolasParceiras(Codigo)
);
 
CREATE TABLE EmailEscola (
    Id SERIAL PRIMARY KEY,
    CodigoEscola INT NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FOREIGN KEY (CodigoEscola) REFERENCES EscolasParceiras(Codigo)
);
 
CREATE TABLE FrenteEscola (
    CodigoFrente INT NOT NULL,
    CodigoEscola INT NOT NULL,
    PRIMARY KEY (CodigoFrente, CodigoEscola),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo),
    FOREIGN KEY (CodigoEscola) REFERENCES EscolasParceiras(Codigo)
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
    Estoque INT CHECK (Estoque >= 0)
);
 
CREATE TABLE FrenteLivro (
    CodigoFrente INT NOT NULL,
    CodigoLivro INT NOT NULL,
    PRIMARY KEY (CodigoFrente, CodigoLivro),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo),
    FOREIGN KEY (CodigoLivro) REFERENCES Livros(Codigo)
);
 
CREATE TABLE LivroAutor (
    CodigoLivro INT NOT NULL,
    Matricula VARCHAR(9) NOT NULL,
    PRIMARY KEY (CodigoLivro, Matricula),
    FOREIGN KEY (CodigoLivro) REFERENCES Livros(Codigo),
    FOREIGN KEY (Matricula) REFERENCES Integrante(Matricula)
);
 
CREATE TABLE ArtigoPublicado (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Publicacao VARCHAR(100) NOT NULL,
    Data DATE NOT NULL,
    Autor VARCHAR(100) NOT NULL
);
 
CREATE TABLE FrenteArtigo (
    CodigoFrente INT NOT NULL,
    CodigoArtigo INT NOT NULL,
    PRIMARY KEY (CodigoFrente, CodigoArtigo),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo),
    FOREIGN KEY (CodigoArtigo) REFERENCES ArtigoPublicado(Codigo)
);
 
CREATE TABLE MaratonaProg (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Edicao VARCHAR(100) NOT NULL,
    Premiacao VARCHAR(100)
);
 
CREATE TABLE Perguntas (
    Codigo INT PRIMARY KEY,
    Enunciado TEXT NOT NULL,
    Edicao VARCHAR(100) NOT NULL,
    Gabarito TEXT NOT NULL,
    CodigoMaratona INT NOT NULL,
    FOREIGN KEY (CodigoMaratona) REFERENCES MaratonaProg(Codigo)
);
 
CREATE TABLE FrenteMaratona (
    CodigoFrente INT NOT NULL,
    CodigoMaratona INT NOT NULL,
    PRIMARY KEY (CodigoFrente, CodigoMaratona),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo),
    FOREIGN KEY (CodigoMaratona) REFERENCES MaratonaProg(Codigo)
);
 
CREATE TABLE Equipe (
    Id_equipe INT PRIMARY KEY,
    NomeEquipe VARCHAR(100) NOT NULL
);
 
CREATE TABLE Participante (
    Id INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Instituicao VARCHAR(100) NOT NULL
);
 
CREATE TABLE ParticipanteEquipe (
    IdParticipante INT NOT NULL,
    Id_equipe INT NOT NULL,
    PRIMARY KEY (IdParticipante, Id_equipe),
    FOREIGN KEY (IdParticipante) REFERENCES Participante(Id),
    FOREIGN KEY (Id_equipe) REFERENCES Equipe(Id_equipe)
    Email VARCHAR(100) NOT NULL
    Telefone VARCHAR(15) NOT NULL
);
 
CREATE TABLE EquipeMaratona (
    Id_equipe INT NOT NULL,
    CodigoMaratona INT NOT NULL,
    Classificacao VARCHAR(50) NOT NULL,
    PRIMARY KEY (Id_equipe, CodigoMaratona),
    FOREIGN KEY (Id_equipe) REFERENCES Equipe(Id_equipe),
    FOREIGN KEY (CodigoMaratona) REFERENCES MaratonaProg(Codigo)
);
 
CREATE TABLE ColecaoProjetos (
    Codigo INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tema VARCHAR(100) NOT NULL
);
 
CREATE TABLE FrenteColecao (
    CodigoFrente INT NOT NULL,
    CodigoColecao INT NOT NULL,
    PRIMARY KEY (CodigoFrente, CodigoColecao),
    FOREIGN KEY (CodigoFrente) REFERENCES FrentesDeTrabalho(Codigo),
    FOREIGN KEY (CodigoColecao) REFERENCES ColecaoProjetos(Codigo)
);
