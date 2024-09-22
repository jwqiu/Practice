from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)  # 创建 Flask 应用实例

@app.route("/")
def home():
    return render_template("ex1.html")

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']  # 获取用户输入的文本
    return render_template('ex2.html', user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)  # 运行应用