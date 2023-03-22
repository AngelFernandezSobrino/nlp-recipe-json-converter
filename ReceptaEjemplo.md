Añadir 2000 kg de agua y calentar a 35 grados

```json
{
    "add_water": {
        "amount": 2000,
        "unit": "kg"
    },
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 0,
        "unit": "rpm"
    },
    "turrax": {
        "value": 0,
        "unit": "rpm"
    },
    "marina": {
        "value": 0,
        "unit": "rpm"
    }
}
```

Una vez llenado, encender palas a 1000 rpm y turrax a 400 rpm durante 25 minutos

```json
{
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 1000,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 0,
        "unit": "rpm"
    },
    "time": {
        "value": 25,
        "unit": "min"
    }
}
```

Encender la marina a 50 rpm y llenar por la boca de solidos con 100 kg de azucar

```json
{
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 1000,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 50,
        "unit": "rpm"
    },
    "solids": {
        "value": 100,
        "unit": "kg",
        "product": "azucar"
    }
}
```

Al terminar subir la temperatura a 40 grados y poner palar a 1500 rpm, esperar 1 hora

```json
{
    "temperature": {
        "value": 40,
        "unit": "C"
    },
    "palas": {
        "value": 1500,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 50,
        "unit": "rpm"
    },
    "time": {
        "value": 1,
        "unit": "h"
    }
}
```

Bajar palas a 200 rpm, y turrax a 100 rpm, apagar la marina y proceder con la descarga

```json
{
    "temperature": {
        "value": 40,
        "unit": "C"
    },
    "palas": {
        "value": 200,
        "unit": "rpm"
    },
    "turrax": {
        "value": 100,
        "unit": "rpm"
    },
    "marina": {
        "value": 0,
        "unit": "rpm"
    }
}
```





Una ejemplo de instrucciones podria ser:

Añadir 2000 kg de agua y calentar a 35 grados
Una vez llenado, encender palas a 1000 rpm y turrax a 400 rpm durante 25 minutos
Encender la marina a 50 rpm y llenar por la boca de solidos con 100 kg de azucar
Al terminar subir la temperatura a 40 grados y poner palar a 1500 rpm, esperar 1 hora

A partir de las cuales necesito generar el siguiente resultado:

[
{
    "add_water": {
        "amount": 2000,
        "unit": "kg"
    },
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 0,
        "unit": "rpm"
    },
    "turrax": {
        "value": 0,
        "unit": "rpm"
    },
    "marina": {
        "value": 0,
        "unit": "rpm"
    }
},
{
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 1000,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 0,
        "unit": "rpm"
    },
    "time": {
        "value": 25,
        "unit": "min"
    }
},
{
    "temperature": {
        "value": 35,
        "unit": "C"
    },
    "palas": {
        "value": 1000,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 50,
        "unit": "rpm"
    },
    "solids": {
        "value": 100,
        "unit": "kg",
        "product": "azucar"
    }
},
{
    "temperature": {
        "value": 40,
        "unit": "C"
    },
    "palas": {
        "value": 1500,
        "unit": "rpm"
    },
    "turrax": {
        "value": 400,
        "unit": "rpm"
    },
    "marina": {
        "value": 50,
        "unit": "rpm"
    },
    "time": {
        "value": 1,
        "unit": "h"
    }
}
]