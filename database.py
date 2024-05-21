import oracledb
import json

def conectar():
    return oracledb.connect("rm552863/050305@oracle.fiap.com.br:1521/orcl")

def cadastrar_usuario(nome_empresa, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO usuarios (nome_empresa, email, senha)
        VALUES (:1, :2, :3)
        """, (nome_empresa, email, senha))
        conn.commit()
    except oracledb.DatabaseError as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome_empresa, email FROM usuarios")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def alterar_usuario(id, nome_empresa, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE usuarios
    SET nome_empresa = :1, email = :2, senha = :3
    WHERE id = :4
    """, (nome_empresa, email, senha, id))
    conn.commit()
    cursor.close()
    conn.close()

def excluir_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = :1", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_por_email(email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = :1", (email,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def consultar_por_empresa(nome_empresa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome_empresa LIKE :1", ('%' + nome_empresa + '%',))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def exportar_para_json(dados, filename):
    with open(filename, 'w') as file:
        json.dump(dados, file, indent=4)
