import psycopg2

def load_sql_file(filepath, db_params):

    # Conectando ao banco de dados
    conn = psycopg2.connect(
        host=db_params['host'],
        database=db_params['database'],
        user=db_params['user'],
        password=db_params['password']
    )

    conn.autocommit = True
    cursor = conn.cursor()

    # Lendo e executando o arquivo SQL
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)

    cursor.close()
    conn.close()
    print("Arquivo SQL carregado com sucesso!")

# Parâmetros de conexão
db_params = {
    'host': 'dpg-ct0u9qu8ii6s73facj80-a.oregon-postgres.render.com',
    'database': 'teste_python',
    'user': 'teste_python_user',
    'password': '4S7UvH4NQtDd3cF1eF5yIFwAhJ5hbHXZ'
}


# Caminho para o arquivo SQL
filepath = 'persons.sql'

# Carregando o arquivo
load_sql_file(filepath, db_params)
