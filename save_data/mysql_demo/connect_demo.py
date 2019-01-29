import pymysql

db = pymysql.connect(host="127.0.0.1", user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('mysql version: ', data)

cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
