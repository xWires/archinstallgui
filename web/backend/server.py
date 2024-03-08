from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/execute_command', methods=['POST'])
def execute_command():
    try:
        data = request.json
        command = data.get('command')
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8'), 200
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8'), 500

if __name__ == '__main__':
    app.run(debug=False, port=9091, host="127.0.0.1")