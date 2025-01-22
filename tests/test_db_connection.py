from config.database import DatabaseConnection

def test_connection():
    db = DatabaseConnection()
    db.connect()  # Conecta ao banco
    if db.connection:
        print("Teste de conexão bem-sucedido!")
        db.disconnect()
    else:
        print("Falha no teste de conexão.")


if __name__ == "__main__":
    test_connection()
