from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Point, Rectangle, Color, Line

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas:
            Color(1, 1, 1, 1, mode="rgba")
            Rectangle(pos=(0, 0), size=Window.size)


class YahooButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resize()
        self.draw_normal()

    def resize(self):
        label = Label(text=self.text, font_size='12sp', bold=True)
        label.texture_update()
        self.size = (label.texture_size[0] + 20, label.texture_size[1] + 5)

    def draw_normal(self):
        self.canvas.clear()
        with self.canvas:
            min_x = self.pos[0]
            min_y = self.pos[1]
            max_x = self.pos[0] + self.size[0]
            max_y = self.pos[1] + self.size[1]

            # Inner background rectangle
            Color(0.9804, 0.0353, 0.5333)
            x = self.pos[0] + 2
            y = self.pos[1] + 2
            width = self.size[0] - 4
            height = self.size[1] - 4
            Rectangle(pos=(x, y), size=(width, height))

            # Bottom line
            Color(0, 0, 0)
            x1 = min_x + 2 + 0.5
            y1 = min_y + 0.5
            x2 = max_x - 2 + 0.5
            y2 = y1
            Line(points=[x1, y1, x2, y2])

            # Top line
            Color(0, 0, 0)
            x1 = min_x + 2 + 0.5
            y1 = max_y - 1 + 0.5
            x2 = max_x - 2 + 0.5
            y2 = max_y - 1 + 0.5
            Line(points=[x1, y1, x2, y2])

            # Left line
            Color(0, 0, 0)
            x1 = min_x + 1
            y1 = min_y + 2
            x2 = min_x + 1
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # Right line
            Color(0, 0, 0)
            x1 = max_x
            y1 = min_y + 2
            x2 = max_x
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # Inner bottom line
            Color(0.42, 0.22, 0.33)
            x1 = min_x + 2 + 0.5
            y1 = min_y + 1 + 0.5
            x2 = max_x - 2 + 0.5
            y2 = y1
            Line(points=[x1, y1, x2, y2])

            # Inner right line
            Color(0.42, 0.22, 0.33)
            x1 = max_x - 1 - 0.5
            y1 = min_y + 2 
            x2 = x1
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # 4 corner pixels
            Color(0, 0, 0)
            top_left = (min_x + 1, max_y - 2)
            Rectangle(pos=top_left, size=(1, 1))
            top_right = (max_x - 2, max_y - 2)
            Rectangle(pos=top_right, size=(1, 1))
            bottom_left = (min_x + 1, min_y + 1)
            Rectangle(pos=bottom_left, size=(1, 1))
            bottom_right = (max_x - 2, min_y + 1)
            Rectangle(pos=bottom_right, size=(1, 1))

            # Draw Text
            x = self.pos[0]
            y = self.pos[1]
            self.label = Label(text=self.text, color=(1, 1, 1), pos=(x, y), size=self.size, font_size='12sp', bold=True)
            self.label.texture_update()
            self.canvas.add(self.label.canvas)

    def on_touch_down(self, touch):
        self.canvas.clear()
        with self.canvas:
            min_x = self.pos[0]
            min_y = self.pos[1]
            max_x = self.pos[0] + self.size[0]
            max_y = self.pos[1] + self.size[1]

            # Inner background rectangle
            Color(0.9804, 0.0353, 0.5333)
            x = self.pos[0] + 2
            y = self.pos[1] + 2
            width = self.size[0] - 4
            height = self.size[1] - 4
            Rectangle(pos=(x, y), size=(width, height))

            # Bottom line
            Color(0, 0, 0)
            x1 = min_x + 2 + 0.5
            y1 = min_y + 0.5
            x2 = max_x - 2 + 0.5
            y2 = y1
            Line(points=[x1, y1, x2, y2])

            # Top line
            Color(0, 0, 0)
            x1 = min_x + 2 + 0.5
            y1 = max_y - 1 + 0.5
            x2 = max_x - 2 + 0.5
            y2 = max_y - 1 + 0.5
            Line(points=[x1, y1, x2, y2])

            # Left line
            Color(0, 0, 0)
            x1 = min_x + 1
            y1 = min_y + 2
            x2 = min_x + 1
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # Right line
            Color(0, 0, 0)
            x1 = max_x
            y1 = min_y + 2
            x2 = max_x
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # Inner bottom line
            Color(1, 0.91, 0.96)
            x1 = min_x + 2 + 0.5
            y1 = min_y + 1 + 0.5
            x2 = max_x - 2 + 0.5
            y2 = y1
            Line(points=[x1, y1, x2, y2])

            # Inner right line
            Color(1, 0.91, 0.96)
            x1 = max_x - 1 - 0.5
            y1 = min_y + 2 
            x2 = x1
            y2 = max_y - 2
            Line(points=[x1, y1, x2, y2])

            # 4 corner pixels
            Color(0, 0, 0)
            top_left = (min_x + 1, max_y - 2)
            Rectangle(pos=top_left, size=(1, 1))
            top_right = (max_x - 2, max_y - 2)
            Rectangle(pos=top_right, size=(1, 1))
            bottom_left = (min_x + 1, min_y + 1)
            Rectangle(pos=bottom_left, size=(1, 1))
            bottom_right = (max_x - 2, min_y + 1)
            Rectangle(pos=bottom_right, size=(1, 1))

            # Draw Text
            x = self.pos[0]
            y = self.pos[1]
            self.label = Label(text=self.text, color=(1, 1, 1), pos=(x, y), size=self.size, font_size='12sp', bold=True)
            self.label.texture_update()
            self.canvas.add(self.label.canvas)

    def on_touch_up(self, touch):
        self.draw_normal()

class MyApp(App):
    def build(self):
        parent = MyWidget()
        #btn = YahooButton(text="MAKE THE ICON", pos=(200, 200), size=(140, 22))
        btn = YahooButton(text="MAKE THE ICON", pos=(200, 200))
        parent.add_widget(btn)
        return parent


if __name__ == '__main__':
    MyApp().run()
