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
        except Error as e: