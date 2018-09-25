bicycles = []			#创建空列表
bicycles = ['trek', 'cannondale', 'readline', 'specialized', 110]
print(bicycles)
print(bicycles[0].title())

#查
print(bicycles[-1])				#索引为负数时,代表获取列表倒数第几个元素,例如-1就是获取倒数第一个元素

#改
bicycles[-1] = "yamahu"			#修改列表中的某个元素

#增
bicycles.append("ducati")  		#append()在列表末尾添加元素(只能添加一个)
bicycles.insert(1,"suzuki")		#insert()插入元素到指定的位置

#删
del bicycles[0]					#del 删除列表中的某个元素
print(bicycles)
name = bicycles.pop(0)			#pop()从列表中删除某个元素并且返回这个元素的值,若不写索引则代表弹出最后一个元素
print(name)
print(bicycles)
name1 = bicycles.remove("yamahu") #根据元素的值删除该元素,并返回该元素(注意:若列表中该元素的值出现多次,只会删除第一个指定的值)
print(bicycles)
				

#永久性排序,即修改后无法恢复到原来的排列顺序
family_name = ['zhang', 'li', 'yue', 'wang', 'an', 'zan']
family_name.sort()				#sort()按字母顺序、或数字大小进行排序
print(family_name)

family_name.sort(reverse = True)		#sort(reverse=True)倒序
print(family_name)

#临时排序,即能够按特定的顺序显示列表元素,同时不影响列表
number = [5, 3, 9, 20]
new_number = sorted(number)			#sorted(列表名)临时排序,返回一个新列表
print(number)        #number未改变
print(new_number)

new_number = sorted(number,reverse = True)		#sorted(列表名,reverse = True)倒序
print(new_number)

'''
注意:在并分所有的值都是小写时，按字母顺序排序要复杂些。决定排列顺序时,有多种解读大些字母的方式。
	若首字母相同,原列表中排在前面的优先,而不是根据第二个字母
'''

#永久性反转列表元素
age = [1, 2, 3, 4]
age.reverse()
print(age)

#列表长度
lengh = len(age)
print(lengh)


