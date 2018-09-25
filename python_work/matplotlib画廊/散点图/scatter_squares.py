import matplotlib.pyplot as plt

"""散点图"""

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, s=40)

#设置每个坐标轴的取值范围
plt.axis = ([0, 1100, 0 , 1100000])

# plt.show()

plt.savefig('scatter1.png', bbox_inches='tight')
