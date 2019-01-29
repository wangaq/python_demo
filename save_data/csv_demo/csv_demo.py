# this is a sample demo
import csv
#
# with open('data.csv', 'w', encoding='utf-8') as csvfile:
#     w = csv.writer(csvfile)
#     w.writerow(['id','name','age','sex'])
#     w.writerow(['1','xiaoming','20','男'])
#     w.writerow(['2','xiaocia','20','女'])


# with open('data.csv', 'w', encoding='utf-8') as csvfile:
#     w = csv.writer(csvfile)
#     w.writerow(['id','name','age','sex'])
#     w.writerows([['1','xvxc','12','男'],['2','xvxc','33','男'],['3','cxccxvcxv','44','男'],['4','xvxvx','55','男']])


# newline 解决插入空行
# with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     fieldnames = ['id','name','age','sex']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"id":"1000","name":"张三","age":100,"sex":"男"})
#     writer.writerow({"id":"1001","name":"李四","age":100,"sex":"男"})
#     writer.writerow({"id":"1002","name":"张三","age":46,"sex":"男"})
#     writer.writerow({"id":"1003","name":"王五","age":33,"sex":"男"})
#     writer.writerow({"id":"1004","name":"张三","age":44,"sex":"男"})
#     writer.writerow({"id":"1005","name":"张三","age":89,"sex":"男"})
#     csvfile.close()

# with open('data.csv', 'a', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)



