import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # screen=pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens,ship)
    
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship,bullets,aliens)

        

run_game();