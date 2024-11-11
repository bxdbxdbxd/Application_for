from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
import json

Builder.load_file('main.kv')
with open("object_first.json", "r") as f:
    data = json.load(f)

class FirstScreen(Screen):
    pass

class ObjectFirstScreen(Screen):
    pass

class ObjectSecondScreen(Screen):
    pass

class ObjectThirdScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        Window.size = (600, 800)
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='menu'))
        sm.add_widget(ObjectFirstScreen(name='first_object'))
        sm.add_widget(ObjectSecondScreen(name='second_object'))
        sm.add_widget(ObjectThirdScreen(name='third_object'))
        return sm

if __name__ == '__main__':
    MyApp().run()