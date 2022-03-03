from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file('main.kv')
Window.clearcolor = (1, 1, 1, 1)
Window.size = (500, 300)
Window.minimum_width, Window.minimum_height = Window.size  # Setting the minimum size of the window


class MainWindow(Widget):
    pass


class AttendeesFormsApp(App):
    def build(self):
        self.title = "Registration Form"
        return MainWindow()


if __name__ == "__main__":
    AttendeesFormsApp().run()
