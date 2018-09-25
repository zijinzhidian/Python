import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	#一个对发射子弹进行管理的类

	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		#若传递过来的参数不需要全局使用,就不需要存储self.var = var
		self.screen = screen

		#创建一个rect对象
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		#调整位置
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor


	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)