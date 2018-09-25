# 1.导入整个模块
import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

#2.导入指定的函数,多个用分号分开
from pizza import make_pizza

make_pizza(13,"banana")

#3.as重命名函数名
from pizza import make_pizza as mp

mp(12, "apple")

#4.as重命名模块名
import pizza as p

p.make_pizza(14, "apple")