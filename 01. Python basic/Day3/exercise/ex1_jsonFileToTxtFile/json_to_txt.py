import json

f1 = open('mc.json', 'r')
f2 = open('output.txt', 'w')

json_data = f1.read()
data = json.loads(json_data)

# 1. window 객체에서 key만 모두 파일에 출력
window_keys = data['widget']['window'].keys()
w = f2.write(' '.join(window_keys) + '\n')

# 2. image 객체에서 value만 모두 파일에 출력
image_values = data['widget']['image'].values()
w = f2.write(' '.join(str(value) for value in image_values) + '\n')

# 3. text 객체에서 key, value 모두 출력하기
text_items = data['widget']['text'].items()
for item in text_items:
    w = f2.write(''.join(f"('{item[0]}', '{item[1]}') "))

f2.close()
f1.close()
