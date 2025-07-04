from database.DatabaseConnection import DatabaseConnection

db = DatabaseConnection()
conn = db.connect()

if conn:
    print("Conexão bem-sucedida com o banco!")
    db.disconnect()
else:
    print("Falha na conexão.")