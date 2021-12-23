
from kivy.lang import Builder
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class Container(BoxLayout):
    adaptive_width = True

class App(App):
    def build(self):
        self.title = 'Setting Screen UI'
        #self.theme_cls.primary_palette = "Pink"
        #self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_file('main.kv')


App().run()
