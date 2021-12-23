
from kivy.lang import Builder
#from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout

class Container(MDBoxLayout):
    adaptive_width = True

class MainApp(MDApp):
    def build(self):
        self.title = 'Setting Screen UI'
        #self.theme_cls.primary_palette = "Pink"
        #self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_file('main.kv')


MainApp().run()
