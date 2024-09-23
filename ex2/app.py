from flask import Flask, render_template,request
from datetime import datetime
import mysql.connector
import connect as connect # 假设这个模块里定义了 dbuser, dbpass, dbhost, dbname

app = Flask(__name__)  # 创建 Flask 应用实例



connection=mysql.connector.connect(
    host=connect.dbhost,
    user=connect.dbuser,
    password=connect.dbpass,
    database=connect.dbname,
)

cursor=connection.cursor()
cursor.execute('SELECT name,email,prize FROM customers;')
customers=cursor.fetchall()

cursor.close()  # 关闭游标
connection.close()  # 关闭数据库连接


@app.route("/")
def home():
    return render_template("surveytxt.html",customers=customers)


if __name__ == "__main__":
    app.run(debug=True)  # 运行应用










# dbconn = None
# connection = None

# def getCursor():
#     global dbconn
#     global connection
#     connection = mysql.connector.connect(user=connect.dbuser, \
#     password=connect.dbpass, host=connect.dbhost, \
#     database=connect.dbname, autocommit=True)
#     dbconn = connection.cursor()
#     return dbconn

# @app.route("/")
# def home():
#     return render_template("base.html")

# @app.route("/listbooks")
# def listbooks():
#     connection = getCursor()
#     connection.execute("SELECT * FROM books;")
#     bookList = connection.fetchall()
#     print(bookList)
#     return render_template("booklist.html", booklist = bookList)   