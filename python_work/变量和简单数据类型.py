print("hello world")


message = "I love you "   
print(message)


print('Jack')    #字符串即可以用单引号,也可以用双印号

print(message.title())		#将每个单词的首字母改为大写
print(message.upper())		#将字符串改为全部大写
print(message.lower())		#将字符串改为全部小写
print(message.rstrip())		#去掉字符串末尾的空白
print(message.lstrip())		#去除字符串开头的空白
print(message.strip())		#去掉字符串两端的空白

print(len(message))         #len()获取字符串长度
print(message[:1])			#截取字符串

print(message + " " + "jack".title())    		#用'+'拼接字符串

print("\tPython")									#‘\t’制表符,可以连续使用
print("Language:\n\tPython\n\tSwift\n\n\tJava")		#'\n'换行符

print(3/2)					
print(2**3)					#两个**表示乘方运算,2的3次方等于8

print("Happy " + str(23) + "rd birthday")	#str()将非字符串转为字符串


