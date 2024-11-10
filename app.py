from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('main.kv')

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        Window.size = (700, 900)
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    MyApp().run()

