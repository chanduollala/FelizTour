from datetime import datetime

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.card import MDCard
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
class AddTransaction(MDScreen):
    pass
class ContentNavigationDrawer(MDBoxLayout):
    pass

class DrawerList(ButtonBehavior, MDList):
    pass

class TeamStatus(MDScreen):
    pass

class Trans(ScrollView):
    pass
class TCard(MDCard):
    pass
currentscreen='helloscreen'
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



        sm.add_widget(NewTrip(name='newtrip'))


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
        sm.add_widget(LoginPage(name='loginpage'))
        sm.current = 'loginpage'
    def clear(self):
        self.welcome_label.text = "WELCOME"
        self.user.text = ""
        self.password.text = ""
    def overview(self):
        sm.current = 'overview'
    def transactions(self):
        t6 = tsheet.col_values(6)
        t5 = tsheet.col_values(5)
        t4 = tsheet.col_values(4)
        t3 = tsheet.col_values(3)
        t2 = tsheet.col_values(2)
        t1 = tsheet.col_values(1)
        print(t3, t2, t1)
        self.transactions = []

        for i in range(len(t2)):
            if t1[i] == self.teamname:
                self.transactions.append([t2[i],t3[i],t4[i],t5[i],t6[i]])

        for i in range(len(self.transactions)):
            self.money=self.transactions[i][1]
            self.paidby=self.transactions[i][0]
            self.purpose=self.transactions[i][2]
            self.category=self.transactions[i][3]

            self.paymenttime=self.transactions[i][4]


        #sm.add_widget(Transactions(name='transactions'))
        sm.current = 'transactions'
        l=MDLabel(text='hello')
        Transactions.add_widget(l)
    def plus(self, addtrs):
        sm.add_widget(AddTransaction(name='addtransaction'))
        sm.current = 'addtransaction'
        sm.remove_widget(sm.get_screen('overview'))
        sm.remove_widget(sm.get_screen('transactions'))
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
            sm.remove_widget(sm.get_screen('loginpage'))
            t4 = rsheet.col_values(4)
            t3 = rsheet.col_values(3)
            t2 = rsheet.col_values(2)
            t1 = rsheet.col_values(1)
            print(t3, t2, t1)
            team = []
            teamthere=False
            for i in range(0, len(t3)):
                if t3[i] == self.uname:
                    teamdes = t2[i]
                    teamno = t1[i]
                    print('user found')
                    teamthere=True
                    break

            if teamthere==True:

                for i in range(len(t2)):
                    if t2[i] == teamdes and t1[i] == teamno:
                        team.append([t3[i], t4[i]])
                self.team = team
                self.teamname = teamdes[0].upper() + str(teamno)
                print(self.teamname)
                print(self.team)
    def newtrip(self):
        sm.add_widget(NewTrip(name='newtrip'))
        sm.current = 'newtrip'
        sm.remove_widget(sm.get_screen('postlogin'))
    def signup(self):
        Snackbar(
            text="Enter your details",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        sm.add_widget(Signup(name='signup'))

        sm.current = 'signup'
        sm.remove_widget(sm.get_screen('loginpage'))
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
            sm.add_widget(LoginPage(name='loginpage'))
            sm.current = 'loginpage'
            sm.remove_widget(sm.get_screen('signup'))
    def track(self):
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))
        sm.current="overview"
    def viewteam(self):
        t4 = rsheet.col_values(4)
        t3 = rsheet.col_values(3)
        t2 = rsheet.col_values(2)
        t1 = rsheet.col_values(1)
        print(t3,t2,t1)
        team=[]
        for i in range(0, len(t3)):
            if t3[i] == self.uname:
                teamdes=t2[i]
                teamno=t1[i]
                print('user found')
                break
        for i in range(len(t2)):
            if t2[i]==teamdes and t1[i]==teamno:
                team.append([t3[i],t4[i]])
        self.team=team
        self.teamname=teamdes[0].upper()+str(teamno)
        print(self.teamname)
        print(self.team)
        if (len(self.team)==4):
            self.ready='Hurray! Your team is ready'
        else:
            self.ready='Oops! You need to wait for others to join'
        while(len(self.team)!=4):
            self.team.append(['', ''])
        sm.add_widget(TeamStatus(name='teamstatus'))
        sm.current="teamstatus"
        sm.remove_widget(sm.get_screen('postlogin'))
    def goback(self):
        x=sm.current
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current="postlogin"
        sm.remove_widget(sm.get_screen(x))
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
    def logout(self):
        x=sm.current
        sm.add_widget(LoginPage(name='loginpage'))
        sm.current = 'loginpage'
        sm.remove_widget(sm.get_screen(x))

    def addSubmit(self,amount,purpose,category):
        row=[self.teamname,self.uname,amount,purpose,category,datetime.now().strftime("%D %H:%M")]
        tsheet.insert_row(row,2)
        tsheet.sort(1,"asc")
        Snackbar(
            text="Transaction added successfully!!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))
        sm.current='overview'
        sm.remove_widget(sm.get_screen('addtransaction'))
    def setcategory(self,x):
        pass
MainApp().run()