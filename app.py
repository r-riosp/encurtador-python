import string, random, sqlite3
# Importa a classe principal Flask do pacote que instalei (pip install)
from flask import Flask, request, jsonify, redirect, abort, send_from_directory

# Cria uma instância da aplicação web
app = Flask(__name__)

# função para facilitar a conexão com o banco
def get_db_connection():
    # Conecta ao arquivo do banco de dados
    conn = sqlite3.connect('database.db')
    # Permite acessar as colunas pelo nome
    conn.row_factory = sqlite3.Row
    return conn

# rota para encurtar o link
@app.route('/encurtar', methods=['POST'])
def encurtar_link():
    # 1. pega o JSON que o usuário mandou e extrai o link original
    link_original = request.json['link_original']

    # 2. Gera um código aleatório para o link
    # (implementação futura: verificar se o código já existe no banco)
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for i in range(7))

    # 3. Conecta no banco de dados
    conn = get_db_connection()

    # 4. Insere o novo link na rabela
    conn.execute('INSERT INTO links (link_original, codigo) VALUES (?, ?)',
                 (link_original, codigo))

    # 5. Salva as mudanças no banco
    conn.commit()

    # 6. Fecha a conexão
    conn.close()

    # 7. Retorna uma resposta de sucesso para o usuário
    link_curto = request.host_url + codigo
    return jsonify({'status': 'sucesso!', 'link_curto': link_curto}), 201

# Rota de Redirecionamento
@app.route('/<string:codigo>')
def redirecionar(codigo):
    # 1. Procura no banco o link com o código fornecido
    conn = get_db_connection()
    link = conn.execute('SELECT * FROM links WHERE codigo = ?', (codigo,)).fetchone()
    conn.close()

    # 2. Se o link existir, redireciona para o link original
    if link:
        return redirect(link['link_original'])
    # 3. Se não existir, mostra um erro 404 (Not Found)
    else:
        abort(404)


# Define uma rota. o "@" cria um "decorator"
# Isso significa que quando alguém acessar a página principal ('/' definida abaixo), a função será executada
@app.route('/')
def pagina_inicial():
    # Envia o arquivo index.html que está dentro da pasta 'static'
    return send_from_directory('static', 'index.html')

# Uma verificação padrão em Python,
# Só executa o que estiver dentro da condicional abaixo se eu rodar o arquivo diretamente
if __name__ == '__main__':
    # Roda o servidor de desenvolvimento do Flask.
    # debug=True faz o servidor reiniciar sozinho toda vez que alguma alteração for salva nos arquivos.
    app.run(debug=True)