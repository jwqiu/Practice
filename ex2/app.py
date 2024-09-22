from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)  # 创建 Flask 应用实例

@app.route("/")
def home():
    return render_template("surveytxt.html")

if __name__ == "__main__":
    app.run(debug=True)  # 运行应用