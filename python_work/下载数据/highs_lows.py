import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	#读取第一行即文件头数据
	header_row = next(reader)
	
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	#获取每天最高气温
	dates, highs = [], []
	for row in reader:
		#最高气温
		highs.append(int(row[1]))
		#日期
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)

	print(highs)


#绘制图表
fig = plt.figure(figsize=(10, 6))
plt.plot(dates ,highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('' ,fontsize=24)
plt.ylabel('Temperature(F)', fontsize=16)

#绘制斜的标签
fig.autofmt_xdate()

plt.show()