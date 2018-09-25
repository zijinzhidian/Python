import matplotlib.pyplot as plt

from random_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))

#设置绘图窗口尺寸,单位为英寸
plt.figure(figsize=(10, 6))

#浅蓝色-->深蓝色进行颜色映射
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues ,s=15)

#绘制起点
plt.scatter(0, 0, c='red', s=100)
#绘制终点
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

#隐藏x轴
plt.axes().get_xaxis().set_visible(False)

#隐藏y轴
plt.axes().get_yaxis().set_visible(False)

plt.show()