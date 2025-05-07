# upload_with_bulk.py

import requests
import json

# Cargar datos desde el JSON generado
with open('atp_tennis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filas a subir
docs = data['docs']

# Configuración de CouchDB
base_datos = "personas005"
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Prepara el payload y envía en un solo lote
payload = {'docs': docs}
response = requests.post(url, headers=headers, json=payload)

# Muestra el resultado
print("Estado:", response.status_code)
print(response.json())
