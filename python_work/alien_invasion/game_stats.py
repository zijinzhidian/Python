class GameStats():
	"""跟踪游戏的统计信息"""

	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False

		#在任何情况下都不应该重置最高得分
		self.high_score = self.get_high_score()

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		#剩余飞船命数
		self.ships_left = self.ai_settings.ship_limit
		#所得分数
		self.score = 0
		#玩家等级
		self.level = 1


	def get_high_score(self):
		"""获得最高得分记录"""
		filename = 'score.txt'
		with open(filename) as file_object:
			return int(file_object.read())