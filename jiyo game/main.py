import arcade
import random
import time
from arcade import SpriteList, play_sound
from arcade.color import REDWOOD

HEIGHT = 600
WIDTH = 1000
TITLE = "Ohhhhhh"
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("images/bg.jpg")
        self.char = Jiyo("images/char1.png", 0.3)
        self.jump_sound = arcade.load_sound("images/jiyo1.mp3")
        self.bg_music = arcade.load_sound("images/bg.mp3")
        self.desert_eagle = arcade.SpriteList()
        self.last_spawn_time = time.time()
        self.hit = arcade.load_sound("images/jiyo.mp3", 1)
        self.lose_message = "ohhhhhhhh"
        self.game= True
        self.score = 0


    def setup(self):
        self.char.center_x=200
        self.char.center_y=100
        if self.game == True:
            arcade.play_sound(self.bg_music, 0.1)

    def spawn_desert_eagle(self):
        if self.game == True:
            fighter1 = Desert_eagle()
            fighter1.center_y = random.randint(30, HEIGHT - 10)
            fighter1.center_x = WIDTH + 30
            self.desert_eagle.append(fighter1)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(WIDTH/2,HEIGHT/2,WIDTH,HEIGHT,self.bg)
        self.char.draw()
        self.desert_eagle.draw()
        arcade.draw_text(self.score, 900, 500, REDWOOD, 80, anchor_x="center", bold=True)
        if not self.game:
            arcade.draw_text(self.lose_message, 500, 300, REDWOOD, 100, anchor_x="center", bold=True)

    def update(self, delta_time):
        if self.game == True:
            self.char.update()
            self.desert_eagle.update()
            current_time = time.time()
            if current_time - self.last_spawn_time >= 3:
                self.spawn_desert_eagle()
                self.last_spawn_time = current_time

            if arcade.check_for_collision_with_list(self.char, self.desert_eagle):
                arcade.play_sound(self.hit)
                self.game = False


    def on_key_press(self, symbol, modifiers):
        if self.game == True:
            if symbol == arcade.key.SPACE and self.char.jump == False:
                self.char.change_y = 15
                self.char.jump = True
                arcade.play_sound(self.jump_sound, 0.7)
            if symbol == arcade.key.D:
                self.char.change_x = 5
            if symbol == arcade.key.A:
                self.char.change_x = -5

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.D or arcade.key.A:
            self.char.change_x = 0


class Jiyo(arcade.Sprite):
    jump = False

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x
        self.change_y -= 0.35
        if self.center_y < 150:
            self.center_y = 150
            self.jump = False
        if self.left<0:
            self.left = 0
        if self.right>WIDTH:
            self.right = WIDTH

class Desert_eagle(arcade.Sprite):
    def __init__(self):
        super().__init__("images/oh.png")
        self.change_x = -5
        self.center_x += self.change_x
        if self.left < -10:
            self.kill()
            window.score += 1

window = Game(WIDTH, HEIGHT, TITLE)
window.setup()
arcade.run()