from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BONUS, BONUS_TYPE, SPACESHIP_BONUS

class Bonus(PowerUp):
    def __init__(self):
        super().__init__(BONUS, BONUS_TYPE)

    def activate(self, game):
        game.player.power_up_type = BONUS_TYPE
        game.player.set_image((40,60), SPACESHIP_BONUS)