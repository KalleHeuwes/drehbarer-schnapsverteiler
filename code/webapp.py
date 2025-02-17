from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>Pumpensteuerung</h1>
    <button onclick="fetch('/start')">Pumpe AN</button>
    <button onclick="fetch('/stop')">Pumpe AUS</button>
    '''

@app.route("/start")
def start_pumpe():
    subprocess.Popen(["sudo", "python3", "pumpe.py", "0"])
    return "Pumpe gestartet"

@app.route("/stop")
def stop_pumpe():
    subprocess.Popen(["sudo", "pkill", "-f", "pumpe.py"])
    return "Pumpe gestoppt"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
