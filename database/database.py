from database.DatabaseConnection import DatabaseConnection

def get_db_connection():
    db = DatabaseConnection()
    return db.connect()

def create_tables():
    pass

