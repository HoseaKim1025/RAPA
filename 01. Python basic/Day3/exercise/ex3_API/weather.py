import requests
import json
from pprint import pprint

API_KEY = '7df3344c668299d1c0b61225ff5f058b'

# # 1. 위/경도로 요청
# lat = 37.56
# lon = 126.97
# URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

# 2. 도시 이름으로 요청
city = 'Seoul,KR'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

# 데이터 추출
data = requests.get(URL).json()
# pprint(data)

# 섭씨 온도 출력
temp_k = data['main']['temp']
temp_c = temp_k - 273.15
print(f'캘빈 온도: {temp_k}K')
print(f'섭씨 온도: {temp_c:.2f}˚C')

# 날씨에 대한 설명 출력
description = data['weather'][0]['description']
print(f'날씨 설명: {description}')