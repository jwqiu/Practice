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

@app.route("/submit",methods=["POST","GET"])
def submit():
    username=None
    if request.method=="POST":
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
            
    db=get_db_connection()
    cursor=db.cursor()
    query="SELECT username,password FROM users"
    cursor.execute(query)
    users=cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("hello_list.html",username=username,users=users)

@app.route("/delete/<username>",methods=['POST'])
def delete_user(username):
    db=get_db_connection()
    cursor=db.cursor()
    sql="DELETE FROM users WHERE username=%s"
    cursor.execute(sql,(username,))
    db.commit()
 
    return redirect('/submit')


if __name__ == "__main__":
    app.run(debug=True)