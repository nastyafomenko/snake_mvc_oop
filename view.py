import pygame

class view:
    def __init__(self):
        self.dis = None
        self.font_style = None
        self.score_font = None
        
    def window_init(self,dis_width, dis_height):
        self.dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game')
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)

    def Your_score(self,score,color):
        value = self.score_font.render("Your Score: " + str(score), True, color)
        self.dis.blit(value, [0, 0])

    def our_snake(self,snake_block, snake_list,prim_color,second_color):
        for x in snake_list[:-1]:
            pygame.draw.rect(self.dis,prim_color, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(self.dis,second_color, [snake_list[-1][0], snake_list[-1][1], snake_block, snake_block])

    def message(self,msg, color,width,height):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [width / 6, height / 3])

    def game_over_screen(self,Length_of_snake,bgcolor,text_color,width,height):
        self.dis.fill(bgcolor)
        self.message("You Lost! Press C-Play Again or Q-Quit",text_color,width,height)
        self.Your_score(Length_of_snake - 1,text_color)
        pygame.display.update()

    def draw_food(self,foodx,foody,bgcolor,food_color,snake_block):
        self.dis.fill(bgcolor)
        pygame.draw.rect(self.dis, food_color, [foodx, foody, snake_block, snake_block])