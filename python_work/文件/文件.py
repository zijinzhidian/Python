filename = 'programming.txt'

#写入模式
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love create new games.\n")

#附加模式(若文件不存在会创建一个新文件,添加的内容不会覆盖原有内容)
with open(filename, 'a') as file_object:
	file_object.write("I also love English\n")

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)
