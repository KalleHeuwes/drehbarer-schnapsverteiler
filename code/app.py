from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/verarbeite", methods=["POST"])
def verarbeite():
    data = request.get_json()
    schrittweite = data.get("schrittweite", "Keine Daten erhalten")
    return jsonify({"empfangen": schrittweite})
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/motor_rechts")
def motor_rechts():
    subprocess.Popen(["sudo", "python3", "motorsteuerung.py", "12"])
    return "Motor 12 rechts"
    
@app.route("/motor_links")
def motor_links():
    subprocess.Popen(["sudo", "python3", "motorsteuerung.py", "-12"])
    return "Motor 12 links"
    
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
