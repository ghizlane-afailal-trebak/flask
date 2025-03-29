from app import mysql

class Info:
    @staticmethod
    def add_info(user_id, data):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_info (user_id, data) VALUES (%s, %s)", (user_id, data))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_all_info():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT users.name, user_info.data FROM user_info JOIN users ON user_info.user_id = users.id")
        infos = cursor.fetchall()
        cursor.close()
        return infos
