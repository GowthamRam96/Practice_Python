import kivy
#Run Basic Kivy Application

from kivy.app import App
from kivy.uix.button import Label

class HelloApp(App):
    def build(self):
        return Label(text = 'Hello World!')

HelloApp().run()
