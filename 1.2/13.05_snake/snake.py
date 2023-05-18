import random
import sys
import tkinter as tk
from tkinter import messagebox

import pygame


class Snake:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.snake_pos = [[50, 50], [40, 50], [30, 50]]
        self.snake_direction = pygame.K_RIGHT

    def update_position(self):
        x, y = self.snake_pos[0]
        if self.snake_direction == pygame.K_UP:
            y -= self.cell_size
        elif self.snake_direction == pygame.K_DOWN:
            y += self.cell_size
        elif self.snake_direction == pygame.K_LEFT:
            x -= self.cell_size
        elif self.snake_direction == pygame.K_RIGHT:
            x += self.cell_size
        self.snake_pos.insert(0, [x, y])

    def check_collision_with_self(self):
        return self.snake_pos[0] in self.snake_pos[1:]

    def check_collision_with_wall(self):
        x, y = self.snake_pos[0]
        return x < 0 or x >= self.cell_number * self.cell_size or y < 0 or y >= self.cell_number * self.cell_size

    def grow(self):
        self.snake_pos.pop()

    def draw(self, screen, snake_color):
        for pos in self.snake_pos:
            pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], self.cell_size, self.cell_size))


class Apple:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.apple_pos = [random.randrange(1, cell_number) * cell_size, random.randrange(1, cell_number) * cell_size]

    def check_collision_with_snake(self, snake_pos):
        return snake_pos[0] == self.apple_pos

    def update_position(self):
        self.apple_pos = [random.randrange(1, self.cell_number) * self.cell_size,
                          random.randrange(1, self.cell_number) * self.cell_size]

    def draw(self, screen, apple_color):
        pygame.draw.rect(screen, apple_color,
                         pygame.Rect(self.apple_pos[0], self.apple_pos[1], self.cell_size, self.cell_size))


class Game:
    def __init__(self):
        pygame.init()

        self.cell_size = 10
        self.cell_number = 100
        self.background_color = (0, 0, 0)
        self.snake_color = (0, 255, 0)
        self.apple_color = (255, 0, 0)
        self.text_color = (255, 255, 255)

        self.eat_sound = pygame.mixer.Sound("eat.wav")
        self.crash_sound = pygame.mixer.Sound("crash.wav")
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        pygame.display.set_caption("Snake Game")

        self.snake_speed = 10

        self.snake = Snake(self.cell_size, self.cell_number)
        self.apple = Apple(self.cell_size, self.cell_number)

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def show_rules(self):
        running = True
        while running:
            self.screen.fill(self.background_color)
            self.draw_text("Rules:", pygame.font.Font(None, 36), self.text_color, self.screen, 40, 40)
            self.draw_text("1. Используйте стрелки для управления змейкой.", pygame.font.Font(None, 24),
                           self.text_color, self.screen, 40, 100)
            self.draw_text("2. Ешьте яблоки, расти.", pygame.font.Font(None, 24), self.text_color, self.screen, 40, 140)
            self.draw_text("3. Не врезайтесь в стены или в себя.", pygame.font.Font(None, 24), self.text_color,
                           self.screen, 40, 180)
            self.draw_text("Нажмите ESC, чтобы вернуться в главное меню.", pygame.font.Font(None, 24), self.text_color,
                           self.screen, 40, 300)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

    def main_menu(self):
        while True:
            self.screen.fill(self.background_color)
            self.draw_text("Snake Game", pygame.font.Font(None, 48), self.text_color, self.screen, 40, 40)
            self.draw_text("Play (P)", pygame.font.Font(None, 36), self.text_color, self.screen, 40, 100)
            self.draw_text("Rules (R)", pygame.font.Font(None, 36), self.text_color, self.screen, 40, 140)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return
                    if event.key == pygame.K_r:
                        self.show_rules()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def game_over(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Game Over", "You crashed into the wall!")
        root.destroy()

    def run(self):
        self.main_menu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                        self.snake.snake_direction = event.key

            self.snake.update_position()

            if self.snake.check_collision_with_wall():
                self.crash_sound.play()
                self.game_over()
                pygame.quit()
                sys.exit()

            if self.snake.check_collision_with_self():
                self.crash_sound.play()
                self.game_over()
                pygame.quit()
                sys.exit()

            if self.apple.check_collision_with_snake(self.snake.snake_pos):
                self.eat_sound.play()
                self.apple.update_position()
            else:
                self.snake.grow()

            self.screen.fill(self.background_color)
            self.snake.draw(self.screen, self.snake_color)
            self.apple.draw(self.screen, self.apple_color)

            pygame.display.flip()
            pygame.time.Clock().tick(self.snake_speed)


if __name__ == "__main__":
    game = Game()
    game.run()
