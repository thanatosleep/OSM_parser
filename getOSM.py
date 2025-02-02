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
#Запрос составляется по координатам, в данном случае здесь Ольхонский район
#Можно указать дороги тоже

response = requests.get(overpass_API, params={'data': overpass_command})
data = response.json()

with open('olkhonFinal.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Файл успешно сохранен")
#по этому ресурсу выделил несколько типов туристической деятельности: 
#ЖИЛЬЕ
#hotel, camp_site(кемпинги), guest_house(не входит в hotel), wilderness_hut(дикие хижины), chalet(типа коттеджи)
#ОБЪЕКТЫ ИНТЕРЕСА
#attraction(природные объекты), information(доски, мб указатели), viewpoint(обзорки, кинотеатр один нашел даже), picnic_site(место для пикника), artwork, 
