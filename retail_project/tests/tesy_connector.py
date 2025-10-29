import traceback

import pymysql

server ="localhost"
port =3306
database="k23416_retail"
user="root"
password="@Obama123"
try:
    conn =pymysql.connect(host=server,port=port,user=user,password=password,db=database)
except:
    traceback.print_exc()
print("Mò được mặt xuống là thành công")
#Câu 1: ăng nhaapk cho customer
def login_customer(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer WHERE Email='" + email + "' AND password='" + pwd + "'"
    cursor.execute(sql)
    print(sql)
    dataset =cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("lỗi")
    cursor.close()
login_customer("daodao@gmail.com","123")

def login_employee(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE Email = %s AND password = %s"
    val = (email,pwd)
    cursor.execute(sql,val)
    print(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("lỗi")
    cursor.close()
login_employee("putin@gmail.com","123")