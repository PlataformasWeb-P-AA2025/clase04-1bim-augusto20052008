# upload_without_bulk.py

import requests
import json

# Carga los datos desde el JSON generado
with open('atp_tennis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Todos los documentos
docs = data['docs']

# Configuración de la base CouchDB
base_datos = "personas005"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Inserta documento por documento
for doc in docs:
    resp = requests.post(url, headers=headers, json=doc)
    if resp.status_code in (201, 202):
        print(f"Creado: {resp.json().get('id')}")
    else:
        print(f"Error {resp.status_code}: {resp.text}")
