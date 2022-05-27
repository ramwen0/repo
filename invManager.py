import pymysql

connection = pymysql.connect(host="localhost", user="root", passwd="", database='localhost')
cursor = connection.cursor()

connection.commit()
connection.close()
