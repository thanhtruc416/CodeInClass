import traceback

import pymysql

from retail_project.models.customer import Customer

server ="localhost"
port =3306
database="k23416_retail"
user="root"
password="@Obama123"
try:
    conn =pymysql.connect(host=server,port=port,user=user,password=password,db=database)
except:
    traceback.print_exc()
#Câu 1: ăng nhaapk cho customer
def login_customer(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer WHERE Email='" + email + "' AND password='" + pwd + "'"
    cust = None
    cursor.execute(sql)
    dataset =cursor.fetchone()
    if dataset != None:
        cust=Customer(dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5])
        cust.ID, cust.Name, cust.Phone, cust.Email, cust.Password, cust.IsDelete = dataset
    cursor.close()
    return cust

cust=login_customer("daodao@gmail.com","123")
if cust==None:
    print('login failed')
else:
    print('login success')
    print(cust)
