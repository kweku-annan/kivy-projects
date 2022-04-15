from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window

# TODO 1: Search for how you can set a default title for the app.

Window.size = (500, 600)
Window.minimum_width, Window.minimum_height = Window.size
# Window.title = "Data Collection App"

Builder.load_file('main.kv')


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class DataCollectionApp(App):
    def build(self):
        # Window.title = "Data Collection App"
        return MainWindow()


if __name__ == "__main__":
    DataCollectionApp().run()
