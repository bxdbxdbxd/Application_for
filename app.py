from tkinter.ttk import Label

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import json

Builder.load_file('main.kv')
with open("object_first.json", "r", encoding='utf-8') as f:
    data = json.load(f)


class FirstScreen(Screen):
    pass

class ObjectFirstScreen(Screen):
    pass

class ObjectSecondScreen(Screen):
    pass

class ObjectThirdScreen(Screen):
    pass

class Data_for_lay(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_scroll_x = True
        self.pos_hint={'center_x':.53, 'center_y':.54}
        self.size_hint = (1, .65)
        grid = GridLayout(cols=6, spacing=5, size_hint = (.95, .8))

        for item in data['warehouse']:
            text1 = Label(text=item['material_name'], halign='left', size_hint_x=0.3)
            grid.add_widget(text1)
            text2 = Label(text=item['unit_of_measure'], halign='left', size_hint_x=0.15)
            grid.add_widget(text2)
            text3 = Label(text=str(item['quantity']), halign='left', size_hint_x=0.05)
            grid.add_widget(text3)
            text4 = Label(text=str(item['price']), halign='left', size_hint_x=0.15)
            grid.add_widget(text4)
            but_provider = Button(text=item['supplier'], halign='left', size_hint_x=0.25, background_normal='', background_color=(.3, .3, .4, .85))
            #but_provider.bind(on_press='')
            grid.add_widget(but_provider)
            text6 = Label(text=item['date_received'], halign='left', size_hint_x=0.15)
            grid.add_widget(text6)
        self.add_widget(grid)

class AddEstimates(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Data_for_lay())

class MyApp(App):
    def build(self):
        Window.size = (800, 800)
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='menu'))
        sm.add_widget(ObjectFirstScreen(name='first_object'))
        sm.add_widget(ObjectSecondScreen(name='second_object'))
        sm.add_widget(ObjectThirdScreen(name='third_object'))
        sm.add_widget(AddEstimates(name='add_estimates'))

        return sm

if __name__ == '__main__':
    MyApp().run()