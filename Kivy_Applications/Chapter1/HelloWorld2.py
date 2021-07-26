#Hello World Using kivy file
from kivy.app import App
from kivy.uix.button import Label

#Note: The beginning part of the App class's subclass name must coincide with the name of the Kivy file.
class HelloWorld2App(App):
    def build(self):
        return Label()

HelloWorld2App().run()


