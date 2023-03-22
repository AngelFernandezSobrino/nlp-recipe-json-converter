import pprint
from transformers import pipeline

generator = pipeline('text-generation', max_new_tokens=300, model='EleutherAI/gpt-neo-125M')

# Establecer el prompt
prompt = """
Añadir 2000 kg de agua y calentar a 35 grados

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

Una vez llenado, encender palas a 1000 rpm y turrax a 400 rpm durante 25 minutos

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

Encender la marina a 50 rpm y llenar por la boca de solidos con 100 kg de azucar

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

Al terminar subir la temperatura a 40 grados y poner palar a 1500 rpm, esperar 1 hora
"""



# Generar texto basado en el prompt
result = generator(prompt, do_sample=True)

# Imprimir el resultado generado
pprint.pp(result)

# Imprimir el texto generado
print(result[0]['generated_text'])