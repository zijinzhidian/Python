class Dog():

	def __init__(self, name, age):
		#初始化属性
		self.name = name
		self.age = age
		#属性默认值
		self.sex = "male"
	
	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over.")

	#修改属性的值
	def update_odometer(self, new_age):
		if new_age < 100:
			self.age = new_age

#创建对象 
my_dog = Dog('willie', 6)

#调用属性
print("My dog's name is " + my_dog.name.title() + ".")
#调用默认属性值
print(my_dog.sex)
#修改属性的值
my_dog.update_odometer(45)
my_dog.update_odometer(100)
print(str(my_dog.age))

#调用方法
my_dog.sit()
my_dog.roll_over()


#继承
class Sub_dog(Dog):

	def __init__(self, name, age):
		super().__init__(name, age)

your_dog = Sub_dog("Tesla", 10)
your_dog.sit()

```
#导入单个类
from 文件名 import 类名
#导入多个类
form 文件名 import 类名, 类名, ......
#导入整个模块
```
	