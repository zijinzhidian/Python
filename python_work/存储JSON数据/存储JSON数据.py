import json

filename = 'number.json'

numbers = [2, 3, 7, 11, 13]

#存储json数据
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

#读取json数据
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	print(numbers)

