import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.explosion import Explosion
from game.components.power_ups.bonus import Bonus
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP, SHIELD_TYPE, BONUS_TYPE,SPACESHIP_BONUS,EXPLOSION_TYPE,SPACESHIP_EXPLOSION

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(5,7)

    def generate_power_up(self):
        power_up_items = [Shield, Explosion, Bonus]
        rages = [40, 20, 40]
        power_up_types = random.choices(power_up_items, weights=rages)[0]
        power_up = power_up_types()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                if isinstance(power_up, Shield):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

                elif isinstance(power_up, Bonus):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

                elif isinstance(power_up, Explosion):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)