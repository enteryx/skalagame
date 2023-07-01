
from view import Actor,Button,Cursor
import pygame, sys 

pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_high = 1000
screen = pygame.display.set_mode((screen_width, screen_high))
background = pygame.image.load("background.jpg")
pygame.mouse.set_visible(False)

update_time = 30

actor = Actor(450, 670)
actor_group = pygame.sprite.Group()
actor_group.add(actor)

play = Button(150, 915, "play.png")
feed = Button(480, 915, "feed.png")
sleep = Button(750, 915, "sleep.png")
buttons_group = pygame.sprite.Group()
buttons_group.add(play)
buttons_group.add(feed)
buttons_group.add(sleep)

cursor = Cursor()
cursor_group = pygame.sprite.Group()
cursor_group.add(cursor)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprite = [s for s in buttons_group if s.rect.collidepoint(pos)]
            for sp in clicked_sprite:
                if sp == play:
                    actor.play()
                if sp == feed:
                    actor.feed()
                if sp == sleep:
                    actor.sleep()

    pygame.display.flip()
    screen.blit(background, (0 ,0))

    actor_group.update(screen)
    actor_group.draw(screen)

    buttons_group.draw(screen)

    cursor.update()
    cursor_group.draw(screen)

    clock.tick(update_time)








