# drehbarer-schnapsverteiler
Dieses Projekt dient einem wichtigen Zweck: Der zeitnahen und zügigen Versorgung der Altherren mit Sasse Sechser

## Aktueller Stand (15.02.2025):
- Teller dreht
- Pumpe pumpt
- Software läuft

## To Do:
- Pumpe ersetzen durch andere, die einen Schlauch in die Flasche einführt, statt komplett in der Flüssigkeit zu stehen. Das erleichtert den Wechsel auf eine andere Flüssigkeit
- Schickes Gehäuse bauen
- Kabel verlängern und sauber verlegen
- Rollenlager für Drehteller einbauen

## Pinbelegung Raspi:
Nr|GPIO|Funktion|Nr|GPIO|Funktion
|-----|-----|-----|-----|-----|-----|
|01|Power 3V||02|Power 5V|`PUMPE`|
|03|GPIO2|SDA I2C|04|Power 5V|`MOTOR`|
|05|GPIO3|SCL I2C|06|GND|`MOTOR`|
|07|GPIO4||08|GPIO14|`PUMPE`|
|09|GND|`PUMPE`|10|GPIO15||
|11|GPIO17|`MOTOR` IN1|12|GPIO18|`MOTOR` IN2|
|13|GPIO27|`MOTOR` IN3|14|GND||
|15|GPIO22|`MOTOR` IN4|16|GPIO23||
|17|Power 3V|`DISPLAY`|18|GPIO24|`DISPLAY` SCL|
|19|GPIO10|`DISPLAY` DC|20|GND||
|21|GPIO9|`DISPLAY` CS|22|GPIO25||
|23|GPIO11|`DISPLAY` RST|24|GPIO8||
|25|GND|`DISPLAY`|26|GPIO7|`DISPLAY` SDA|
|27||ID_SD|28||ID_SC|
|29|GPIO5||30|GND||
|31|GPIO6||32|GPIO12||
|33|GPIO13||34|GND||
|35|GPIO19||36|GPIO16||
|37|GPIO26||38|GPIO20||
|39|GND||40|GPIO21||

