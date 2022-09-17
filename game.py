import pygame

class PongGame:

    def __init__(self, screen, width, height):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.BG = pygame.image.load('assets/background.png')
        self.STICK = pygame.image.load('assets/stick.png')
        self.BALL = pygame.image.load('assets/ball.png')
        self.BRICK = pygame.image.load('assets/brick.png')
        
        self.stick_x, self.stick_y = 130, 450
        self.ball_x, self.ball_y = 200, 200
        self.brick_x, self.brick_y = 0, 0
        
        self.stick_vel = 5
        self.ball_xvel = 2.5
        self.ball_yvel = 2.5
        
        self.brick_pos = [(x*108,y*30) for y in range(2) for x in range(7)]
        
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.overfont = pygame.font.Font('freesansbold.ttf', 30)
        self.over = self.overfont.render('', True, (255,0,0))
        self.text = self.font.render(f'Score: {self.score}', True, (0,255,0))
        
    def draw_screen(self):
        self.screen.blit(self.BG,(0,0))
        self.screen.blit(self.STICK,(self.stick_x, self.stick_y))
        for pos in self.brick_pos: self.screen.blit(self.BRICK,pos)
        self.screen.blit(self.BALL,(self.ball_x, self.ball_y))
        self.screen.blit(self.text, (5, 480))
        self.screen.blit(self.over,(287, 235))
        
    def controls(self,direction):
        if   direction=="left" :  self.stick_x -= self.stick_vel
        elif direction=="right":  self.stick_x += self.stick_vel
        if   self.stick_x<0: self.stick_x += self.stick_vel
        elif self.stick_x+125>self.WIDTH: self.stick_x -= self.stick_vel
    
    def ball_motion(self):
        self.ball_x += self.ball_xvel
        self.ball_y += self.ball_yvel
        if self.ball_x <= 0 or self.ball_x+30 >= self.WIDTH: self.ball_xvel *= -1
        if self.ball_y <= 0 or self.ball_y+30 >= self.HEIGHT: self.ball_yvel *= -1
        if self.ball_y <= self.stick_y <= self.ball_y+30 and self.stick_x<=self.ball_x<=self.stick_x+125:
            self.ball_yvel *= -1
            
    def breakbrick(self):
        for pos in self.brick_pos: 
            if self.ball_y <= pos[1] <= self.ball_y+30 and pos[0]<=self.ball_x<=pos[0]+108 or \
               self.ball_y <= pos[1]+30 <= self.ball_y+30 and pos[0]<=self.ball_x+30<=pos[0]+108:
                self.ball_yvel *= -1
                self.brick_pos.remove(pos)
                self.score += 5
                self.text = self.font.render(f'Score: {self.score}', True, (0,255,0))
            
    def isgameover(self): 
        if self.ball_y+30 >= self.HEIGHT: 
            self.over = self.overfont.render("GAME OVER", True, (255,0,0))
            self.stick_vel = 0
            self.ball_xvel = 0
            self.ball_yvel = 0
        if self.brick_pos == []: 
            self.over = self.overfont.render("YOU WON!!!", True, (255,0,0))
            self.stick_vel = 0
            self.ball_xvel = 0
            self.ball_yvel = 0
        

    
        