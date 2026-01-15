
import arcade
import os
import random
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

        self.sprite = None
        self.playerSpriteList = arcade.SpriteList()

        self.setup()

    def setup(self):
        
        self.sprite = arcade.Sprite("shooter.png")

        self.sprite.center_x = 100
        self.sprite.center_y = 100
        self.sprite.scale_x = 5.0
        self.sprite.scale_y = 5.0

        self.playerSpriteList.append(self.sprite)

        

    def on_draw(self):
        self.playerSpriteList.draw()
        
    def on_update(self, deltaTime):
        self.sprite.center_x += 1




def main():
    game = MyGame(
        600, 600, "Endless_Galactic_Ship"
    )
    arcade.run()


if __name__ == "__main__":
    main()
