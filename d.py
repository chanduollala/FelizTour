# SOURCE CODE FOR 'FELIZTOUR APP'
# Created by CHANDRASHEKAR OLLALA



# Kivy string that configures GUI.
import json
import webbrowser

from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.imagelist import SmartTile
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.utils.fitimage import FitImage

kv='''
<HelloScreen>:
    # Hello Screen is the screen which is displayed on app startup.

    Image:
        # It has background image embedded with App logo and author names.
        # Background image covers whole window of GUI.

        source:'logo.png'
        size_hint_x: 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}


    MDRaisedButton:
        # Button floating above background image.

        text: "Continue to APP"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.15}

        # On clicking on this button, continue_to_app() function from main will be executed.
        on_press: app.continue_to_app()



<LoginPage>:

    # Login Page is the screen which is displayed when use clicks on continue to app button in HelloScreen.

    MDCard:
        # This card is a white widget that remains in background.
        # All other widgets are placed above this card.

        size_hint: 0.8, 0.75
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDLabel:
        # This label prints 'Welcome' on top of screen.

        id: welcome_label
        text: "Welcome"
        font_size: 35
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDTextField:
        # Text Field to enter username for logging in.
        # Positioned below welcome label.

        id: user
        hint_text: "Username"
        icon_right: "account"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

    MDTextField:
        # Text Field to enter passsword for logging in.
        # Positioned below Username text field.

        id: password
        hint_text: "Password"
        icon_right: "eye-off"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        password: True

    MDRoundFlatButton:
        # Button positioned below username and password text fields.

        text: "Login"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        size_hint_x: 0.6

        # On clicking on this button, login() function from main will be executed.
        # Text entered in Username and Password text fields are passed as arguments.
        on_press: app.login(root.ids.user.text,root.ids.password.text)


    MDLabel:
        # This Label asks user if he is new to app.
        text: "New User? Signup!"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: 'center'
        size_hint_y: None
        padding_y: 15


    MDRoundFlatButton:
        # Button positioned below at bottom of the screen.

        text: "Signup"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.2}

        # On clicking on this button, login() function from main will be executed.
        on_press: app.signup()
        size_hint_x: 0.6

    # Collecion of widgets to create a content navigation drawer.
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:
        # On clicking top left button, a screen comes out that can be called as Drawer.
        # However, Drawer will not be there in Login screen.
        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "User Login"
                    elevation: 10
                    pos_hint: {"top": 1}

                    # There will be no items in Login page content drawer.
                    # There wil be no button on top left.
                    left_action_items:
                        []





<Signup>:
    # Signup Page is the screen which is displayed when user clicks on signup button in LoginScreen.
    # This screen takes user input to fill all the details of the user to store it to database.

    MDCard:
        # This blank Card is displayed in the background.

        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDTextField:

        # This text field asks for Name of the new user.
        # The text entered in this field can be accessed by the name 'signup_name.text'.
        # Text will be validated for text-only input.

        id: signup_name
        hint_text: "Name"
        size_hint_x: 0.7
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.75}


    MDTextField:
        # This text field asks for Age of the new user.
        # The text entered in this field can be accessed by the name 'signup_age.text'.
        # Text will be validated for number-only input between 10 to 100.

        id: signup_age
        hint_text: "Age"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.65}
        max_text_length: 2
        input_type: 'number'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDTextField:
        # This text field asks for Gender of the new user.
        # The text entered in this field can be accessed by the name 'signup_gender.text'.
        # Text will be validated for some keywords only.

        id: signup_gender
        hint_text: "Gender"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.55}
        required: True
        helper_text_mode: "on_error"
        helper_text: "M/F"



    MDTextField:
        # This text field asks for Phone number of the new user.
        # The text entered in this field can be accessed by the name 'signup_phn.text'.
        # Text will be validated for number-only input of 10-digit length.

        id: signup_phn
        hint_text: "Phone number"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.45}
        helper_text_mode: "on_error"
        helper_text: "Enter 10-digit phone number"

    MDTextField:

        # This text field asks for Email of the new user.
        # The text entered in this field can be accessed by the name 'signup_email.text'.
        # Text will be validated for format of email.

        id: signup_email
        hint_text: "Email"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.35}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDTextField:

        # This text field asks for setting password.
        # The text entered in this field can be accessed by the name 'signup_password.text'.

        id: signup_password
        hint_text: "Set Password"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.25}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDRoundFlatButton:
        # Button positioned bottom of the screen.

        text: "Submit"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7

        # On clicking on this button, signupSubmit() function from main will be executed.
        # Text entered in all text fields are passed as arguments.

        on_press: app.signupSubmit(root.ids.signup_name.text,root.ids.signup_age.text,root.ids.signup_gender.text,root.ids.signup_phn.text,root.ids.signup_email.text,root.ids.signup_password.text)


    # Collecion of widgets to create a content navigation drawer.
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:
                # On clicking top left button, a screen comes out that can be called as Drawer.
                MDToolbar:
                    title: "Signup "
                    elevation: 10
                    pos_hint: {"top": 1}

                    # There will be a button on top left.
                    # Clicking on it logs the user out and returns to login page.
                    left_action_items:
                        [['menu', lambda x: app.logout()]]



<PostLogin>:
    # Dashbard screen or post login screen is the screen which is displayed after successful login.
    # This screen displays three options for user to continue.

    MDLabel:
        # Label displayed at top of the screen.
        # Navigation for Plan New Trip button.
        text: "Planning for a Trip this week?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        # Placed below new trip label.

        text: "Plan new trip"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

        # On clicking on this button, newtrip() function from main will be executed.

        on_press: app.newtrip()


    MDLabel:
        # Label displayed middle of the screen.
        # Navigation for View Team button.
        text: "Already Registered?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        # Placed below Already registered? label.

        text: "Check your team status"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        # On clicking on this button, viewteam() function from main will be executed.

        on_press: app.viewteam()

    MDLabel:
        # Label displayed bottom of the screen above a button.
        # Navigation for Track Expenses button.

        text: "Trip Started?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        # Placed below bottom of the screen.

        text: "Track expenses"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        # On clicking on this button, track() function from main will be executed.

        on_press: app.track()

    # Collecion of widgets to create a content navigation drawer.

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:
                # On clicking top left button, a screen comes out that can be called as Drawer.
                MDToolbar:
                    title: "Hi "+ app.uname
                    elevation: 10
                    pos_hint: {"top": 1}
                    # There will be a button on top left.
                    # Clicking on this button opens the navigation drawer containing a button.
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer

            # Content Navigation drawer appears when top left button is clicked.
            ContentNavigationDrawer:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height:

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDRaisedButton:
                            # Theere will be a LOGOUT button in navigation drawer.
                            # Clicking on it logs the user out and returns to login page.
                            text: "LOG OUT"
                            font_size: 40
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            on_press: app.logout()
<Trans>:
    # This is a Box Layout.
    orientation: 'horizontal'





<TCard>:
    # This is a user defined card widget. Used to create multiple cards of same layout.
    # Each TCard added represents a transaction.
    id: tcard
    orientation: "vertical"
    size_hint: 1, None
    height: box_top.height + box_bottom.height
    focus_behavior: True
    ripple_behavior: True
    pos_hint: {"center_x": .5, "center_y": .5}
    # Useually, a MDCard allows user to embed widgets into it.
    # So, we are embedding a MDBoxLayout into MDCard.
    # We will add all the labels into MD BoxLayout.
    MDBoxLayout:
        id: box_top
        spacing: "20dp"
        adaptive_height: True


        # A nested MDBoxLayout
        MDBoxLayout:
            id: text_box
            orientation: "vertical"
            adaptive_height: True
            spacing: "10dp"
            padding: 0, "10dp", "10dp", "10dp"

            MDLabel:
                # This Label displays the amount spent of the transaction.
                text: app.money
                theme_text_color: "Primary"
                font_style: "H5"
                bold: True
                adaptive_height: True

            MDLabel:
                # This Label displays the person name who paid for the transaction and payment time.

                text: app.paidby+"    "+app.paymenttime
                adaptive_height: True
                theme_text_color: "Primary"

    MDSeparator:

    MDBoxLayout:
        id: box_bottom
        adaptive_height: True
        padding: "10dp", 0, 0, 0

        MDLabel:
            # This Label displays the purpose of the transaction.

            text: app.purpose
            adaptive_height: True
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"


<NewTrip>:

    # NewTrip screen is the screen which is displayed when user selects plan new trip button in Dashboard screen.
    # This screen displays three destinations for user to continue(can be upgraded in future versions).


    ScrollView:
        # Three destination details along with images are embedded in a scrollView.
        # Three destination details are aligned side by side.
        # User can scroll horizontally to view the destination details and select them.
        do_scroll_x: True
        do_scroll_y: False
        size_hint: 0.95,0.87
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        GridLayout:
            # Three destination details are aligned side by side.
            cols: 4
            size_hint_x: 3
            MDCard:
                # This MDCard gives details of Goa Trip Destination and has a button to select.
                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    # This image displays Goa and Has image in background.
                    source:'goa.png'
                    size_hint_y: .55
                    pos_hint:{"center_x": 0.5, "center_y": 0.5}

                MDLabel:
                    # This label diaplays title Goa.
                    # This label is placed below Goa Image.
                    text: "Goa"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    # This label displays detail about distance.
                    # This label is placed below Goa Heading.

                    text: "India, 691 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays 'estimated cost'.
                    # This label is placed below distance detail.

                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays the estimated cost of Trip.
                    # This label is placed at bottom above Go button.

                    text: "Rs.25000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    # This button is situated at the bottom of the screen in the Goa details section.
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    # On clicking on this button, go() function from main will be executed.
                    # As this button is situated in Goa Destination details, 'Goa' is passed as argument.

                    on_press: app.go("Goa")
            MDCard:
                # This MDCard gives details of Manali Trip Destination and has a button to select.

                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    # This image displays Manali and has image in background.

                    source:'manali.png'
                    size_hint_y: .55

                    pos_hint:{"center_x": 0.5, "center_y": 0.5}



                MDLabel:
                    # This label diaplays title Mnali.
                    # This label is placed below Manali Image.
                    text: "Manali"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    # This label displays detail about distance.
                    # This label is placed below Manali Heading.

                    text: "India, 2126 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays 'estimated cost'.
                    # This label is placed below distance detail.

                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays the estimated cost of Trip.
                    # This label is placed at bottom above Go button.

                    text: "Rs.35000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    # Button situated at bottom of the page in the Manali details section.
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    # On clicking on this button, go() function from main will be executed.
                    # As this button is situated in Manali Destination details, 'Manali' is passed as argument.

                    on_press: app.go("Manali")

            MDCard:
                # This MDCard gives details of Agra Trip Destination and has a button to select.

                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    # This image displays Agra and has image in background.

                    source:'agra.png'
                    size_hint_y: .55

                    pos_hint:{"center_x": 0.5, "center_y": 0.5}



                MDLabel:
                    # This label diaplays title Agra.
                    # This label is placed below Agra Image.

                    text: "Agra"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    # This label displays detail about distance.
                    # This label is placed below Agra Heading.

                    text: "India, 1341 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays 'estimated cost'.
                    # This label is placed below distance detail.

                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    # This label displays the estimated cost of Trip.
                    # This label is placed at bottom above Go button.

                    text: "Rs.15000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    # Button situated bottom of screen in Agra details section.
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    # On clicking on this button, go() function from main will be executed.
                    # As this button is situated in Agra Destination details, 'Agra' is passed as argument.

                    on_press: app.go("Agra")

    # Collecion of widgets to create a content navigation drawer.
    MDNavigationLayout:

        ScreenManager:

            MDScreen:
                # On clicking top left button, a screen comes out that can be called as Drawer.

                MDToolbar:
                    title: "Plan new trip"
                    elevation: 10
                    pos_hint: {"top": 1}
                    # There will be a button on top left.
                    # Clicking on this button opens the navigation drawer containing a button.

                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer
            # Content Navigation drawer appears when top left button is clicked.

            ContentNavigationDrawer:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height:

                MDLabel:
                    text: "FelizTour"
                    font_style: "Button"
                    size_hint_y: None




                ScrollView:

                    DrawerList:
                        id: md_list

                        MDFlatButton:
                            # Theere will be a goback button in navigation drawer.

                            text: "Go to home page"
                            font_size: 25
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            # Clicking on this button returns to user to dashboard.

                            on_press: app.goback()




<TeamStatus>:
    # TeamStatus screen is the screen which is displayed when user selects view team status button in Dashboard screen.
    # This screen displays the team name assigned and co-teammates and their phonenumbers.

    MDRoundFlatButton:
        # This button is situated at the bottom of the screen.

        text: "Go Back"
        font_size: 28
        size_hint_x: 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        # Clicking on this button returns to user to dashboard.

        on_press: app.goback()

    MDLabel:
        # This label displays name of team assigned to user.
        text: "Your Team: "+app.teamname
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        halign: 'center'


    MDCard:
        # This card contains names of members of the team which is assigned to user.
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.27, "center_y": 0.55}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            # This label displays name of first member of the team.

            text: app.team[0][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
             # This label displays name of second member of the team.
            text: app.team[1][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays name of third member of the team.
            text: app.team[2][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays name of fourth member of the team.
            text: app.team[3][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDCard:
        # This card contains phone numbers of members of the team which is assigned to user.
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.73, "center_y": 0.55}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            # This label displays phone number of first member of the team.
            text: app.team[0][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays phone number of second member of the team.

            text: app.team[1][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays phone number of third member of the team.

            text: app.team[2][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays phone number of fourth member of the team.

            text: app.team[3][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDLabel:
        # This label prints if the team is ready to go or not.
        # This prints 'Hurray! Team is ready!' if team has 4 members.
        # This prints 'Oops need to wait for others to join' if team has less than 4 members.
        text: app.ready
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: 'center'

    # Collecion of widgets to create a content navigation drawer.
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Team Status"
                    elevation: 10
                    pos_hint: {"top": 1}

                    # Theere will be a goback button on top left.
                    # On clicking this button, user is returned to dashboard.
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer

            # Content Navigation drawer appears when top left button is clicked.

            ContentNavigationDrawer:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height:

                MDLabel:
                    text: "KivyMD library"
                    font_style: "Button"
                    size_hint_y: None


                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None


                ScrollView:

                    DrawerList:
                        id: md_list

                        MDFlatButton:
                            text: "LOG IN"
                            font_size: 12
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            on_press: app.login()




<Overview>:
    # Overview screen is the screen which is displayed when user selects track expenses button in Dashboard screen.
    # This screen displays the spending analysis of team.

    MDRaisedButton:
        # This Button is placed on top right of the screen.
        # This is like a tab in Transactions Section.

        text: "Overview"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        size_hint: 0.5,0.075
        # This button refreshes overview screen when clicked in overview screen.
        on_press: app.overview()
        border: 'yellow'

    MDFlatButton:
        # This Button is placed on top left of the screen.
        # This is like a tab in Transactions Section.

        text: "Transactions"
        font_size: 18
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        # On clicking this button, transactions() method from main will be executed.
        on_press: app.transactions()
        size_hint: 0.5,0.075


    MDCard:
        # This card displays names of persons in team.
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.27, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            # This label displays name of first member of team.
            text: app.team[0][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays name of second member of team.
            text: app.team[1][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays name of third member of team.
            text: app.team[2][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays name of fourth member of team.
            text: app.team[3][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        # This card displays spends of each member in the team.
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.73, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            # This label displays money spent by first member of team.
            text: str(app.spends[app.team[0][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays money spent by second member of team.
            text: str(app.spends[app.team[1][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays money spent by third member of team.
            text: str(app.spends[app.team[2][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays money spent by fourth member of team.
            text: str(app.spends[app.team[3][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDCard:

        # This card displays categories of spends.
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.27, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            # This label displays 'Food'.

            text: 'Food'
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays 'Utilities'.
            text: "Utilities"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays 'Travelling'.
            text: "Travelling"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays 'Parties'.
            text: "Parties"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            # This label displays 'Others'.
            text: "Others"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDCard:
        # This card displays categories of spends.
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.73, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            # This label displays amount of money spent on Food.
            text: str(app.cwisespends["Food"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays amount of money spent on Utilities.

            text: str(app.cwisespends["Utilities"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays amount of money spent on Travelling.

            text: str(app.cwisespends["Travelling"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays amount of money spent on Parties.

            text: str(app.cwisespends["Parties"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            # This label displays amount of money spent on Other purposes.

            text: str(app.cwisespends["Others"])
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDFloatingActionButtonSpeedDial:
        # This is a Floating Button.
        # This is situated at bottom left of the screen.
        # Clicking on this button navigates to Add Transaction screen.

        data: app.data
        rotation_root_button: True
        callback: app.plus


    # Collecion of widgets to create a content navigation drawer.
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:
            # On clicking top left button, a screen comes out that can be called as Drawer.

            MDScreen:

                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}
                    # Theere will be a goback button on top left.
                    # On clicking this button, user is returned to dashboard.
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer


            ContentNavigationDrawer:
                # Content Navigation drawer appears when top left button is clicked.

                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height:

                MDLabel:
                    text: "KivyMD library"
                    font_style: "Button"
                    size_hint_y: None

                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None

                ScrollView:
                    # Contents of navigation drawer are placed in a scroll view.
                    DrawerList:
                        id: md_list

                        MDFlatButton:
                            text: "LOG IN"
                            font_size: 12
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}

                            on_press: app.login()

<Transactions>:
    # Overview screen is the screen which is displayed when user clicks on Transactions button in Overview screen.
    # This screen displays all the transactions done by team.
    MDRaisedButton:
        # This Button is placed on top left of the screen.
        # This is like a tab in Transactions Section.
        text: "Transactions"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        size_hint: 0.5,0.075
        # This button refreshes transactions screen when clicked in transactions screen.

        on_press: app.transactions()
        border: 'yellow'

    MDFlatButton:
        # This Button is placed on top right of the screen.
        # This is like a tab in Transactions Section.
        text: "Overview"
        font_size: 18
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        # On clicking this button, track() method from main will be executed.
        on_press: app.track()
        size_hint: 0.5,0.075

    ScrollView:
        # The screen excluding Navigation Heading and Buttons is placed in Scroll view.
        # This scroll view contains all the tcards, each representing one transaction.
        id: scroll
        do_scroll_x: False
        do_scroll_y: True
        size_hint: 1,0.80
        pos_hint: {"center_x": 0.5275, "y": 0}

        MDList:
            # MDList is added with all the TCards in transactions method in main.
            id: box
            spacing: 20


    MDFloatingActionButtonSpeedDial:
        # This is a Floating Button.
        # This is situated at bottom left of the screen.
        # Clicking on this button navigates to Add Transaction screen.

        data: app.data
        rotation_root_button: True
        callback: app.plus

    # Collecion of widgets to create a content navigation drawer.

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:
            # On clicking top left button, a screen comes out that can be called as Drawer.            MDScreen:
            MDScreen:

                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}

                    # There will be a goback button on top left.
                    # On clicking this button, user is returned to dashboard.
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


<Weather>:
    MDLabel:
        text: "The weather details at "+app.destination+" is: "
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.90}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Current Temperature:'+str(app.current_temperature)
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.80}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Humidity:'+str(app.humidity)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.70}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Minimum Temperature:'+str(app.tempmin)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Maximum Temperature:'+str(app.tempmax)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.60}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: "The location details of "+app.destination+" is :"
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.50}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: 'Latitude:'+str(app.latitude)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.40}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDLabel:
        text: 'Longitude:'+str(app.longitude)
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        text: "Go to Home Page"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        on_press: app.goback()







<AddTransaction>
    # AddTransaction screen is the screen which is displayed when user clicks on Floating add transaction button in Overview screen or Transactions screen.
    # This screen allows user to enter details of transaction made and save it.
    MDCard:
        # This card is displayed in the Background.
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
    MDTextField:
        # This TextField takes user input for amount spent in the transaction.
        # This text entered in this TextField can be accessed as 'amount.text'
        id: amount
        hint_text: "Amount"
        size_hint_x: 0.7
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter Amount"
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.75}


    MDTextField:
        # This TextField takes user input for purpose of the transaction.
        # This text entered in this TextField can be accessed as 'purpose.text'
        id: purpose
        hint_text: "Purpose"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.65}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter purpose"


    MDLabel:
        # This label displays 'select purpose'.
        # This label is situated middle of the screen.
        id: category
        text: 'select purpose'
        font_size: 15
        halign: left
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        halign: 'center'

    MDLabel:
        # This label displays 'Food'.
        text: "Food"
        font_size: 20
        pos_hint: {"center_x": 0.50, "center_y": 0.5}
        size_hint_x: 0.5
        halign: 'left'

    MDCheckbox:
        # This check box is located next to Food Label.
        # On checking this checkbox, on_checkbox_active() method from main is executed.
        # 'Food' is passed as argument to the method.

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .5}
        on_active: app.on_checkbox_active('Food')

    MDLabel:
        # This label displays 'Utilities'.
        text: "Utilities"
        font_size: 20
        pos_hint: {"center_x": 0.50, "center_y": 0.42}
        size_hint_x: 0.5
        halign: 'left'

    MDCheckbox:
        # This check box is located next to Utilities Label.
        # On checking this checkbox, on_checkbox_active() method from main is executed.
        # 'Utilities' is passed as argument to the method.

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .42}
        on_active: app.on_checkbox_active('Utilities')

    MDLabel:
        # This label displays 'Travelling'.
        text: "Tranvelling"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        size_hint_x: 0.5
        halign: 'left'

    MDCheckbox:
        # This check box is located next to Travelling Label.
        # On checking this checkbox, on_checkbox_active() method from main is executed.
        # 'Travelling' is passed as argument to the method.

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .35}
        on_active: app.on_checkbox_active('Travelling')

    MDLabel:
        # This label displays 'Parties'.
        text: "Parties"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.27}
        size_hint_x: 0.5
        halign: 'left'

    MDCheckbox:
        # This check box is located next to Parties Label.
        # On checking this checkbox, on_checkbox_active() method from main is executed.
        # 'Parties' is passed as argument to the method.

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .27}
        on_active: app.on_checkbox_active('Parties')

    MDLabel:
        # This label displays 'Others'.
        text: "Others"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        size_hint_x: 0.5
        halign: 'left'

    MDCheckbox:
        # This check box is located next to Others Label.
        # On checking this checkbox, on_checkbox_active() method from main is executed.
        # 'Others' is passed as argument to the method.

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .20}
        on_active: app.on_checkbox_active('Others')



    MDRaisedButton:

        # This button is situated at the bottom of the screen.
        text: "Add"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        # On clicking on this button, addSubmit() method from main is executed.
        # Texts entered in amund and purpose textfields are passed as arguments.
        on_press: app.addSubmit(amount.text,purpose.text)

    # Collecion of widgets to create a content navigation drawer.

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:
            # On clicking top left button, a screen comes out that can be called as Drawer.

            MDScreen:

                MDToolbar:
                    title: "Add Transaction"
                    elevation: 10
                    pos_hint: {"top": 1}
                    # There will be a goback button on top left.
                    # On clicking this button, user is returned to dashboard.
                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer


            ContentNavigationDrawer:

                # Content Navigation drawer appears when top left button is clicked.
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height:

                MDLabel:
                    text: "KivyMD library"
                    font_style: "Button"
                    size_hint_y: None


                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None

                ScrollView:
                    # Contents of navigation drawer are placed in a scroll view.
                    DrawerList:
                        id: md_list

                        MDFlatButton:
                            text: "LOG IN"
                            font_size: 12
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            # On clicking this button, user is returned to login page.
                            on_press: app.login()

'''








