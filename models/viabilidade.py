from config.database import DatabaseConnection  # Importe a classe
from mysql.connector import Error

class Viabilitie:

    def latestViabilities():

        db = DatabaseConnection
        db.connect()

        try:

            sql = ""

        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            
