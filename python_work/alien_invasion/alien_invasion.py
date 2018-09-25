import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏
	pygame.init()

	#游戏设置类
	ai_settings = Settings()

	#创建一个屏幕对象
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	#游戏名称(可选)
	pygame.display.set_caption("Alien Invasion")

	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	#创建计分牌
	sb = Scoreboard(ai_settings, screen, stats)

	#创建一艘飞船
	ship = Ship(screen, ai_settings)

	#创建一个用于存储子弹的编组(类似列表)
	bullets = Group()

	#创建一个用于存储外星人的空编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings, screen, aliens, ship)

	#开始游戏的主循环
	while True:
		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			#更新飞船
			ship.update()

			#更新子弹
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)

			#更新外星人
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

		#更新屏幕
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()