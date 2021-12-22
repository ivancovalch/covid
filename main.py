from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text = "Hello world", halign = "center")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
