import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	"""监听键盘和鼠标事件"""
	for event in pygame.event.get():
		#退出事件
		if event.type == pygame.QUIT:
			save_high_score(stats)
			sys.exit()

		#按下按键事件
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, stats, screen, ship, bullets)

		#松开按键事件
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

		#鼠标点击事件
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, stats, screen, ship, bullets):
	"""响应按下"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#创建一颗子弹,并加入到编组中
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		save_high_score(stats)
		sys.exit()


def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	"""单击Play按钮时开始游戏"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:

		#隐藏光标
		pygame.mouse.set_visible(False)

		#重置游戏设置
		ai_settings.initialize_dynamic_settings()

		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True

		#重置计分牌图案
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人,并让飞船居中
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	"""更新屏幕,并切换到新的屏幕"""
	#设置屏幕背景颜色
	screen.fill(ai_settings.bg_color)
	#绘制飞船
	ship.blitme()
	#重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#重绘所有外星人
	aliens.draw(screen)

	#显示得分
	sb.show_score()

	#如果游戏处于非活动状态,绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()


	#让最近绘制的屏幕可见
	pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新子弹的位置,并删除已消失的子弹"""

	#更新子弹(编组里面的所有子弹都会调用update方法)
	bullets.update()
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collosions(ai_settings, screen, stats, sb, ship, aliens, bullets)
		

def check_bullet_alien_collosions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""响应子弹外星人的碰撞"""

	#删除被子弹击中的外星人及相应的子弹
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	#统计得分
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	#若外星人群被消灭完,删除现有的子弹并新建一群外星人
	if len(aliens) == 0:
		bullets.empty()
		#提高游戏难度
		ai_settings.increase_speed()

		#提高等级
		stats.level += 1
		sb.prep_level()

		#创建一群新的外星人
		create_fleet(ai_settings, screen, aliens, ship)


def create_fleet(ai_settings, screen, aliens, ship):
	"""创建外星人群"""
	#创建一个外星人,该外星人不加入编组中
	alien = Alien(ai_settings, screen)

	#每行的外星人个数
	number_aliens_x = get_number_aline_x(ai_settings, alien.rect.width)
	#外星人行数
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	#创建一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aline_x(ai_settings, alien_width):
	"""计算每行可容纳多少个外星人"""

	#有效空间
	available_space_x = ai_settings.screen_width - 2 * alien_width
	#每行的外星人数量
	number_aliens_x = int(available_space_x / (2 * alien_width))

	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""创建一个外星人并放在当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x 
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算屏幕可容纳多少行外星人"""

	available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
	number_rows = int (available_space_y / (2 * alien_height))

	return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""更新外星人群中所有外星人的位置"""
	aliens.update()
	check_fleet_edges(ai_settings, aliens)

	#检测外星人和飞船是否碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		print("Ship hit!")
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

	#检测是否有外星人到达屏幕底端
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def check_fleet_edges(ai_settings, aliens):
	"""当有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""将整群外星人向下移,并改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""响应外星人撞到飞船"""

	if stats.ships_left > 0:
		#将剩余飞船减1
		stats.ships_left -= 1

		#更新计分牌
		sb.prep_ships()

		#晴空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人,并将飞船放到屏幕底端中央
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()

		#暂停一小段时间
		sleep(0.5)

	else:
		stats.game_active = False
		#显示光标
		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""检测是否有外星人到达了屏幕底端"""
	screen_rect = screen.get_rect()
	for aline in aliens.sprites():
		if aline.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
			break


def check_high_score(stats, sb):
	"""检查是否诞生了新的最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def save_high_score(stats):
	"""退出前存储最高得分"""
	filename = 'score.txt'
	with open(filename, 'w') as file_object:
		file_object.write(str(stats.high_score))
