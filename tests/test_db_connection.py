from database.config import create_connection

def test_connection():
    connection = create_connection()
    if connection:
        print("Teste de conexão bem-sucedido!")
        connection.close()
    else:
        print("Falha no teste de conexão.")

if __name__ == "__main__":
    test_connection()
