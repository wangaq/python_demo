import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

# sql = 'insert into students(name, age) values (%s, %s)'
#
# try:
#     cursor.execute(sql, ('张三',20))
#     db.commit()
# except:
#     db.rollback()
# db.close()

data = {
    'name':'liujn',
    'age':120
}

tableName = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'insert into {table}({keys}) values ({values})'.format(table=tableName, keys=keys, values=values)
print('sql: ', sql)

try:
    print(data.values())
    print(tuple(data.values()))

    if cursor.execute(sql, tuple(data.values())):
        print('success!!')
        db.commit()
except:
    db.rollback()
db.close()


