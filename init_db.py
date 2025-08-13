import sqlite3

# Abre uma conexão com o banco de dados (isso cria um arquivo database.db)
connection = sqlite3.connect('database.db')

# Abre o arquivo schema.sql
with open('schema.sql') as f:
    # Executa o script SQL que está dentro do arquivo
    connection.executescript(f.read())

# Fecha a conexão
connection.close()