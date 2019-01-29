import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students'

cursor.execute(sql)
print(cursor.rowcount)

# one = cursor.fetchone()
# print(one)

all = cursor.fetchall()
print(all)

for one in all:
    print(one)