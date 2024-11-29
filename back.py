import mysql.connector
from mysql.connector import Error,connect,connection
import requests


def conexao_db():

    try:
        conexao= mysql.connector.connect(
            host="localhost",
            user="root",
            password="853227",
            db="meu_site"
        )
        print('Conexão ao banco de dados bem-sucedida!')
        return conexao
    except Error as e:
        print(f"Erro ao tentar conectar ao banco de dados: {e}")
        return None

def inserir_dados(nome,email,telefone,mensagem):
    print(f"Tentando inserir dados: {nome}, {email}, {telefone}, {mensagem}")
    conexao= conexao_db()
    if conexao:

        query= 'INSERT INTO contato (nome,email,telefone,mensagem) VALUES (%s,%s,%s,%s)'
        cursor= conexao.cursor()

        try:
            cursor.execute(query,(nome,email,telefone,mensagem))
            conexao.commit()
            print('dados inseridos com sucesso!')
            return True
        
        except Error as e:
            print(f'Dados não inseridos na base. Erro: {e}')

        finally:
            cursor.close()
            conexao.close()
    else:
        print('conexão com o banco de dados não estabelecida!')
        return False