# Kivy package implements Graphical User Interface(GUI).
import kivy
# Builder loads the GUI configuration file ( .kv extension) or string.
from kivy.lang import Builder
# KivyMD is extended version of Kivy.
# It provides GUI.
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
from kivymd.uix.list import MDList, IRightBodyTouch
from kivymd.uix.snackbar import Snackbar
from kivy.properties import ObjectProperty
# datetime module is used to get current time and date.
from datetime import datetime
from kivy.metrics import dp
import os
from matplotlib import pyplot as plt
from geopy.geocoders import Nominatim

#Configuring Google Drive API and Google Spreadsheets API.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']



# Credentials used to create a client to interact with the Google Drive API.

# File named 'apifile.json' has credentials of Google Developer account used to authorise APIs.
# Contents of api.json file

#   {
#     "type": "service_account",
#     "project_id": "gold-atlas-326210",
#     "private_key_id": "a77d1d86cfa5e49d03143ce2eecc92b4b67d6b62",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMg0kkbZ4LhzAv\nDSmiwLecF3sYrUed8V6yFozwLgQZkiGpLYWYALcPHfZ0dTIJudymUKEgOtljMlpV\nY1ijKQkPu3w2WN7Cbb/j/gI7egt6seCwTIdhaEcVBSfPNTKNGSE+oYEaMoZu+Ra8\nrU+BqT1QA34m5UbyoSJfS6q6rsWPda4XdzHsS491o1t5sqrHtzEn4y5BZQTpRQJR\n05TIcBAc7z2dE1nNJZ00qryPBrI8JMm+OTzxyk+EjLnuGkeZBGD9qWNMpvGqw0zf\nEK2SPJYTbrJbC9b+lMMEU6r97nkf2iru2VMJyCAt9sA1zZZihVH+1oatK1VTKmWD\nD0q7lor9AgMBAAECggEAW0BxEFoA3O/zJetfmokW5ATuHfKjM+wQ7rF1LW260pYL\ngusW4t3e0FX0M75fF0vhEiyD2Fepy8MZ32O2lwamTmi/YZiBvIsvxdD+uf8YxCQ+\nNyvOdD4NCWoFe0UnSyHdXY6+hivpI/bsmD9UbGxROTR1w3EmGPig15hxk16MNBfn\nep8oaFRWXn6gdojfKbPQOJwzTCjNdWN27KlC9H4jz1ZHmJtIbP7ykyVTCvB9U6cE\nJY92E11tROKlACVRwmRX4lBIrF5PSb4hcwUStyefjTWnHHdTbDv5ieKZXV/KrbT5\ngrmJtuSdgNXNYTtKTOFA57gRRzzQpuYOU5svtr4w2QKBgQD0B1Y18vOUD6jhsxKY\n7IkoaYOMAS3C/84AN/Lx4mEvnDI5HBu5EH/svpwJ9eilujPBcoQ/B+oQWISxalLv\nq2WZhbOEahDGSYSRvCk3aJQdobhe74EwqK9UpQdCPWEEH0+xo6VQmIuofuyD74Do\ntW2YSJHDxGsEc2csiGy4xzh1NwKBgQDWi69J9r7t38NC3/L+zSEGjSJnyPF4Pazl\n+v1oNd9R1/e8HRIFwwItCY38pEHaQV13wN0Swneo2p1waBgUHj3znuYsg7s9OJyR\nsygf9q+tk6/PRzTbN3z91736wq21UTnICN6hqnzqNyBh7XPio7qvJUAB9ySS4sAc\n3MlOXsVbawKBgQDaQ/2uP2HyWpdZWIwXz+lWBhotDZjaw2aD94cLJsp6hSC+yA9b\n1hA1tr9mgVbXdNZ5/m2e2vtWJ3Z4IXuQ9yLm0BmjJCNg170FhODwuE9SuaVo9Jv+\n48H+2aTGcJPn1gG4B4EDt42i5fOyhnQssKoX/UCzc2mtD3OG93cXRsmOvQKBgAVB\nFIDmNxTSRxDrNSNCWM21RSNvi2JbeFGFjRExSI/TjzCfMaLMfNAnjL+kMiyrLyPQ\nqFleQ9nxyKtJEVXky7WcrZxneX1tVoBG9/OYcgL5O/QClWvM9xWsY+2xONnY7GZW\nuUUSTM7bnMJpM05YnijN67xglhe2z+elDJULwx+TAoGACGFwFcWFB4YUHRZhtHs1\nPHqHoPgJDi3v3L5100JGQx6QB6ujfcDpcrXL8eIbtP7/+Oftuiwcn0tYHQoIX4aZ\nDBo8GDRPZ8kzotDIk4z8xMH5Xu1tqCywnmL3nia77V02qqLGgQkI+AlpWBE/Isj1\nJGE5xgVvuY8+59OoFGy9eIE=\n-----END PRIVATE KEY-----\n",
#     "client_email": "chandu@gold-atlas-326210.iam.gserviceaccount.com",
#     "client_id": "117609925135611496821",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/chandu%40gold-atlas-326210.iam.gserviceaccount.com"
#   }

