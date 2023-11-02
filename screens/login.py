from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class LoginAuthPatokCoffee(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file('kv/login.kv')
        super().__init__(*args, **kwargs)
