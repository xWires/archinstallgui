from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")

@app.route("/disks", methods=["GET"])
def disks_page():
    return render_template("disks.html")

if __name__ == '__main__':
    app.run(debug=False, port=9090, host="127.0.0.1")