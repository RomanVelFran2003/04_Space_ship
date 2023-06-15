from game.components.enemies.enemy import Enemy
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def add_enemy(self):
        enemy_type = random.randint(1,3)
        if enemy_type == 1:
            enemy = Enemy()
        elif enemy_type == 2:
            x_speed = 8
            y_speed = 4
            move_x_for = [50,120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        elif enemy_type == 3:
            x_speed = 10
            y_speed = 6
            move_x_for = [50,120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)

        if len(self.enemies)<1:
            self.enemies.append(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            