# Credentials belong to Chandrashekar Ollala. Not to be misused.
creds = ServiceAccountCredentials.from_json_keyfile_name('apifile.json', scope)
client = gspread.authorize(creds)



# Mentioning spreadsheets saved in Drive cloud of Chandrashekar Ollala.
# Four sheets are used to store and verify data.

usheet = client.open("FelizTourUsers").sheet1
tsheet= client.open("FelizTourTransactions").sheet1
rsheet= client.open("FelizTourTripRequests").sheet1
msheet= client.open("FelizTourTeams").sheet1


# Fast2SMS API is used to send One-Time Passwords to Users when they signup.
# Configuring Fast2SMS API using requests module.

import requests
url = "https://www.fast2sms.com/dev/bulk"

headers = {
'authorization': "aWmyldGXYkqTQFo9cb5K1st6geJARZ4uLnP2jVEMH0Sr3DziIxWviBmqXgeTV25xcwFjdaPsZERk8G9D",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}


# Regular Expressions are used in app to verify the pattern of email and phone number input.
import re

Window.size = (530,620)

# Builder loads GUI configuration string saved as kv.
Builder.load_file("file.kv")

# Screen Manager is used to switch between different screens.
sm = ScreenManager()



# Screens and Widgets mentioned as classes.

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


