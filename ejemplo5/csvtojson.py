import csv
import json

# Abre el CSV en modo lectura
csv_file = open("atp_tennis.csv", encoding="latin-1", newline="")
reader = csv.DictReader(csv_file)

# Lista de documentos
docs = []
for fila in reader:
    docs.append(fila)

csv_file.close()

# Crea el JSON con la estructura {"docs": [...]}
json_file = open("atp_tennis.json", "w", encoding="utf-8")
json.dump({"docs": docs}, json_file, ensure_ascii=False, indent=4)
json_file.close()

print("Creado atp_tennis.json con", len(docs), "documentos")
