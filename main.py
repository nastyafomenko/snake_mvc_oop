import pygame
import time
import random
import constants as const
from controller import controller
from view import view
from food import food
from snake import snake

MOVEFOOD = pygame.USEREVENT + 0

pygame.init()
clock = pygame.time.Clock()

view = view()
view.window_init(const.dis_width,const.dis_height)

def gameLoop():
	contr = controller()
	Food = food()
	Snake = snake(Food)
	
	Snake.set_x1_y1(const.dis_width,const.dis_height)
	Food.get_food_pos(const.dis_width,const.dis_height,const.snake_block)
	pygame.time.set_timer(MOVEFOOD, 3000)

	while not contr.game_over:
		
		while contr.game_close == True:
			view.game_over_screen(Snake.Length_of_snake,const.blue,const.red,const.dis_width,const.dis_height)
			

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						contr.set_gameover()
						contr.set_gameclose()
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				contr.set_gameover()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					Snake.change_x1y1_change(-const.snake_block,0)
				elif event.key == pygame.K_RIGHT:
					Snake.change_x1y1_change(const.snake_block,0)
				elif event.key == pygame.K_UP:
					Snake.change_x1y1_change(0,-const.snake_block)
				elif event.key == pygame.K_DOWN:
					Snake.change_x1y1_change(0,const.snake_block)
			if event.type == MOVEFOOD:
				Food.move_food_pos(const.snake_block)

		contr.change_gameclose(Snake.is_border_death(const.dis_width,const.dis_height))
		
		foodx,foody = Food.ret_food_pos()
		if contr.food_behind_border(foodx,foody,const.dis_width,const.dis_height):
			Food.get_food_pos(const.dis_width,const.dis_height,const.snake_block)
		
		Snake.change_x1_y1()
		view.draw_food(Food.foodx,Food.foody,const.blue,const.red,const.snake_block)
		Snake.add_snake_head()
		Snake.control_snake_size()
		contr.change_gameclose(Snake.self_death())
		view.our_snake(const.snake_block,Snake.snake_List,const.green,const.black)
		view.Your_score(Snake.Length_of_snake-1,const.yellow)

		pygame.display.update()

		Snake.inc_snake_length()

		clock.tick(const.snake_speed)

	pygame.quit()
	quit()

gameLoop()
