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
        if e.returncode != 32:
            return e.output.decode('utf-8'), 500
        else:
            return result.decode('utf-8'), 200

@app.route("/launch_gparted", methods=["POST"])
def launch_gparted():
    return execute_command("gparted")

@app.route("/format_disk", methods=["POST"])
def launch_cfdisk():
    data = request.json
    boot_partition = data.get("boot_partition")
    root_partition = data.get("root_partition")
    return execute_command(f"umount -q {boot_partition}; umount -q {root_partition}; mkfs.ext4 -qF {root_partition}; mkfs.fat -F 32 {boot_partition}; mount --mkdir {root_partition} /mnt; mount --mkdir {boot_partition} /mnt/boot")

if __name__ == '__main__':
    app.run(debug=False, port=9091, host="127.0.0.1")