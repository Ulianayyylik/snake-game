from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Ellipse
import random

WIDTH = 20
HEIGHT = 15
CELL_SIZE = 30

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
        self.init_game()
        Window.bind(on_touch_move=self.on_touch_move)
        Clock.schedule_interval(self.update, 0.15)
        
    def init_game(self):
        self.snake = [[WIDTH // 2, HEIGHT // 2], [WIDTH // 2 - 1, HEIGHT // 2], [WIDTH // 2 - 2, HEIGHT // 2]]
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.score = 0
        self.game_over = False
        self.create_apple()
        self.draw()
    
    def create_apple(self):
        while True:
            apple = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
            if apple not in self.snake:
                self.apple = apple
                break
    
    def update(self, dt):
        if self.game_over:
            return
        self.direction = self.next_direction
        head = self.snake[0].copy()
        if self.direction == "RIGHT": head[0] += 1
        elif self.direction == "LEFT": head[0] -= 1
        elif self.direction == "UP": head[1] += 1
        elif self.direction == "DOWN": head[1] -= 1
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in self.snake:
            self.game_over = True
            return
        self.snake.insert(0, head)
        if head == self.apple:
            self.score += 1
            self.create_apple()
        else:
            self.snake.pop()
        self.draw()
    
    def draw(self):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.2, 0.2, 0.2, 1)
            for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
                Rectangle(pos=(self.x + x, self.y), size=(1, HEIGHT * CELL_SIZE))
            for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
                Rectangle(pos=(self.x, self.y + y), size=(WIDTH * CELL_SIZE, 1))
            Color(1, 0, 0, 1)
            apple_x = self.apple[0] * CELL_SIZE
            apple_y = self.apple[1] * CELL_SIZE
            Ellipse(pos=(self.x + apple_x + 2, self.y + apple_y + 2), size=(CELL_SIZE - 4, CELL_SIZE - 4))
            for i, segment in enumerate(self.snake):
                seg_x = segment[0] * CELL_SIZE
                seg_y = segment[1] * CELL_SIZE
                if i == 0:
                    Color(0.3, 0.8, 0.3, 1)
                else:
                    Color(0.2, 0.6, 0.2, 1)
                Rectangle(pos=(self.x + seg_x + 1, self.y + seg_y + 1), size=(CELL_SIZE - 2, CELL_SIZE - 2))
    
    def on_touch_move(self, touch, *args):
        if not hasattr(self, '_touch_start'):
            self._touch_start = (touch.x, touch.y)
            return
        dx = touch.x - self._touch_start[0]
        dy = touch.y - self._touch_start[1]
        if abs(dx) > abs(dy) and abs(dx) > 20:
            if dx > 0 and self.direction != "LEFT": self.next_direction = "RIGHT"
            elif dx < 0 and self.direction != "RIGHT": self.next_direction = "LEFT"
        elif abs(dy) > 20:
            if dy > 0 and self.direction != "DOWN": self.next_direction = "UP"
            elif dy < 0 and self.direction != "UP": self.next_direction = "DOWN"
        self._touch_start = (touch.x, touch.y)

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == "__main__":
    SnakeApp().run()