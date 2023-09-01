import pymysql

conn = pymysql.connect(
    host="your_mysql_host",
    user="your_mysql_username",
    password="your_mysql_password",
    database="your_database_name",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """CREATE TABLE autos (
    id_auto integer PRIMARY KEY AUTO_INCREMENT,
    id_parking integer NOT NULL,
    matricule text NOT NULL,
)"""

cursor.execute(sql_query)
conn.close()
