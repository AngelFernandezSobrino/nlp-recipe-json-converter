import spacy
import json

nlp = spacy.load("es_core_news_md")

def process_sentence(sentence):
    doc = nlp(sentence)

    output = {
        "temperature": {
            "value": None,
            "unit": "C"
        },
        "palas": {
            "value": None,
            "unit": "rpm"
        },
        "turrax": {
            "value": None,
            "unit": "rpm"
        },
        "marina": {
            "value": None,
            "unit": "rpm"
        }
    }

    for token in doc:
        if token.pos_ == "NUM":
            if token.dep_ == "nummod" and token.head.text == "kg":
                output["add_water"] = {
                    "amount": float(token.text),
                    "unit": "kg"
                }
            elif token.dep_ == "nummod" and token.head.text == "minutos":
                output["time"] = {
                    "value": int(token.text),
                    "unit": "min"
                }
            else:
                output["temperature"]["value"] = int(token.text)
        elif token.text == "kg" and token.dep_ == "quantmod":
            output["solids"] = {
                "value": int(doc[token.i-1].text),
                "unit": "kg",
                "product": doc[token.i+1].text
            }
        elif token.text == "palas" and token.dep_ == "ROOT":
            output["palas"]["value"] = int(doc[token.i-1].text)
        elif token.text == "turrax" and token.dep_ == "ROOT":
            output["turrax"]["value"] = int(doc[token.i-1].text)
        elif token.text == "marina" and token.dep_ == "ROOT":
            output["marina"]["value"] = int(doc[token.i-1].text)

    return output

if __name__ == "__main__":
    sentence = "Encender la marina a 50 rpm y llenar por la boca de solidos con 100 kg de azucar"
    print(json.dumps(process_sentence(sentence), indent=4))
