from flask import Flask,render_template,request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Jwqiu475715529',
        database='jd'
    )

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/list",methods=["GET"])
def list():            
    username=request.args.get("username")
    db=get_db_connection()
    cursor=db.cursor()
    query="SELECT id,username,password FROM users"
    cursor.execute(query)
    users=cursor.fetchall()
    cursor.close()
    db.close()

    return render_template("hello_list.html",username=username,users=users)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/submit",methods=["POST"])
def submit():

    username=request.form["username"]
    password=request.form["password"]
    db=get_db_connection()
    cursor=db.cursor()
    sql="INSERT INTO users(username,password) VALUES(%s,%s)"
    val=(username,password)
    cursor.execute(sql,val)
    db.commit()
    cursor.close()
    db.close()
    return redirect("/list")

@app.route("/delete/<id>",methods=['POST'])
def delete_user(id):
    db=get_db_connection()
    cursor=db.cursor()
    sql="DELETE FROM users WHERE id=%s"
    cursor.execute(sql,(id,))
    db.commit()
    return redirect('/list')

@app.route("/edit/<id>",methods=["GET"])
def edit(id):
    db=get_db_connection()
    cursor=db.cursor()
    sql="SELECT id,username,password FROM users where id=%s"
    cursor.execute(sql,(id,))
    person=cursor.fetchone()
    cursor.close()
    db.close()
    return render_template("edit.html",person=person)

@app.route("/update/<id>",methods=["POST"])
def update(id):
    db=get_db_connection()
    cursor=db.cursor()
    username=request.form["username"]
    password=request.form["password"]

    sql="UPDATE users SET username=%s,password=%s where id=%s"
    cursor.execute(sql,(username,password,id))
    db.commit()
    cursor.close()
    db.close()
    return redirect('/list')


if __name__ == "__main__":
    app.run(debug=True)