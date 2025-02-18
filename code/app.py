from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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
