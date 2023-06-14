from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_1 import Enemy_1
from game.components.enemies.enemy_2 import Enemy_2

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
        for enemy_1 in self.enemies:
            enemy_1.update(self.enemies)
        for enemy_2 in self.enemies:
            enemy_2.update(self.enemies)
    
    def add_enemy(self):
        if len(self.enemies)<1:
            enemy = Enemy()
            enemy_1 = Enemy_1()
            enemy_2 = Enemy_2()
            self.enemies.append(enemy)
            self.enemies.append(enemy_1)
            self.enemies.append(enemy_2)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for enemy_1 in self.enemies:
            enemy_1.draw(screen)
        for enemy_2 in self.enemies:
            enemy_2.draw(screen)
            