class MySwiperItem(MDSwiperItem):
    pass

class Signup(MDScreen):
    pass

class NewTrip(MDScreen):
    pass

class Destinations(MDScreen):
    pass

class PlaceDetails(MDScreen):
    pass

class Weather(MDScreen):
    pass

class OpenMaps(MDRaisedButton):
    pass

class OpenWhatsapp(MDRaisedButton):
    pass

class DismissButton(MDFlatButton):
    pass

class DismissButtonB(MDRaisedButton):
    pass

class AddTransaction(MDScreen):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass

class DrawerList(ButtonBehavior, MDList):
    pass

class TeamStatus(MDScreen):
    pass

class Trans(MDBoxLayout):
    def addcard(self):
        p=TCard()

class TCard(MDCard):
    pass

class Tab1(MDFloatLayout,MDTabsBase):
    pass

class RightCheckBox(IRightBodyTouch, MDCheckbox):
    pass

class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class Spinner(MDSpinner):
    pass


# Global variables.
userdetails=[]
currentscreen='helloscreen'

# Main App Class that runs GUI.

class MainApp(MDApp):

    # Data for action button in transactions screen and overview screen.
    data = {
        'Add Transaction': 'Addtrs',
        "hi": "hello"
    }

    # Default display name.
    displayname="User"

    # main method of GUI.


    def build(self):

        LabelBase.register(
            name="Dongle",
            fn_regular="Dongle-Regular.ttf")

        theme_font_styles.append('Dongle')
        self.theme_cls.font_styles["Dongle"] = [
            "Dongle",
            16,
            False,
            0.15,
        ]

        # Setting display theme for GUI.
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"

        # Adding screens (HelloScreen and New Trip)
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(NewTrip(name='newtrip'))

        self.tap_target_view=MDTapTargetView(widget=sm,
                    title_text="Location ",
                    description_text="This is a description\n of the button",
                    widget_position="left_bottom",)

        # Current screen set to HelloScreen.(on app start).

        sm.current = 'helloscreen'

        self.loading=False



        return sm

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        pass

    def weather(self,destination):
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + destination + "&units=metric&appid=" + 'bb9c06a29f2282c6d4b8606cc12d874c')

        api = json.loads(api_request.content)

        # Temperatures
        y = api['main']
        self.current_temperature = y['temp']
        self.humidity = y['humidity']
        self.tempmin = y['temp_min']
        self.tempmax = y['temp_max']

        # Coordinates
        x = api['coord']
        self.longitude = x['lon']
        self.latitude = x['lat']

        # Country
        z = api['sys']
        self.country = z['country']
        self.citi = api['name']
        '''search = f"weather in {self.destination}"
        url=f"https://www.google.com/search?&q={search}"
        url2=f"https://in.search.yahoo.com/search?p=weather%20in%20hyderabad"
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        update=s.find("div",class_="BNeawe").text
        self.temp=update

        '''
        sm.add_widget(Weather(name='weather'))
        sm.current = 'weather'

    # Method to validate Login credentials entered by verifying.

    # Userdetails global variable is updated only if Username is found and Entered Password matches with correct password.
    def navigate(self):
        self.dialog = MDDialog(
            text="This takes you to Google Maps. Do you wish to continue?",
            buttons=[
                DismissButton(),
                OpenMaps(),
            ],
        )
        self.dialog.open()

    def gotomap(self):
        webbrowser.open("https://www.google.com/maps/dir/Your+location/"+self.destination+"/")


    def calculate(self):


        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")

        # entering the location name
        getLoc = loc.geocode("Gosainganj Lucknow")

        # printing address
        location=str(getLoc.address)+"\n"+"Latitude = "+str(getLoc.latitude)+"\nLongitude = "+str(getLoc.longitude)

        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                   + self.desplace + "&units=metric&appid=" + 'bb9c06a29f2282c6d4b8606cc12d874c')

        api = json.loads(api_request.content)

        # Temperatures
        y = api['main']

        weather=f"Current Temperature:\t{y['temp']}\nHumidity:\t{y['humidity']}\nMinimum Temperature:  {y['temp_min']}\nMaximum Temperature:  {y['temp_max']}"

        import googlemaps
        try:
            # Requires API key
            gmaps = googlemaps.Client(key='AIzaSyAYOoO_A2xUECEXmkeI7kLEqYAPNz8JF84')

            # Requires cities name
            my_dist = gmaps.distance_matrix('Peddapalli', self.desplace)['rows'][0]['elements'][0]

            # Printing the result
            distance=my_dist['distance']['text']
            duration=my_dist['duration']['text']
        except googlemaps.exceptions.ApiError:
            distance="1984 km"
            duration="38 hours"



        return location,weather,distance,duration

    def generatetaptarget(self, requested):

        location,weather,distance,duration=self.calculate()

        if requested=="location" and self.tap_target_view.state=="close":

            self.tap_target_view = MDTapTargetView(
                widget=sm.get_screen("placedetails").ids.location,
                title_text="Location details of "+self.desplace,
                description_text=location,
                widget_position="left_top",
            )

        if requested=="weather" and self.tap_target_view.state=="close":

            self.tap_target_view = MDTapTargetView(
                widget=sm.get_screen("placedetails").ids.weather,
                title_text="Weather condition at "+self.desplace,
                description_text=weather,
                widget_position="right_top",
            )

        if requested=="distance" and self.tap_target_view.state=="close":

            self.tap_target_view = MDTapTargetView(
                widget=sm.get_screen("placedetails").ids.distance,
                title_text="Distance from your location to "+self.desplace,
                description_text=distance,

                widget_position="top",
            )

        if requested=="time" and self.tap_target_view.state=="close":

            self.tap_target_view = MDTapTargetView(
                widget=sm.get_screen("placedetails").ids.time,
                title_text="Journey Duration from your \ncurrent location to "+self.desplace,
                description_text=duration,
                widget_position="top",
            )

    def taptarget(self,requested):

        if self.tap_target_view.state == "close":
            self.generatetaptarget(requested)
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

    def viewdestination(self,place,icon):

        self.desplace=place
        self.desicon=icon

        images={"Goa":[fr"C:\Users\chand\Documents\GitHub\FelizTour\images\goa{x}.png" for x in range(1,6)],"Agra":[fr"C:\Users\chand\Documents\GitHub\FelizTour\images\agra{x}.png" for x in range(1,5)],"Manali":[fr"C:\Users\chand\Documents\GitHub\FelizTour\images\manali{x}.png" for x in range(1,5)]}

        try:
            sm.remove_widget(sm.get_screen('placedetails'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        sm.add_widget(PlaceDetails(name="placedetails"))
        sm.current="placedetails"



        for image in images[place]:

            self.image=image
            p= MySwiperItem()


            sm.get_screen("placedetails").ids.swiperimages.add_widget(p)









    def validateuser(self,username,password):

        # gets all the usernames that are registered
        usernames=usheet.col_values(7)

        # Verifies the entered input with all usernames.


        if username not in usernames:

            # Username not found.
            # SnackBar is a widget that shows a dialogue by popping up from bottom of the screen.
            Snackbar(
                text="Username not found!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        else:
            # Username matched with one of the usernames in cloud.

            for i in range(0,len(usernames)):

                # Retrieves all the details of username found.

                if usernames[i]==username:
                    column=i
                    user_keys=usheet.row_values(1)
                    user_values=usheet.row_values(i+1)
                    userdetails= {user_keys[i]: user_values[i] for i in range(len(user_keys))}
                    print(userdetails)
                    print("user found")

                    # Validating Password.
                    if password==userdetails["password"]:

                        # Entered password matches with correct password.
                        return userdetails
                    else:

                        # Entered password doesn't mtch with correct password.
                        Snackbar(
                            text="Password incorrect",
                            snackbar_x="10dp",
                            snackbar_y="10dp",
                            size_hint_x=.95
                        ).open()

            return 0


    # Method to check Data entered during signup.
    # Entries are rejected if data entered doesn't match prescribed pattern.

    def checksignupdata(self,name,age,gender,phone,email,password):

        # Defining patterns for email, name and phone number.
        namepattern='^[a-zA-Z]([a-zA-Z\s]){0,}$'
        phonepattern='^[6-9]([0-9]){9}$'
        emailpattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Ensuring none of the fields are blank.
        if name=="" or age=="" or gender=="" or phone=="" or email=="" or password=="":
            Snackbar(
                text="Fields cant be empty",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        # Checking if name matches the pattern.
        if (re.match(namepattern,name)):

            # Name field met criteria.
            print(re.match(namepattern,name))
            pass
        else:
            # Name field did not meet criteria.
            print(re.match(namepattern, name))
            Snackbar(
                text="Name has only alphabets and spaces",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        # Checking if age falls in possible range.
        if (int(age)>10 and int(age)<100):

            # Age field met criteria.
            pass
        else:
            # Age field did not meet criteria.
            Snackbar(
                text="Age invalid!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        # Checking if gender is selected correctly.
        if (gender in ["male","female","Male","Female","M","F"]):

            # Gender entered is one of the given options.
            pass
        else:
            # Gender entered is not one of the given options.

            Snackbar(
                text="Gender: Invalid Input",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        # Checking if entered phonenumber matches the given pattern.
        if (re.match('^[0-9]([0-9]){9}$',phone)):
            # Phone number pattern matched.
            pass
        else:

            # Phone number pattered did not match.
            print(re.match(phonepattern, phone))
            Snackbar(
                text="Invalid Phone number",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0

        # Checking if entered email matches with the given pattern.
        if (re.match(emailpattern,email)):

            # Email pattern matched.
            pass
        else:
            # Email pattern did not match.
            Snackbar(
                text="Invalid Email",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
            return 0


        # All test cases passed.
        # Giving clearance for details to be saved in database.
        return "OK"

    # Method that runs when user clicks on Continue to app button in HelloScreen.
    def continue_to_app(self):

        self.loading=True

        # Creating new screen for Userlogin and setting current screen to login screen.
        sm.add_widget(LoginPage(name='loginpage'))
        sm.current = 'loginpage'

        self.dialog = MDDialog(
            text="App Information\n===============\nThis Application is developed by CHANDRASHEKAR OLLALA and SAHAJA REDDY P.\nSubmitted to Vasavi College of Engineering as part of MiniProject-1 -III Semester. \nThis app repository is available at:\nhttps://github.com/chanduollala/FelizTour",
            buttons=[
                DismissButtonB(),
            ],
        )
        self.dialog.open()

    def clear(self):
        self.welcome_label.text = "WELCOME"
        self.user.text = ""
        self.password.text = ""

    # Method that loads transactions screen
    def transactions(self):
        # Removing Transactions screen if it is already there as it needs to be reloaded.
        try:
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        # Getting values from Transactions Sheet(Google Drive).
        t6 = tsheet.col_values(6)
        t5 = tsheet.col_values(5)
        t4 = tsheet.col_values(4)
        t3 = tsheet.col_values(3)
        t2 = tsheet.col_values(2)
        t1 = tsheet.col_values(1)
        print(t3, t2, t1)

        # List to store the transactions.
        self.transactionsar = []

        # Filtering transactions related to team that contains current user.
        for i in range(len(t2)):
            if t1[i] == self.teamname:
                self.transactionsar.append([t2[i],t3[i],t4[i],t5[i],t6[i]])
        print(self.transactionsar)

        # Variable for .kv file.
        self.lenn = len(self.transactionsar) * 90

        # Creating Transactions screen again and setting it to current.
        sm.add_widget(Transactions(name='transactions'))
        sm.current = 'transactions'

        # Updating Overview Screen with reloaded details.

        # Removing Overview screen if already exists.
        try:
            sm.remove_widget(sm.get_screen('overview'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        # Loading variables for usage in GUI.
        for i in range(len(self.transactionsar)):
            self.money = self.transactionsar[i][1]
            self.paidby = self.transactionsar[i][0]
            self.purpose = self.transactionsar[i][2]
            self.category = self.transactionsar[i][3]

            self.paymenttime = self.transactionsar[i][4]

            # Adding each transaction as a card to transactions screen.
            # Class Tcard defines card that contains all details of a transaction
            l=TCard()
            sm.get_screen('transactions').ids.box.add_widget(l)



    # Method that executes when Add Transaction button is clicked.
    def plus(self):
        # Creating new Screen and setting it to current.
        sm.add_widget(AddTransaction(name='addtransaction'))
        sm.current = 'addtransaction'

        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png")
        else:
            print("The file does not exist")
        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png")
        else:
            print("The file does not exist")



    # Method that is executed when login button is clicked.
    # Username and Passsword entered are read and passsed as arguments.
    def login(self,username,password):

        # Calls validate user method.
        self.userdetails=self.validateuser(username,password)

        if self.userdetails!=0:
            # Setting variable for use in .kv file.
            self.uname=self.userdetails["Name"]
            self.phonenumber=self.userdetails["Phone"]
            self.loggedinusername=self.userdetails["Usename"]
            self.gender=self.userdetails["Gender"]
            self.uicon="alpha-"+self.uname[0].lower()+"circle"

            try:
                sm.remove_widget(sm.get_screen('postlogin'))

            except kivy.uix.screenmanager.ScreenManagerException:
                pass


            # Adding dashboard screen(Postlogin page)
            sm.add_widget(PostLogin(name='postlogin'))
            Snackbar(
                text="Logged in succesfully as "+self.uname,
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()



            # setting current screen to dashboard page.
            sm.current = 'postlogin'

            # Remove pre exixting login page.
            sm.remove_widget(sm.get_screen('loginpage'))

            # Reading trip requests sheet.
            t4 = rsheet.col_values(4)
            t3 = rsheet.col_values(3)
            t2 = rsheet.col_values(2)
            t1 = rsheet.col_values(1)
            print(t3, t2, t1)

            # List containing team member details.
            team = []
            teamthere=False

            # Finding team number of logged in user.
            for i in range(0, len(t3)):
                if t3[i] == self.uname:
                    teamdes = t2[i]
                    teamno = t1[i]
                    print('user found')
                    teamthere=True
                    break


            if teamthere==True:
                # Retrieving the details of co-team members.
                for i in range(len(t2)):
                    if t2[i] == teamdes and t1[i] == teamno:
                        team.append([t3[i], t4[i]])
                self.team = team
                self.teamname = teamdes[0].upper() + str(teamno)
                print(self.teamname)
                print(self.team)
                self.destination=teamdes

    # Method that is executed when new trip button is clicked.
    def newtrip(self):
        try:
            sm.remove_widget(sm.get_screen('destinations'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        # Add screen.
        # Set current screen to added screen.
        # Remove previous screen.
        sm.add_widget(Destinations(name='destinations'))
        sm.current = 'destinations'
        sm.remove_widget(sm.get_screen('postlogin'))


    # Method executed when signup button from login oage is clicked.
    def signup(self):
        self.dialog = MDDialog(
            text="Enter your Details and click Submit",
            buttons=[
                DismissButtonB(),
            ],
        )
        self.dialog.open()

        # Add signup screen.
        # Set current screen to signup screen.
        # Remove previous screen.
        sm.add_widget(Signup(name='signup'))

        sm.current = 'signup'
        sm.remove_widget(sm.get_screen('loginpage'))

    def chatwhatsapp(self,phone):
        self.whatsappno=phone
        self.dialog = MDDialog(
            text="This event takes you to Whatsapp. Do you wish to continue?",
            buttons=[
                DismissButton(),
                OpenWhatsapp(),
            ],
        )
        self.dialog.open()

    def gotowhatsapp(self):
        webbrowser.open("wa.me/+91" + self.whatsappno)


    def viewmemberdetails(self,name):

        names = usheet.col_values(2)

        for i in range(0, len(names)):

            # Retrieves all the details of name found.

            if names[i] == name:
                column = i
                user_keys = usheet.row_values(1)
                user_values = usheet.row_values(i + 1)
                userdetails = {user_keys[i]: user_values[i] for i in range(len(user_keys))}
                print(userdetails)
                print("user found")

                self.dialog = MDDialog(
                    title= "Team Member Details",
                    text=f"\nName:\t{userdetails['Name']} \nAge:\t{userdetails['Age']}\nGender:\t{userdetails['Gender']}\nPhone:\t{userdetails['Phone']}\nEmail:\t{userdetails['Email']}",
                    buttons=[
                        DismissButtonB(),
                    ],
                )
                self.dialog.open()
                break




    # Method that is executed when user clicks on submit button in signup screen.
    # All values entered as details are passed as arguments.
    def signupSubmit(self,name,age,gender,phone,email,password):

        # Checks if details are valid.
        x=self.checksignupdata(name,age,gender,phone,email,password)
        if x=="OK" and name!="" and age!="" and gender!="" and phone!="" and email!="" and password!="":

            # Generating username.
            username=name[:5]+phone[-3:]

            # Sending One-Time Password.
            payload = f"sender_id=FSTSMS&message=welcome to feliz tour. your username:{username}&language=english&route=p&numbers={phone}"
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)

            # Adding user details to users database.
            newrow=["001",name,age,gender,phone,email,username,password]
            usheet.insert_row(newrow,2)

            self.dialog = MDDialog(
                text="Account created successfully. Your username is sent through SMS. Please check your phone.",
                buttons=[
                    DismissButtonB(),
                ],
            )
            self.dialog.open()

            # Returning to login page after creating account successfully.
            sm.add_widget(LoginPage(name='loginpage'))
            sm.current = 'loginpage'
            sm.remove_widget(sm.get_screen('signup'))


    # Method that is executed when user clicks on Track expenses button or Overview Tab.
    def track(self):

        # Removing screen is it is already present.
        try:
            sm.remove_widget(sm.get_screen('overview'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        # Checking if user is enrolled in a trip and team is assigned.
        t4 = rsheet.col_values(4)
        t3 = rsheet.col_values(3)
        t2 = rsheet.col_values(2)
        t1 = rsheet.col_values(1)
        print(t3, t2, t1)
        team = []
        found = False
        for i in range(0, len(t3)):
            if t3[i] == self.uname:
                teamdes = t2[i]
                teamno = t1[i]
                print('user found')
                found = True
                break
        if found==True:
            # User is in a team.
            for i in range(len(t2)):
                if t2[i]==teamdes and t1[i]==teamno:
                    team.append([t3[i],t4[i]])
            self.team=team

            # Getting all values of transactions sheet.
            t6 = tsheet.col_values(6)
            t5 = tsheet.col_values(5)
            t4 = tsheet.col_values(4)
            t3 = tsheet.col_values(3)
            t2 = tsheet.col_values(2)
            t1 = tsheet.col_values(1)
            print(t3, t2, t1)
            self.transactionsar = []

            # Adding transactions related to current team to local list.
            for i in range(len(t2)):
                if t1[i] == self.teamname:
                    self.transactionsar.append([t2[i], t3[i], t4[i], t5[i], t6[i]])
            print(self.transactionsar)

            # Declaring dictionaries for storing spends.
            c=['Food','Utilities','Travelling','Parties','Others']
            self.cwisespends={"Food":0,"Utilities":0,"Travelling":0,"Parties":0,"Others":0}
            self.spends={self.team[0][0]:0,self.team[1][0]:0,self.team[2][0]:0,self.team[3][0]:0,}

            # Updating values of spends in every step.
            for i in range(len(self.transactionsar)):
                for j in range(len(self.team)):
                    if self.transactionsar[i][0]==self.team[j][0]:
                        # Analysing spends based on who spent how much.
                        self.spends[self.transactionsar[i][0]]=self.spends[self.transactionsar[i][0]]+int(self.transactionsar[i][1])
                for k in c:
                    if self.transactionsar[i][3]==k:
                        # Analysing spends based on category the spend belong to.
                        self.cwisespends[k]=self.cwisespends[k]+int(self.transactionsar[i][1])

            # Adding Overview Screen and set it to current.
            sm.add_widget(Overview(name='overview'))
            sm.current="overview"

            # Removing Transactions screen if already exits.(outdated).
            try:
                sm.remove_widget(sm.get_screen('transactions'))
            except kivy.uix.screenmanager.ScreenManagerException:
                pass

            self.namewisespend = MDDataTable(
                use_pagination=False,
                check=True,
                column_data=[
                    ("No.", dp(30)),
                    ("Name", dp(30)),
                    ("Money Spent", dp(60)),

                ],
                row_data=[
                    (
                        "1",
                        ("alpha-"+self.team[0][0][0].lower()+"-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                         self.team[0][0]
                         ),
                        self.spends[self.team[0][0]],
                    ),
                    (
                        "2",
                        ("alpha-" + self.team[1][0][0].lower() + "-circle",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                        self.team[1][0],
                         ),
                        self.spends[self.team[1][0]],
                    ),
                    (
                        "3",
                        ("alpha-" + self.team[2][0][0].lower() + "-circle",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                        self.team[2][0],
                         ),
                        self.spends[self.team[2][0]],
                    ),
                    (
                        "4",
                        ("alpha-" + self.team[3][0][0].lower() + "-circle",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                        self.team[3][0],
                         ),
                        self.spends[self.team[3][0]],
                    ),

                ],
                sorted_on="Money Spent",
                sorted_order="ASC",
                elevation=2,
            )
            sm.get_screen('overview').ids.overviewtab.add_widget(self.namewisespend)

            #name wise spends bargraph
            # creating the dataset
            data = {self.team[0][0]: self.spends[self.team[0][0]], self.team[1][0]: self.spends[self.team[1][0]],
                    self.team[2][0]: self.spends[self.team[2][0]],self.team[3][0]: self.spends[self.team[3][0]] }
            courses = list(data.keys())
            values = list(data.values())

            fig = plt.figure(figsize=(5, 3.5))

            self.catwisespend = MDDataTable(
                use_pagination=False,
                check=True,
                column_data=[
                    ("No.",dp(30)),
                    ("Category", dp(30)),
                    ("Money Spent", dp(60)),

                ],
                row_data=[
                    (
                        "1",
                        ("food",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                         "Food"
                         ),
                        self.cwisespends["Food"],
                    ),
                    (
                        "2",
                        ("bag-personal",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                         "Utilities"
                         ),
                        self.cwisespends["Utilities"],
                    ),
                    (
                        "3",
                        ("airplane",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                         "Travelling"
                         ),
                        self.cwisespends["Travelling"],
                    ),
                    (
                        "4",
                        ("party-popper",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                         "Parties"
                         ),
                        self.cwisespends["Parties"],
                    ),(
                        "5",
                        ("map-marker-question",
                         [39 / 256, 174 / 256, 96 / 256, 1],
                         "Others"
                         ),
                        self.cwisespends["Others"],
                    ),

                ],
                elevation=2,
            )
            sm.get_screen('overview').ids.catwisetab.add_widget(self.catwisespend)
            # creating the bar plot
            plt.bar(courses, values, color='maroon',
                    width=0.4)
            plt.ylabel("Amount")

            plt.savefig("namewise.png")

            tile1=Image(source=r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png",size_hint_y=0.45)
            sm.get_screen('overview').ids.overviewtab.add_widget(tile1)

            # Creating dataset
            categories = ["Food", 'Utilities', 'Travelling',
                    'Parties', 'Others']

            data = [self.cwisespends[x] for x in categories]

            # Creating plot
            fig = plt.figure(figsize=(5, 3.5))
            plt.pie(data, labels=categories)
            plt.savefig("catwise.png")

            tile2 = Image(source=r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png", size_hint_y=0.35)
            sm.get_screen('overview').ids.catwisetab.add_widget(tile2)

            # Loading variables for usage in GUI.
            for i in range(len(self.transactionsar)):
                self.money = self.transactionsar[i][1]
                self.paidby = self.transactionsar[i][0]
                self.purpose = self.transactionsar[i][2]
                self.category = self.transactionsar[i][3]

                self.paymenttime = self.transactionsar[i][4]

                # Adding each transaction as a card to transactions screen.
                # Class Tcard defines card that contains all details of a transaction
                l = TCard()
                sm.get_screen('overview').ids.transbox.add_widget(l)



        else:

            # User is not enrolled for a trip. so no team is allocated.
            Snackbar(
                text="Team not found. enroll in a trip macha!!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()

    def select(self,cat):
        '''sm.get_screen("overview").ids.Food.active=False
        sm.get_screen("overview").ids.Utilities.active = False
        sm.get_screen("overview").ids.Travelling.active = False
        sm.get_screen("overview").ids.Parties.active = False
        sm.get_screen("overview").ids.Others.active = False'''
        if cat=="Food":
            #sm.get_screen("overview").ids.Food.active = True
            self.category="Food"
        elif cat=="Utilities":
            #sm.get_screen("overview").ids.Utilities.active = True
            self.category = "Utilities"
        elif cat=="Travelling":
            #sm.get_screen("overview").ids.Travelling.active = True
            self.category = "Travelling"
        elif cat=="Parties":
            #sm.get_screen("overview").ids.Parties.active = True
            self.category = "Parties"
        elif cat=="Others":
            #sm.get_screen("overview").ids.Others.active = True
            self.category = "Others"




    # Method that runs when user clicks on view teams button.
    # This gets the assigned team details and displays.
    def viewteam(self):

        # Checking if user placed a request.
        t4 = rsheet.col_values(4)
        t3 = rsheet.col_values(3)
        t2 = rsheet.col_values(2)
        t1 = rsheet.col_values(1)
        print(t3,t2,t1)
        team=[]
        found=False
        for i in range(0, len(t3)):
            if t3[i] == self.uname:
                # User found in existing requests and team name retrieved.
                teamdes=t2[i]
                teamno=t1[i]
                print('user found')
                found=True
                break
        if found==True:
            # Team found.
            # Finding all other teammates.
            for i in range(len(t2)):
                if t2[i]==teamdes and t1[i]==teamno:
                    team.append([t3[i],t4[i]])
            self.team=team
            self.teamname=teamdes[0].upper()+str(teamno)
            print(self.teamname)
            print(self.team)

            # Checking if team is ready to go.(4 people)
            if (len(self.team)==4):
                # Team has 4 people. Ready
                self.ready='Hurray! Your team is ready'
                self.readyicon=r"C:\Users\chand\Documents\GitHub\FelizTour\Eo_circle_light-green_checkmark.ico"
            else:
                # Team has less than four people. Not Ready.
                self.ready='Oops! You need to wait for others to join'
                self.readyicon = r"C:\Users\chand\Documents\GitHub\FelizTour\Cross_red.ico"

            # Random declaration.
            while(len(self.team)!=4):
                self.team.append(['Someone', '9999999999'])

            # Adding newScreen and setting it to current.
            sm.add_widget(TeamStatus(name='teamstatus'))
            sm.current="teamstatus"

            # Removing previous screen.
            sm.remove_widget(sm.get_screen('postlogin'))
        else:

            # User is not enrolled in any trip.
            # User doesnt have a team yet.
            Snackbar(
                text="You are currently not in any team. Register for a trip",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()

    # Method that is executed when user clicks on back button.
    def goback(self):
        # This method returns user to Dashboard screen.
        x=sm.current

        # Dashboard screen is recreated and set to current.
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current="postlogin"

        # Removes previous screen.
        sm.remove_widget(sm.get_screen(x))

        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png")
        else:
            print("The file does not exist")
        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png")
        else:
            print("The file does not exist")

    # Method to get count of requests to each destination.
    # Used in backend.
    def getrcount(self):
        c=rsheet.col_values(2)
        d=rsheet.col_values(3)
        id = {"Goa": 1, "Manali": 2, "Agra": 3}
        list = {'Goa': [], 'Manali': [], 'Agra': []}
        for i in range(len(c)):
            list[c[i]].append(d[i])

        # Returns dictionary containing destinations and respective request count.
        return list

    # Method that is executed when user clicks on go button in selecting destination.
    def go(self,x):

        # Destination selected is passed as argument to function.
        destination=x
        self.requestplaced=True

        # Assigning team to the user when request is placed.

        # getting count of each destination requests.
        list = self.getrcount()
        count = {"Goa": len(list['Goa']), "Manali": len(list['Manali']), "Agra": len(list['Agra'])}

        # Assigning team number based on the number of the current request. (divided by 4).
        teamno=int((count[x]/4)+1)

        # Adding user details to requests sheet in google drive.
        newrow = [teamno, destination,self.uname,self.phonenumber]
        rsheet.insert_row(newrow, 1)

        # Confirmation note.
        Snackbar(
            text="Request placed. Check team status",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()

        # Returning to Dashboard screen after placing Trip Request.
        # Recreate dashboard screen and set it to current.
        sm.add_widget(PostLogin(name='postlogin'))
        sm.current = 'postlogin'

        # Sort the requests sheet in database based on teams.
        rsheet.sort(2,'asc')


        print(list,count)

    # Method that is executed when user clicks on logout button in navigation drawer.
    def logout(self):
        # Shifts from current screen to Login page
        x=sm.current

        # Recreating loginpage screen and setting it to current.
        sm.add_widget(LoginPage(name='loginpage'))
        sm.current = 'loginpage'

        # Remove previous screen.
        sm.remove_widget(sm.get_screen(x))


    # Method that is executed when user clicks on Submit button in Add transaction screen.
    # This method adds transaction to transactions list.
    def addSubmit(self,amount,purpose):

        # amount and purpose are passed as arguments from GUI.
        # Adding transaction details to transactions sheet in database.
        row=[self.teamname,self.uname,amount,purpose,self.category,datetime.now().strftime("%D %H:%M")]
        tsheet.insert_row(row,2)

        # Sorting the transactions sheet in database.
        tsheet.sort(1,"asc")

        # Confirmation dialogue.
        Snackbar(
            text="Transaction added successfully!!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()

        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\catwise.png")
        else:
            print("The file does not exist")
        if os.path.exists(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png"):
            os.remove(r"C:\\Users\\chand\\Documents\\GitHub\\FelizTour\\namewise.png")
        else:
            print("The file does not exist")

        # Remove Overview and Transaction screens as they are outdated.
        try:
            sm.remove_widget(sm.get_screen('overview'))
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass

        # Reloading Overview and Transactions Screens.
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))

        # Switching to overview screen.
        self.track()

        # Removing previous screen.
        sm.remove_widget(sm.get_screen('addtransaction'))

    # Method that is executed when user sets a category.
    def setcategory(self,x):
        pass


# Running Main App.
# Initiating GUI.
MainApp().run()