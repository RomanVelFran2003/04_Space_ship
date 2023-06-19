from game.components.enemies.enemy import Enemy
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    
    def update(self, game):
        self.add_enemy(game)
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def add_enemy(self, game):
        enemy_type = random.randint(1,3)
        max_enemies = 3
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
        if game.score.count >= 100:
            max_enemies = 5
        if game.score.count >= 200:
            max_enemies = 10
        if game.score.count >= 300:
            max_enemies = 15
        if game.score.count >= 400:
            max_enemies = 20        
            
        if len(self.enemies)<max_enemies:
                self.enemies.append(enemy)
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
        self.enemies = []
            