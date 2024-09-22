from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)  # 创建 Flask 应用实例

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']  # 获取用户输入的文本
    return render_template('ex2.html', user_input=user_input)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == "__main__":
    app.run(debug=True)  # 运行应用
