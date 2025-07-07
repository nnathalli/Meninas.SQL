# Meninas.SQL – Projeto Final de Banco de Dados

Este repositório contém o sistema desenvolvido para o projeto Meninas.SQL, que visa organizar os dados do projeto Meninas.comp da UnB, utilizando banco de dados PostgreSQL, interface gráfica e persistência com Python.
---
## Sobre o Projeto Meninas.comp

O projeto Meninas.comp incentiva a participação de meninas nas áreas de computação e tecnologia. Este sistema tem como objetivo armazenar, consultar e manter dados das alunas, professoras, atividades, produtos e parcerias.
---
## Integrantes

* Maria Eduarda Pacheco Ferreira de Freitas – 221003977
* Sara Lima Gaspar – 221017121
* Pedro Maia de Oliveira Evangelista – 232005951
* Náthalli de Oliveira Maciel – 221018970
---
## Licença

Este projeto é acadêmico, sem fins lucrativos, e tem fins exclusivamente educacionais.
---
## Requisitos

- Python 3.10+
- PostgreSQL 15+
- Biblioteca: 'psycopg2-binary'
---
### Instalação das dependências:
```bash
pip install psycopg2-binary

# Configuração do Banco de Dados

1. Crie o banco de dados no pgAdmin com o nome desejado (ex: Meninas.SQL)

2. Execute o script SQL:

   ```bash
   \i scripts/schema.sql
   ```

3. Configure suas credenciais reais no arquivo ‘database/DatabaseConnection.py’

> ⚠️ Importante: Não versionar esse arquivo com a senha real! Use o ‘.gitignore’.

- Testando a Conexão com o Banco

Após configurar corretamente o `DatabaseConnection.py`, execute:

```bash
python -m tests.teste_connection
```

Se tudo estiver funcionando corretamente, o terminal deve exibir:

```
Conexão bem-sucedida com o banco!
```
---
## Funcionalidades CRUD Implementadas

-Tabelas escolhidas para o CRUD:
>1 - Integrante;  
>2 - FrentesDeTrabalho;  
>3 - Atividades;  
>4 - Livros (para facilitar inserção de dados binários);  
>5 - Artigos (para facilitar inserção de dados binários).  

Comandos para os testes do CRUD:
```
python -m tests.teste_integrante_crud
python -m tests.teste_frente_crud
python -m tests.teste_atividade_crud
python -m tests.teste_artigo_crud
python -m tests.teste_livro_crud
```

Comandos para verificação dos dados inseridos/atualizados no pgAdmin:

SELECT * FROM integrante;  
SELECT * FROM frentesdetrabalho;  
SELECT * FROM atividades;  
SELECT matricula, nome, LENGTH(foto) as tamanho_foto FROM integrante WHERE foto IS NOT NULL;
SELECT codigo, nome, LENGTH(arquivo_pdf) as tamanho_pdf FROM artigopublicado;
SELECT codigo, nome, LENGTH(arquivo_pdf) as tamanho_pdf FROM livros;  
---
## Views implementadas

Foram criadas duas views no banco de dados, usadas para facilitar consultas com dados agregados e organizados.  
scripts/views.sql  

###  view_dashboard_gerencial.  
_Apresenta um panorama geral das frentes de trabalho:_

> Contém:  
Nome da frente e tipo (ensino, extensão etc.),  
Total de integrantes e seus nomes,  
Total de atividades e nomes das atividades,  
Total de livros e artigos vinculados,  
Data da última atividade,  
Escola parceira associada (se houver).  

* Localização: scripts/views.sql/view_dashboard_gerencial.sql

* Consulta: SELECT * FROM view_dashboard_gerencial;

### view_maratonas  
_Mostra um resumo completo das maratonas de programação._

> Contém:  
Nome,  
Edição e premiação da maratona,  
Total de equipes e participantes,  
Nomes das equipes e participantes,  
Classificações,  
Perguntas aplicadas, com enunciado e edição (em JSON). 

* Localização: scripts/views.sql/view_maratona.sql

* Consulta: SELECT * FROM view_maratona;

---

## Procedure
scripts/procedure/cadastro_integrante.sql  

A procedure implementa a lógica completa de cadastro de um novo integrante, com validações e relacionamento:

- Evita cadastro duplicado por e-mail ou matrícula;  
- Bloqueia conflito entre `aluna` e `professora`;  
- Insere na tabela `Integrante`;  
- Insere na tabela específica (Aluna ou Professora);  
- Vincula à frente de trabalho (se fornecido);  
- Associa automaticamente às atividades recentes da frente (últimos 30 dias).  

###  Teste SQL da Procedure
O arquivo de teste está em:  
scripts/procedure/teste_call_procedure.sql  

###  Como executar no pgAdmin
Abra o Query Tool e rode:  

```sql
\i scripts/procedures/testes/teste_cadastrar_integrante_com_vinculo.sql


Consulta para verificar os resultados:  
SELECT * FROM integrante;  
SELECT * FROM aluna;  
SELECT * FROM professora;  
SELECT * FROM integrantefrente;  
SELECT * FROM integranteatividade;  

---
## Inserção de dados binários

As funções de upload e download desses arquivos foram integradas nos CRUDs e testadas por meio de scripts em `tests/`, garantindo que os dados binários sejam corretamente armazenados e recuperados.  

* Inserção de Arquivos

>Foto (imagem) em Integrante: permite armazenar imagens das participantes de forma segura no banco, utilizando o tipo `BYTEA`.

>Arquivo PDF em Livros e Artigos: possibilita o armazenamento e posterior download de arquivos PDF vinculados aos registros de livros e artigos publicados no projeto, também utilizando o tipo `BYTEA`.

Como testar:
```bash
python -m tests.teste_dadobinario       # Teste de fotos
python -m tests.teste_artigo_crud      # Teste de artigos com PDF
python -m tests.teste_livro_crud       # Teste de livros com PDF 
````

Consulta de verificação no pgAdmin:

```sql
SELECT matricula, nome, LENGTH(foto) as tamanho_foto FROM integrante WHERE foto IS NOT NULL;
SELECT codigo, nome, LENGTH(arquivo_pdf) as tamanho_pdf FROM artigopublicado;
SELECT codigo, nome, LENGTH(arquivo_pdf) as tamanho_pdf FROM livros;
````
