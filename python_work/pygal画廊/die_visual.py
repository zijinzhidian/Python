import pygal

from die import Die


def analyze_results(results, die):
	"""分析结果，出现点数的次数"""
	frequencies = []
	#range从1开始到7结束,但不包含7
	for value in range(1, die.num_sides + 1):
		#列表中重复元素出现的次数
		frequency = results.count(value)
		frequencies.append(frequency)

	return frequencies


#创建一个骰子
die = Die()

results = []
for roll_number in range(1000):
	results.append(die.roll())

#出现频率
frequencies = analyze_results(results, die)


hist = pygal.Bar()

#图表标题
hist.title = "Results of rolling one D6 1000 times."
#x轴标题
hist.x_title = "Result"
#y轴标题
hist.y_title = "frequency of Result"
#x轴刻度内容
hist.x_labels = ["1", "2", "3", "4", "5", "6"]

hist.add('D6', frequencies)
hist.render_to_file('die_visual_svg')