from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
	pass

class WidgetsApp(App):
	def build(self):
		return MyWidget()

WidgetsApp().run()
#Note that the coordinate (0, 0) is located at the bottom-left corner, the Cartesian origin.
#Attributes with properties are updated in kivy file
