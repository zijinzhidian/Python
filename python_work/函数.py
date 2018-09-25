#1.无参的函数
def greet_user():
	print("Hello!")

#2.有参的函数
def greet_user_name(username):
	print("Hello " + username.title() + "!")

greet_user()
greet_user_name('jack')

#3.位置实参和关键字实参
def describe_pet(animal_type, animal_name):
	print("My " + animal_type + "'s name is " + animal_name)\

describe_pet("hamster", "Harry") #位置实参,实参和形参的位置需一致
describe_pet(animal_name="Harry", animal_type="hamster")  #关键字实参

#4.默认值,必须先列出没有默认值的形参
def describe_phone(phone_name, phone_type="Apple"):
	print("My " + phone_type + " is " + phone_name)

describe_phone("iPhoneX")
describe_phone("vivo8", "Adroid")

#5.返回值
def get_formatted_name(first_name, last_name):
	return first_name + " " + last_name

print(get_formatted_name("zhang", "san"))

#6.可选值(将可选的值默认为空字符串)
def get_formatted_name(first_name, last_name, middle_name = ""):
	if middle_name:
		return first_name + " " + middle_name + " " + last_name
	else:
		return first_name + " " + last_name

print(get_formatted_name("li", "si"))
print(get_formatted_name("wang", "wu", "lao"))

#7.传递列表
def greet_users(names):
	for name in names:
		print("Hello, " + name + "!")

greet_users(["zhangsan", "lisi"])

#8.传递任意数量的实参，toppings为元组名
def make_pizza(*toppings):
	for topping in toppings:
		print(topping)

make_pizza("pomato")
make_pizza("banana", "apple", "pear")

#9.结合使用位置实参和任意数量实参(即有些参数是必须要的，有些参数可有可无)
def make_cake(size, *toppings):
	print("Make a " + str(size) + "-inch cake need: ")
	for topping in toppings:
		print("- " + topping)

make_cake("12", "banana", "apple")

#10.任意数量的关键字实参,user_info为字典(相当于知道有些参数知道键，有些不知道)
def build_profile(name, **user_info):
	print("name: " + name)
	for key, value in user_info.items():
		print(key + ": " + value)

build_profile("yuewei", address="hunan", age="10")

