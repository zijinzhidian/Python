#input()用户输入,接受一个参数用于输入提示
name = input("Please enter your name: ")
print('hello, ' + name + '!')

#int()字符串转
age = input("How old are you: ")
print(age)

#while循环不断地运行,直到指定的条件不满足为止
current_number = 0
while current_number < 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != "quit":
	message = input(prompt)
	if message != "quit":
		print(message)


#标志:Ture或者False
active = True
while active:
	message = input(prompt)
	if message == "quit":
		active = False
	else:
		print(message)