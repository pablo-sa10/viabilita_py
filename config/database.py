import mysql.connector
from mysql.connector import error
from dotenv import load_dotenv
import os

# carrega as variaveis de ambiente do .env
load_dotenv()

class DatabaseConnection:

    def __init__(self):
        """ INICIALIZA A CLASSE E DEFINE OS PARAMETRO PARA A CONEXAO """
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.connection = None

    def connect(self):
        """ ESTABELECE A CONEXAO COM O BANCO DE DADOS """
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database,
            )

            if self.connection.is_connected():
                print("Conexão com o banco de dados estabelecida!")

        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def disconnect(self):
        """ FECHA A CONEXAO COM O BANCO DE DADOS """
        if not self.connection or not self.connection.is_connected():
            print("Sem conexao ativa com o banco de dados.")
            self.connection.close()
            print("Conexao com o banco de dados")

    def execute_query(self, query, params = None):
        """ EXECUTA UMA CONSULTA SQL """
        if not self.connection