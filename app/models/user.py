from app import mysql
import bcrypt

class User:
    @classmethod
    def create_user(cls, name, email, password):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                      (name, email, password))
        mysql.connection.commit()
        cursor.close()

    @classmethod
    def get_user_by_email(cls, email):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

    @classmethod
    def get_user_by_id(cls, user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user