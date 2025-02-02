import requests
import json

overpass_API = "http://overpass-api.de/api/interpreter"
overpass_command = """
[out:json][timeout:25];
node["tourism"](52.8, 106.8, 53.5, 107.8); 
out body;
>;
out skel qt;
"""

response = requests.get(overpass_API, params={'data': overpass_command})
data = response.json()

with open('olkhonFinal.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Файл успешно сохранен")