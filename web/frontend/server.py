from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, port=9090, host="127.0.0.1")