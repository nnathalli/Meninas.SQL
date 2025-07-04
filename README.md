# Meninas.SQL – Projeto Final de Banco de Dados

Este repositório contém o sistema desenvolvido para o projeto Meninas.SQL, que visa organizar os dados do projeto Meninas.comp da UnB, utilizando banco de dados PostgreSQL, interface gráfica e persistência com Python.

# Sobre o Projeto Meninas.comp

O projeto Meninas.comp incentiva a participação de meninas nas áreas de computação e tecnologia. Este sistema tem como objetivo armazenar, consultar e manter dados das alunas, professoras, atividades, produtos e parcerias.

# Integrantes

* Maria Eduarda Pacheco Ferreira de Freitas – 221003977
* Sara Lima Gaspar – 221017121
* Pedro Maia de Oliveira Evangelista – 232005951
* Náthalli de Oliveira Maciel – 221018970

# Licença

Este projeto é acadêmico, sem fins lucrativos, e tem fins exclusivamente educacionais.

# Requisitos

- Python 3.10+
- PostgreSQL 15+
- Biblioteca: 'psycopg2-binary'

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

...
