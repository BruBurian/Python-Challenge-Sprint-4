import oracledb

def conectar():
    return oracledb.connect("rm552863/050305@oracle.fiap.com.br:1521/orcl")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE usuarios (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY,
            nome_empresa VARCHAR2(255),
            email VARCHAR2(255) UNIQUE,
            senha VARCHAR2(255),
            PRIMARY KEY (id)
        )
        """)
        conn.commit()
        print("Tabela 'usuarios' criada com sucesso.")
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 955:
            print("Tabela 'usuarios' já existe.")
        else:
            print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    criar_tabela()
