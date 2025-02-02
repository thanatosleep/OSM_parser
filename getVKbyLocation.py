import requests 
import json

tokenVK = 'PLACE_YOUR_TOKEN_HERE'
lat = 52.8
long = 106.8
radius = 50000
#sort - по лайкам не работает почему-то, отображется только одна запись
#q - строка поиска, типа природа, байкал (ключевое слово)
#extended - 1, возращает расширенный формат данных, лайки и просмотры тоже

url = f'https://api.vk.com/method/photos.search?lat={lat}&long={long}&radius={radius}&extended=1&access_token={tokenVK}&v=5.199'
response = requests.get(url)
data = response.json()

def sortByData(item):
    """ Функция сортирует данные по лайкам и просмотрам.
    
    """
    likes = item.get('likes', {}).get('count', 0)
    views = item.get('views', 0)
    return(likes, views)

if 'response' in data and 'items' in data['response']:
    sorted_items = sorted(data['response']['items'], key=sortByData, reverse=True)
    
    with open('vkDataSortedOlkhon.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_items, f, ensure_ascii=False, indent=4)
        
    print("Файл успешно сохранен")
else:
    print("Не хватает данных")
