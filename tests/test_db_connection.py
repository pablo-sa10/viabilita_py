from config.database import connect

def test_connection():
    db = DatabaseConnection()
    connection = db.connect()  # Você usa o método connect() da instância de DatabaseConnection
    if connection:
        print("Teste de conexão bem-sucedido!")
        connection.close()
    else:
        print("Falha no teste de conexão.")

if __name__ == "__main__":
    test_connection()
