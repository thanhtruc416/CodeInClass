#python -m pip install mysql-connector-python
import mysql.connector
import traceback
import pandas as pd
import pymysql


class Connector:
    def __init__(self,server="localhost", port=3306, database="k23416_retail", username="root", password="@Obama123"):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password
    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except:
            self.conn=None
            traceback.print_exc()
        return None

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()

            if not data:
                return pd.DataFrame()  # Trả về DataFrame rỗng nếu không có dữ liệu

            # Lấy tên cột từ cursor.description
            col_names = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(data, columns=col_names)
            cursor.close()
            return df
        except Exception as e:
            traceback.print_exc()
            return None
    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results=cursor.fetchall()
        tablesName=[]
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName
    def fetchone(self,sql,val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            dataset=cursor.fetchone()
            cursor.close()
            return dataset
        except:
            traceback.print_exc()
        return None
    def fetchall(self,sql,val):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            dataset=cursor.fetchall()
            cursor.close()
            return dataset
        except:
            traceback.print_exc()
        return None
    def insert_one(self,sql,val):
        cursor = self.conn.cursor()
        cursor.execute(sql, val)
        self.conn.commit()
        result =cursor.rowcount
        cursor.close()
        return result