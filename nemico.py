import arcade
import random

class Enemy(arcade.Sprite):
    def __init__(self, screen_height, scale=0.55, speed=4.2):
        super().__init__("./assets/nemico.png", scale=scale)
        self.center_x = 950
        self.center_y = random.randint(50, screen_height - 50)
        self.change_x = -speed
        self.change_y = 0

    def update(self):
        super().update()
        if self.right < 0:
            self.remove_from_sprite_lists()
