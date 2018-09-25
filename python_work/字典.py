#创建字典
students = {'zhangsan' : 15 ,'lisi' : 12}

#查
age = students["lisi"]   #访问字典中的值
print('The age of zhangsan is' + ' ' + str(students['zhangsan']) + '.')

#增
students['wangwu'] = 25
print(students)

#改
students['zhangsan'] = 16
print(students)

#删
del students['lisi']
print(students)


user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
	}

#items()返回字典的所有键-值
for key, value in user_0.items():
	print('\nkey:' + key)
	print('value:' + value)

#keys()返回字典的所有键
for key in user_0.keys():   #等同于for key in user_0:
	print('\nkey:' + key)

#values()返回字典的所有值
for value in user_0.values():
	print('\nvalue:' + value)

#sorted()按顺序遍历字典的键或值
for key in sorted(user_0.keys()):
	print(key)

#set()返回一个去重的列表
for value in set(user_0.values()):
	print(value)


