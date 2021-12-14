from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<Screen0>:
    MDCard:
        size_hint: 0.9, 0.7
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDLabel:
        id: appdetail
        text: "FELIZ TOUR"
        font_size: 35
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15
    MDLabel:
        id: appdes
        text: "developed by"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15
    MDLabel:
        id: chandu
        text: "Chandrashekar O"
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15
    MDLabel:
        id: sahaja
        text: "Sahaja Reddy P"
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15
    MDRoundFlatButton:
        text: "Continue to APP"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_press: app.continue_to_app()
<Screen1>:

    MDCard:
        size_hint: 0.8, 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDLabel:
        id: welcome_label
        text: "WELCOME"
        font_size: 40
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15

    MDTextFieldRound:
        id: user
        hint_text: "username"
        icon_right: "account"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.60}

    MDTextFieldRound:
        id: password
        hint_text: "password"
        icon_right: "eye-off"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        password: True

    MDRoundFlatButton:
        text: "LOG IN"
        font_size: 12
        pos_hint: {"center_x": 0.3, "center_y": 0.3}
        on_press: app.login()

    MDRoundFlatButton:
        text: "CLEAR"
        font_size: 12
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        on_press: app.clear()

    Widget:
        size_hint_y: None
        height: 10

<PostLogin>:

    MDLabel:
        id: welcome_label
        text: "Not registered for a Trip?"
        font_size: 40
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15

    MDRoundFlatButton:
        text: "New Registration"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        on_press: app.newRegistration()


    MDLabel:
        id: welcome_label
        text: "Already registered? "
        font_size: 40
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 15

    MDRoundFlatButton:
        text: "Check status"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        on_press: app.continue_to_app()


<Register>:
    MDFlatButton:
        text: "Submit"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        on_press: app.transactions()
        size_hint: 0.5,0.075






<Overview>:
    MDRaisedButton:
        text: "Overview"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.25, "center_y": 0.8875}
        size_hint: 0.5,0.075
        on_press: app.overview()
        border: 'yellow'

    MDFlatButton:
        text: "Transactions"
        font_size: 18
        pos_hint: {"center_x": 0.75, "center_y": 0.8875}
        on_press: app.transactions()
        size_hint: 0.5,0.075


    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        size_hint: 1,0.850
        pos_hint: {"center_x": 0.55, "y": 0}


        MDCard:
            size_hint: 0.90, 2.6
            pos_hint: 0.5,0.5
            elevation: 10
            orientation: 'vertical'


    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus
<Transactions>:
    MDRaisedButton:
        text: "Transactions"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.75, "center_y": 0.8875}
        size_hint: 0.5,0.075
        on_press: app.transactions()
        border: 'yellow'

    MDFlatButton:
        text: "Overview"
        font_size: 18
        pos_hint: {"center_x": 0.25, "center_y": 0.8875}
        on_press: app.overview()
        size_hint: 0.5,0.075

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus

""")

sm = ScreenManager()
Window.size = (360, 600)


class Screen0(Screen):
    pass


class Screen1(Screen):
    pass


class Overview(Screen):
    pass


class Transactions(Screen):
    pass


class PostLogin(Screen):
    pass


class Register(Screen):
    pass


class Screen6(Screen):
    pass


class MainApp(MDApp):
    data = {

        'Add Transaction': 'Addtrs',

    }

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(Screen0(name='screen0'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))
        sm.add_widget(PostLogin(name='postlogin'))
        sm.add_widget(Register(name='register'))
        sm.add_widget(Screen6(name='screen6'))

        sm.current = 'screen0'
        return sm

    def continue_to_app(self):
        # self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
        sm.current = 'screen1'

    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def overview(self):
        sm.current = 'overview'

    def transactions(self):
        sm.current = 'transactions'

    def plus(self, addtrs):
        sm.current = 'screen0'

    def login(self):
        sm.current = 'postlogin'

    def newRegistration(self):
        sm.current = 'register'


MainApp().run()