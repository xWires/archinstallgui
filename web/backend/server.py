from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/execute_command", methods=["POST"])
def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8'), 200
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8'), 500

@app.route("/launch_gparted", methods=["POST"])
def launch_gparted():
    return execute_command("gparted")

@app.route("/launch_cfdisk", methods=["POST"])
def launch_cfdisk():
    return execute_command("kitty cfdisk")

if __name__ == '__main__':
    app.run(debug=False, port=9091, host="127.0.0.1")