import matplotlib.pyplot as plt

"""折线图"""

#y轴的值(未指定x轴时默认从0开始,(0,1),(2,4),...,(4,25))
squares = [1, 4, 9, 16, 25]

#x轴的值
input_valus = [1, 2, 3, 4, 5]

#设置坐标点和线条宽度(y轴的值为必选,其余的为可选)
plt.plot(input_valus, squares, linewidth=5, c='red')

#设置图表标题
plt.title("Square Number", fontsize=24)
#设置x轴标题
plt.xlabel("Value")
#设置y轴标题
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major' ,labelsize=14)

plt.show()
