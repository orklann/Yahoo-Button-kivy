from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

import yahoo

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas:
            Color(1, 1, 1, 1, mode="rgba")
            Rectangle(pos=(0, 0), size=Window.size)


class MyApp(App):
    def build(self):
        parent = MyWidget()
        parent.size = Window.size
        #btn = YahooButton(text="MAKE THE ICON", pos=(200, 200), size=(140, 22))
        btn = yahoo.YahooButton(text="MAKE THE ICON", pos=(200, 200))
        btn2 = yahoo.YahooButton(text="Comfirm", pos=(200, 175))
        btn3 = yahoo.YahooButton(text="Yahoo!", pos=(200, 150))
        parent.add_widget(btn)
        parent.add_widget(btn2)
        parent.add_widget(btn3)

        label = Label(text="Hello, World!", pos=(0,0), font_size="12sp", 
                  color=(1, 0, 0, 1))
        label.texture_update()
        label.size = label.texture_size
        parent.add_widget(label)
        return parent


if __name__ == '__main__':
    MyApp().run()
