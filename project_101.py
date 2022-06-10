# making a game using the command pygame 
import pygame
pygame.init()

from tkinter import *

win = Tk()
win.title("maddroxx")
win.configure(bg="black")
win.geometry("1280x720") #fix the window size

#defining variables
x = 100
y = 100
ballX = 300
ballY = 300
vel = 6
ballVel = 4
run = True

def draw_game():
          win.fill((0, 0, 0))
          pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
          pygame.draw.rect(win, (255, 0, 0), (ballX, ballY, 40, 40))
          pygame.display.update()

while run:
      pygame.time.delay(100)

      if ballX &lt; x - 10: ballX = ballX + ballVel drawGame() elif baddyX &gt; x + 10:
          drawGame()
          baddyX = baddyX - baddyVel
      elif baddyY &lt; y - 10: baddyY = baddyY + baddyVel elif baddyY &gt; y + 10:
          baddyY = baddyY - baddyVel
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
            x -= vel

      if keys[pygame.K_RIGHT]:
            x += vel
      
      if keys[pygame.K_UP]:
            y -= vel
      
      if keys[pygame.K_DOWN]:
            y += vel
      
      draw_game()
        
