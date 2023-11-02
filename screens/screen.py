from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class HomeScreenPatokCoffee(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file('kv/screen.kv')
        super().__init__(*args, **kwargs)
