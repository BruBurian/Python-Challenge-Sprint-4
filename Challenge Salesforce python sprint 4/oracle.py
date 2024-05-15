import oracledb 

# Função para conectar ao banco de dados Oracle
def conexao_com_oracle():
    connection = oracledb.connect("rm552863/050305@oracle.fiap.com.br:1521/orcl")
    return connection

# Funções CRUD
def insert_data(connection, table, data):
    cursor = connection.cursor()
    # Implemente a inserção de dados na tabela especificada
    cursor.close()

def update_data(connection, table, data):
    cursor = connection.cursor()
    # Implemente a atualização de dados na tabela especificada
    cursor.close()

def delete_data(connection, table, condition):
    cursor = connection.cursor()
    # Implemente a exclusão de dados da tabela especificada baseado na condição
    cursor.close()

def select_data(connection, table, condition=""):
    cursor = connection.cursor()
    # Implemente a consulta de dados na tabela especificada, opcionalmente com uma condição
    cursor.close()