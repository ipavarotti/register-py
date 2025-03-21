import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', 3306),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'pw')
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def create_user(name, passwd, truename, email, passwd2):
    """Create a new user in the database using the stored procedure"""
    try:
        connection = get_db_connection()
        if connection is None:
            return False, "Database connection failed"
        
        cursor = connection.cursor()
        
        # Verificar se o nome de usuário já existe
        cursor.execute("SELECT COUNT(*) FROM users WHERE name = %s", (name,))
        if cursor.fetchone()[0] > 0:
            cursor.close()
            connection.close()
            return False, "O nome de usuário já existe"

        # Verificar se o endereço de e-mail já está em uso
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
        if cursor.fetchone()[0] > 0:
            cursor.close()
            connection.close()
            return False, "O endereço de e-mail já está em uso"
        
        cursor.execute("SELECT MAX(ID) FROM users")
        max_id_result = cursor.fetchone()
        user_id = (max_id_result[0] + 16) if max_id_result[0] is not None else 32

        cursor.callproc('adduser', (
            name,           # name1
            passwd,         # passwd1
            '',             # prompt1
            '',             # answer1
            truename,       # truename1
            '',             # idnumber1
            email,          # email1
            '',             # mobilenumber1
            '',             # province1
            '',             # city1
            '',             # phonenumber1
            '',             # address1
            '',             # postalcode1
            0,              # gender1
            '',             # birthday1
            '',             # qq1
            passwd2         # passwd21
        ))
        

        connection.commit()
         
        
        cursor.close()
        connection.close()
        
        return True, user_id
    except Error as e:
        print(f"Error creating user: {e}")
        return False, str(e)
