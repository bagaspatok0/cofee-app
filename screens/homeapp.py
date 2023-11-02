from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class HomeApplicationCoffee(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file('kv/homeapp.kv')
        super().__init__(*args, **kwargs)
