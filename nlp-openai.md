Convert the next recipe using following example of text converted to JSON format with the information about the recipe:

Añadir 2000 kg de agua y calentar a 35 grados
Una vez llenado, encender palas a 1000 rpm y turrax a 400 rpm durante 25 minutos
Encender la marina a 50 rpm y llenar por la boca de solidos con 100 kg de azucar
Al terminar subir la temperatura a 40 grados y poner palar a 1500 rpm, esperar 1 hora

[ 
{ "add_water": { "amount": 2000, "unit": "kg" }, 
"temperature": { "value": 35, "unit": "C" }, 
"palas": { "value": 0, "unit": "rpm" }, 
"turrax": { "value": 0, "unit": "rpm" }, "marina": { "value": 0, "unit": "rpm" } }, { "temperature": { "value": 35, "unit": "C" }, "palas": { "value": 1000, "unit": "rpm" }, "turrax": { "value": 400, "unit": "rpm" }, "marina": { "value": 0, "unit": "rpm" }, "time": { "value": 25, "unit": "min" } }, { "temperature": { "value": 35, "unit": "C" }, "palas": { "value": 1000, "unit": "rpm" }, "turrax": { "value": 400, "unit": "rpm" }, "marina": { "value": 50, "unit": "rpm" }, "solids": { "value": 100, "unit": "kg", "product": "azucar" } }]

Llenar con 1950 kg de agua y poner la temperatura a 38 grados
Al terminar poner palas a 1020 rpm y turrax a 800 rpm durante 60 minutos
Arrancar la marina a 100 rpm y añadir 20 kg de sal
Subir la temperatura a 60 ºC y cambiar palas a 900 rpm durante 2 horas y media
Detener todos los motores y esperar 1 hora

[ { "add_water": { "amount": 1950, "unit": "kg" }, "temperature": { "value": 38, "unit": "C" }, "palas": { "value": 0, "unit": "rpm" }, "turrax": { "value": 0, "unit": "rpm" }, "marina": { "value": 0, "unit": "rpm" } }, { "temperature": { "value": 38, "unit": "C" }, "palas": { "value": 1020, "unit": "rpm" }, "turrax": { "value": 800, "unit": "rpm" }, "marina": { "value": 0, "unit": "rpm" }, "time": { "value": 60, "unit": "min" } }, { "temperature": { "value": 38, "unit": "C" }, "palas": { "value": 1020, "unit": "rpm" }, "turrax": { "value": 800, "unit": "rpm" }, "marina": { "value": 100, "unit": "rpm" }, "solids": { "value": 20, "unit": "kg", "product": "sal" } }, { "temperature": { "value": 60, "unit": "C" }, "palas": { "value": 900, "unit": "rpm" }, "turrax": { "value": 800, "unit": "rpm" }, "marina": { "value": 100, "unit": "rpm" }, "time": { "value": 150, "unit": "min" } }, { "temperature": { "value": 60, "unit": "C" }, "palas": { "value": 0, "unit": "rpm" }, "turrax": { "value": 0, "unit": "rpm" }, "marina": { "value": 0, "unit": "rpm" }, "time": { "value": 60, "unit": "min" } }]