import pygame
import os

from game.utils.constants import SHIELD_TYPE, IMG_DIR

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
 
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy':
                    game.enemy_manager.enemies.remove(enemy)
                    pygame.mixer.music.load(os.path.join(IMG_DIR,"Sounds\enemydeath.mp3"))
                    pygame.mixer.music.play(1)
                    self.bullets.remove(bullet)
                    game.score.update()
                    
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1000)
                    game.death_count.update()
                break


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []