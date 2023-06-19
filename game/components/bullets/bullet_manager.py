import pygame

from game.utils.constants import SHIELD_TYPE, SFXEXPLOSIONENEMY, SFXDEATHPLAYER,SFXSHOOT, SFXSHOOTENEMY


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
                    sfx_sound_explosion = pygame.mixer.Sound(SFXEXPLOSIONENEMY)
                    pygame.mixer.Sound.play(sfx_sound_explosion)
                    self.bullets.remove(bullet)
                    game.score.update()
                    
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    sfx_sound_death = pygame.mixer.Sound(SFXDEATHPLAYER)
                    pygame.mixer.Sound.play(sfx_sound_death)
                    game.playing = False
                    pygame.time.delay(100)
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
            sfx_sound = pygame.mixer.Sound(SFXSHOOTENEMY)
            pygame.mixer.Sound.play(sfx_sound)
        if bullet.owner == 'player'and len(self.bullets) < 1:
            self.bullets.append(bullet)
            sfx_sound = pygame.mixer.Sound(SFXSHOOT)
            pygame.mixer.Sound.play(sfx_sound)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []