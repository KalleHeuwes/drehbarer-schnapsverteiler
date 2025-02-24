import time
import datetime
import sys
import subprocess

if __name__ == "__main__":
    anzahlPinnchen = int(sys.argv[1])
    fuellmenge = float(sys.argv[2])
    fuelldauer = fuellmenge / 10

def log(inText):
    c = datetime.datetime.now()
    current_time = c.strftime('%H:%M:%S')
    print(current_time + " " + inText)
    
try:
       
    for x in range(anzahlPinnchen):
        log(f"Befülle Pinnchen {x + 1} mit {fuellmenge} ml für {fuelldauer} Sekunden ...")
        subprocess.run(["python3", "pumpe.py", f"{fuelldauer}"])    # Pumpfunktion in Extrascript ausgelagert, da die Pumpe sonst durchgehend läuft
        subprocess.run(["python3", "motorsteuerung.py", f"{int(512/ anzahlPinnchen)}"])                     # 512 Schritte = ca. eine Umdrehung
        
finally:
    log("Programmende !")
