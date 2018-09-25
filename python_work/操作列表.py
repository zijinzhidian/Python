#1 遍历列表
students = ["zhangsan", "lisi", "wangwu"]
for sudent_name in students:
	print(sudent_name.title() + '\tis' + '\tcute.')

#2 range()遍历数值
for value in range(-1, 5):    #range(a,b)从a开始，并到b结束(不包括b)
	print(value)

for x in range(0,10,2):      #range(a,b,c)从a开始,然后不断的加+c,直到达到或超过终值b(不包括b)
	print(x)

#3 list(range())创建数字列表
numbers = list(range(2, 5)) 
print(numbers)

#4 列表解析:将for循环和创建新元素的代码合并成一行,并自动附加新元素
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]  #列表解析[表达式 for 为表达式提供值]
print(squares)


#5 切片
traffics = ['bus', 'airplane', 'ship', 'bike', 'car', 'train']
print(traffics[1:3])   #[a:b]从第a个元素开始,到第b-1个元素(相当于不包含第b个元素)
print(traffics[1:])    #[a:]从第a个元素开始的所有元素
print(traffics[:3])	   #[:a]从第0个元素开始到第a-1个元素
print(traffics[-3:])   #[-a:]倒数a个元素

for traffic in traffics[2:5]:   #遍历列表切片
	print(traffic)

#6 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:];       
print(friend_foods)

#7 元组(不可变的列表称为元组)
dimensions = (200, 50)
# dimensions(0) = 250     #不能修改
for dimension in dimensions:  #遍历元组
	print(dimension)

#8 计算列表中重复元素出现的次数
numbers = [1, 2, 2, 3]
#列表中出现2的次数
num_same = numbers.count(2)
print(num_same)


#9 enumerate()获取每个元素的索引及其值
teachers = ['zhangsan', 'lisi', 'wangwu']
for index, name in enumerate(teachers):
    print(index, name)
