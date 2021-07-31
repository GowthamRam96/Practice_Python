<h1>Layout Creation using Kivy and Python</h1>

<h2>Files List</h2>
<h4>1. Python Code in FloatLayouts.py</h4>
<h4>2. Kivy Code in floatlayout.kv</h4>  

<h3>FloatLayouts.py</h3>

```py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
```

The above two lines are used to import the libraries and packages to be used in the code.

```py
class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()
```

The above piece of code has a Class definition.

```py
FloatLayoutApp().run()
```

Run method is used to excecute the App()

Properties and attributes are defined in **_floatlayout.kv_** file

<h2>Results</h2>

![OriginalResult](Chapter1/Images/FloatLayout1.PNG)

![SizingReference](Chapter1/Images/FloatLayout2.PNG)
