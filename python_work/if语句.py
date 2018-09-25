#1 条件测试
cars = ['audi', 'bmw', 'subaru', 'toyoka']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#数字
number = 25
if number == 25:
	print(1)


#布尔值
if True:
	print('false')
if False:
	print('false')

#2 检查特定的值是否包含在列表中
if 'toyoka' in cars:
	print('True')

names = []
if names:			#if 列表名-->判断列表是否为空
	print('list is not null')
else:
	print('list is null')


