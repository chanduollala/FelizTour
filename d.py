from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import Snackbar
#google drive api
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('apifile.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
usheet = client.open("FelizTourUsers").sheet1
tsheet= client.open("FelizTourTransactions").sheet1
rsheet= client.open("FelizTourTripRequests").sheet1
msheet= client.open("FelizTourTeams").sheet1


# SMS for sending SMS
import requests
url = "https://www.fast2sms.com/dev/bulk"

headers = {
'authorization': "aWmyldGXYkqTQFo9cb5K1st6geJARZ4uLnP2jVEMH0Sr3DziIxWviBmqXgeTV25xcwFjdaPsZERk8G9D",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}


import re



Builder.load_file("file.kv")
sm = ScreenManager()
Window.size = (300,550)

userdetails=[]

class HelloScreen(MDScreen):
    pass

class LoginPage(MDScreen):
    pass

class Overview(MDScreen):
    pass

class Transactions(MDScreen):
    pass

class PostLogin(MDScreen):
    pass

class Signup(MDScreen):
    pass

class NewTrip(MDScreen):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass

class DrawerList(ButtonBehavior, MDList):
    pass

class TeamStatus(MDScreen):
    pass

class MainApp(MDApp):

    data = {
        'Add Transaction': 'Addtrs',
        "hi": "hello"
    }
    displayname="User"

    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(LoginPage(name='loginpage'))

        sm.add_widget(Transactions(name='transactions'))
        sm.add_widget(NewTrip(name='newtrip'))
        sm.add_widget(Signup(name='signup'))

        #sm.add_widget(TeamStatus(name='teamstatus'))

        sm.current = 'helloscreen'
        return sm
    def validateuser(self,username,password):
        usernames=usheet.col_values(7)

        if username not in usernames:
            Snackbar(
                text="Username not found!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0
        else:
            for i in range(0,len(usernames)):
                if usernames[i]==username:
                    column=i
                    user_keys=usheet.row_values(1)
                    user_values=usheet.row_values(i+1)
                    userdetails= {user_keys[i]: user_values[i] for i in range(len(user_keys))}
                    print(userdetails)
                    print("user found")
                    if password==userdetails["password"]:
                        return userdetails
                    else:
                        Snackbar(
                            text="Password incorrect",
                            snackbar_x="10dp",
                            snackbar_y="10dp",
                            size_hint_x=.95
                        ).open()

            return 0

    def checksignupdata(self,name,age,gender,phone,email,password):
        return "OK"
        namepattern='[a-zA-Z\s]'
        phonepattern='^[0-9]{10}$'
        emailpattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.search(namepattern,name)):
            pass
        else:
            Snackbar(
                text="Name has only alphabets and spaces",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0
        if (int(age)>10 and int(age)<100):
            pass
        else:
            Snackbar(
                text="Age invalid!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        if (gender in ["male","female","Male","Female","M","F"]):
            pass
        else:
            Snackbar(
                text="Gender: Invalid Input",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        if (re.search(phonepattern,phone)):
            pass
        else:
            Snackbar(
                text="Invalid Phone number",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        if (re.search(emailpattern,email)):
            pass
        else:
            Snackbar(
                text="Invalid Phone number",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        return "OK"
    def continue_to_app(self):
        # self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
        sm.current = 'loginpage'

    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def overview(self):
        sm.current = 'overview'

    def transactions(self):
        sm.current = 'transactions'

    def plus(self, addtrs):
        sm.current = 'addtransaction'

    def login(self,username,password):
        self.userdetails=self.validateuser(username,password)
        if self.userdetails!=0:
            self.uname=self.userdetails["Name"]
            self.phonenumber=self.userdetails["Phone"]
            self.loggedinusername=self.userdetails["Usename"]
            self.gender=self.userdetails["Gender"]

            sm.add_widget(PostLogin(name='postlogin'))
            Snackbar(
                text="Logged in succesfully as "+self.uname,
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            sm.current = 'postlogin'

    def newtrip(self):
        sm.add_widget(NewTrip(name='newtrip'))
        sm.current = 'newtrip'

    def signup(self):
        Snackbar(
            text="Enter your details",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        sm.current = 'signup'


    def signupSubmit(self,name,age,gender,phone,email,password):
        x=self.checksignupdata(name,age,gender,phone,email,password)
        if x=="OK":
            username=name[:5]+phone[-3:]
            payload = f"sender_id=FSTSMS&message=welcome to feliz tour. your username:{username}&language=english&route=p&numbers={phone}"
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            newrow=["001",name,age,gender,phone,email,username,password]
            usheet.insert_row(newrow,2)
            Snackbar(
                text="Account created successfully. Login to continue",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            sm.current = 'loginpage'


    def track(self):
        sm.add_widget(Overview(name='overview'))
        sm.current="overview"

    def viewteam(self):
        user=self.uname
        sm.add_widget(TeamStatus(name='teamstatus'))
        sm.current="teamstatus"

    def goback(self):
        sm.current="postlogin"
    def getrcount(self):
        c=rsheet.col_values(2)
        d=rsheet.col_values(3)
        id = {"Goa": 1, "Manali": 2, "Agra": 3}
        list = {'Goa': [], 'Manali': [], 'Agra': []}
        for i in range(len(c)):
            list[c[i]].append(d[i])

        return list
    def go(self,x):

        destination=x
        self.requestplaced=True
        list = self.getrcount()
        count = {"Goa": len(list['Goa']), "Manali": len(list['Manali']), "Agra": len(list['Agra'])}
        teamno=int((count[x]/4)+1)
        newrow = [teamno, destination,self.uname,self.phonenumber]
        rsheet.insert_row(newrow, 1)
        Snackbar(
            text="Request placed. Check team status",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current = 'postlogin'
        rsheet.sort(2,'asc')



        print(list,count)


MainApp().run()