from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.screens import *
from kivymd.uix.card import MDCard

import pyrebase
from datetime import datetime

pyrebaseConfig = {
    "apiKey": "AIzaSyA35EfGcz9Wlx4zKu6WY_79EWrZlqlOG4g",
    "authDomain": "patokcoffee-f74a1.firebaseapp.com",
    "databaseURL": "https://patokcoffee-f74a1-default-rtdb.firebaseio.com/",
    "projectId": "patokcoffee-f74a1",
    "storageBucket": "patokcoffee-f74a1.appspot.com",
    "messagingSenderId": "74047010534",
    "appId": "1:74047010534:web:afea68e0c4ab46b2d7ad27",
    "measurementId": "G-4KPXHWSYCB",
}

firebase = pyrebase.initialize_app(pyrebaseConfig)
db = firebase.database()
auth = firebase.auth()

class WindowManager(MDScreenManager):
    pass

class Coffee_Application(MDApp):

    CLASSES = {
        'homescreen': 'screens.screen',
        'login': 'screens.login',
        'homeapp': 'screens.homeapp',
        'sigup': 'screens.signup',
        'account': 'screens.account'
    }

    KV_FILES = {
        'kv/screen.kv',
        'kv/login.kv',
        'kv/signup.kv',
        'kv/homeapp.kv',
        'kv/account.kv'
    }

    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]

    def build(self):
        
        self.wm = WindowManager()
        screens = [
            HomeScreenPatokCoffee(name='homescreen'),
            HomeApplicationCoffee(name='homeapp'),
            LoginAuthPatokCoffee(name='login'),
            SiginupPatokCoffee(name='signup'),
            Account(name='account'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

    def login_to_pyrebase(self, email_input, password_input):
        # time
        def get_part_of_day(h):
            return (
                "morning"
                if 5 <= h <= 11
                else "afternoon"
                if 12 <= h <= 13
                else "evening"
                if 14 <= h <= 18
                else "night"
            )
        time = get_part_of_day(datetime.now().hour)
        people = db.child('UserDatabase').child('Users').get() 
        try:
            for i in people.each():
                if email_input.text == i.val()['Email']:
                    if password_input.text == i.val()['Password']:
                        self.wm.current = 'homeapp'

                        username_database = i.val()['Username']
                        pay = i.val()['Pay']
                        self.wm.get_screen('homeapp').time_and_user.text = f"Good {time}, {username_database}"
                        self.wm.get_screen('account').user_account.text = f'Hello {username_database}'
                        self.wm.get_screen('account').patokpay.text = f'Patok Pay ${pay}'
        except:
            email_input.text = ''
            password_input.text = ''

    def signup_to_pyrebase(self, username_to_user, email_to_user, password_to_user, status_signup): # username_to_user, email_to_user, password_to_user

        try:
            auth.create_user_with_email_and_password(email_to_user.text, password_to_user.text)
            data = {
                'Username': username_to_user.text,
                'Email': email_to_user.text,
                'Password': password_to_user.text,
                'Pay': 0
            }
            db.child('UserDatabase').child('Users').push(data)
            username_to_user.text = ''
            email_to_user.text = ''
            password_to_user.text = ''
            status_signup.text = ''
            status_signup.text = 'Signup Sucess'
        except:
            status_signup.text = ''
            status_signup.text = 'Singup Error'

if __name__ == '__main__':
    Coffee_Application().run()
