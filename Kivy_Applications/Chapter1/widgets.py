from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
	pass

class WidgetsApp(App):
	def build(self):
		return MyWidget()

WidgetsApp().run()