kv='''
<HelloScreen>:

    Image:
        source:'logo.png'
        size_hint_x: 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDRaisedButton:
        text: "Continue to APP"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        on_press: app.continue_to_app()



<LoginPage>:



    MDCard:
        size_hint: 0.8, 0.75
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDLabel:
        id: welcome_label
        text: "Welcome"
        font_size: 35
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None

        padding_y: 15

    MDTextField:
        id: user
        hint_text: "Username"
        icon_right: "account"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

    MDTextField:
        id: password
        hint_text: "Password"
        icon_right: "eye-off"
        size_hint_x: 0.6
        width: 200
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        password: True

    MDRoundFlatButton:
        text: "Login"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        on_press: app.login(root.ids.user.text,root.ids.password.text)
        size_hint_x: 0.6

    MDLabel:
        text: "New User? Signup!"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: 'center'
        size_hint_y: None

        padding_y: 15


    MDRoundFlatButton:
        text: "Signup"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        on_press: app.signup()
        size_hint_x: 0.6




    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "User Login"
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        []


        MDNavigationDrawer:
            id: nav_drawer


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



<Signup>:


    MDCard:
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
    MDTextField:
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
        id: signup_phn
        hint_text: "Phone number"
        size_hint_x: 0.7
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.50, "center_y": 0.45}
        helper_text_mode: "on_error"
        helper_text: "Enter 10-digit phone number"

    MDTextField:
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
        text: "Submit"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        on_press: app.signupSubmit(root.ids.signup_name.text,root.ids.signup_age.text,root.ids.signup_gender.text,root.ids.signup_phn.text,root.ids.signup_email.text,root.ids.signup_password.text)

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Signup "
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['menu', lambda x: app.logout()]]


        MDNavigationDrawer:
            id: nav_drawer


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


<PostLogin>:

    MDLabel:

        text: "Planning for a Trip this week?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        text: "Plan new trip"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        on_press: app.newtrip()


    MDLabel:
        text: "Already Registered?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        text: "Check your team status"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        on_press: app.viewteam()

    MDLabel:
        text: "Trip Started?"
        font_size: 18
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDRoundFlatButton:
        text: "Track expenses"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        on_press: app.track()

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Hi "+ app.uname
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer


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
                            text: "LOG OUT"
                            font_size: 40
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            on_press: app.logout()
<Trans>:
    #boxlayout : box
    #id: box
    orientation: 'horizontal'





<TCard>:
    id: tcard
    orientation: "vertical"
    size_hint: 1, None
    height: box_top.height + box_bottom.height
    focus_behavior: True
    ripple_behavior: True
    pos_hint: {"center_x": .5, "center_y": .5}

    MDBoxLayout:
        id: box_top
        spacing: "20dp"
        adaptive_height: True



        MDBoxLayout:
            id: text_box
            orientation: "vertical"
            adaptive_height: True
            spacing: "10dp"
            padding: 0, "10dp", "10dp", "10dp"

            MDLabel:
                text: app.money
                theme_text_color: "Primary"
                font_style: "H5"
                bold: True
                adaptive_height: True

            MDLabel:
                text: app.paidby+"    "+app.paymenttime
                adaptive_height: True
                theme_text_color: "Primary"

    MDSeparator:

    MDBoxLayout:
        id: box_bottom
        adaptive_height: True
        padding: "10dp", 0, 0, 0

        MDLabel:
            text: app.purpose
            adaptive_height: True
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"
<NewTrip>:
    ScrollView:
        do_scroll_x: True
        do_scroll_y: False
        size_hint: 0.95,0.87
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        GridLayout:
            cols: 4
            size_hint_x: 3
            MDCard:
                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    source:'goa.png'
                    size_hint_y: .55

                    pos_hint:{"center_x": 0.5, "center_y": 0.5}



                MDLabel:
                    text: "Goa"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    text: "India, 691 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Rs.25000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_press: app.go("Goa")
            MDCard:
                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    source:'manali.png'
                    size_hint_y: .55

                    pos_hint:{"center_x": 0.5, "center_y": 0.5}



                MDLabel:
                    text: "Manali"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    text: "India, 2126 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Rs.35000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_press: app.go("Manali")

            MDCard:
                size_hint: 0.97, 0.6
                pos_hint: {"center_x": 0.5, "center_y": 0.45}
                elevation: 30
                padding: 25
                spacing: 25
                orientation: 'vertical'
                Image:
                    source:'agra.png'
                    size_hint_y: .55

                    pos_hint:{"center_x": 0.5, "center_y": 0.5}



                MDLabel:
                    text: "Agra"
                    font_size: 40
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .1
                    padding_y: 15
                MDLabel:
                    text: "India, 1341 km from Hyderabad"
                    font_size: 20
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Estimated cost:"
                    font_size: 15
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDLabel:
                    text: "Rs.15000/person"
                    font_size: 28
                    halign: left
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    halign: 'center'
                    size_hint_y: .05
                    padding_y: 15

                MDRaisedButton:
                    text: "Go"
                    font_size: 20
                    size_hint_y: .15
                    size_hint_x: .8
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_press: app.go("Agra")
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Plan new trip"
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer


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
                            text: "Go to home page"
                            font_size: 25
                            pos_hint: {"center_x": 0.3, "center_y": 0.3}
                            on_press: app.goback()




<TeamStatus>:

    MDRoundFlatButton:
        text: "Go Back"
        font_size: 28
        size_hint_x: 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        on_press: app.goback()
    MDLabel:
        text: "Your Team: "+app.teamname
        font_size: 30
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        halign: 'center'
    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.27, "center_y": 0.55}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: app.team[0][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[1][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[2][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[3][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.73, "center_y": 0.55}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: app.team[0][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            text: app.team[1][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[2][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[3][1]
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDLabel:
        text: app.ready
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: 'center'
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

                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer


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
    MDRaisedButton:
        text: "Overview"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        size_hint: 0.5,0.075
        on_press: app.overview()
        border: 'yellow'

    MDFlatButton:
        text: "Transactions"
        font_size: 18
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        on_press: app.transactions()
        size_hint: 0.5,0.075


    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.27, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: app.team[0][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[1][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[2][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: app.team[3][0]
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.32
        pos_hint: {"center_x": 0.73, "center_y": 0.65}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: str(app.spends[app.team[0][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            text: str(app.spends[app.team[1][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.team[2][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.spends[app.team[3][0]])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDCard:
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.27, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: 'Food'
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Utilities"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Travelling"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Parties"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: "Others"
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
    MDCard:
        size_hint: 0.48, 0.4
        pos_hint: {"center_x": 0.73, "center_y": 0.25}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        MDLabel:
            text: str(app.cwisespends["Food"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

        MDLabel:
            text: str(app.cwisespends["Utilities"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Travelling"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Parties"])
            font_size: 15
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
        MDLabel:
            text: str(app.cwisespends["Others"])
            font_size: 18
            halign: left
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus


    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer


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

<Transactions>:
    MDRaisedButton:
        text: "Transactions"
        font_size: 18
        md_bg_color: 1, 0, 1, 1
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": 0.75, "center_y": 0.85}
        size_hint: 0.5,0.075
        on_press: app.transactions()
        border: 'yellow'

    MDFlatButton:
        text: "Overview"
        font_size: 18
        pos_hint: {"center_x": 0.25, "center_y": 0.85}
        on_press: app.track()
        size_hint: 0.5,0.075
    ScrollView:
        id: scroll
        do_scroll_x: False
        do_scroll_y: True
        size_hint: 1,0.80
        pos_hint: {"center_x": 0.5275, "y": 0}

        MDList:

            id: box
            spacing: 20


    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.plus

    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Track Expenses"
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]





<AddTransaction>

    MDCard:
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
    MDTextField:
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
        id: category
        text: 'select purpose'
        font_size: 15
        halign: left
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        halign: 'center'
    MDLabel:
        text: "Food"
        font_size: 20
        pos_hint: {"center_x": 0.50, "center_y": 0.5}
        size_hint_x: 0.5
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .5}
        on_active: app.on_checkbox_active('Food')
    MDLabel:
        text: "Utilities"
        font_size: 20
        pos_hint: {"center_x": 0.50, "center_y": 0.42}
        size_hint_x: 0.5
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .42}
        on_active: app.on_checkbox_active('Utilities')
    MDLabel:
        text: "Tranvelling"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        size_hint_x: 0.5
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .35}
        on_active: app.on_checkbox_active('Travelling')
    MDLabel:
        text: "Parties"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.27}
        size_hint_x: 0.5
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .27}
        on_active: app.on_checkbox_active('Parties')
    MDLabel:
        text: "Others"
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        size_hint_x: 0.4
        halign: 'left'
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .8, 'center_y': .20}
        on_active: app.on_checkbox_active('Others')



    MDRaisedButton:
        text: "Add"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        on_press: app.addSubmit(amount.text,purpose.text)
    Widget:
        size_hint_y: None
        height: 10
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "Add Transaction"
                    elevation: 10
                    pos_hint: {"top": 1}

                    left_action_items:
                        [['keyboard-backspace', lambda x: app.goback()]]


        MDNavigationDrawer:
            id: nav_drawer


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
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import Snackbar
from kivy.properties import ObjectProperty
# datetime module is used to get current time and date.
from datetime import datetime


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


# Builder loads GUI configuration string saved as kv.
Builder.load_string(kv)

# Screen Manager is used to switch between different screens.
sm = ScreenManager()

# Window.size = (300,550)


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

class Trans(MDBoxLayout):
    def addcard(self):
        p=TCard()

class TCard(MDCard):
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

        # Setting display theme for GUI.
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"

        # Adding screens (HelloScreen and New Trip)
        sm.add_widget(HelloScreen(name='helloscreen'))
        sm.add_widget(NewTrip(name='newtrip'))

        # Current screen set to HelloScreen.(on app start).
        sm.current = 'helloscreen'

        return sm

    # Method to validate Login credentials entered by verifying.

    # Userdetails global variable is updated only if Username is found and Entered Password matches with correct password.

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

        # Creating new screen for Userlogin and setting current screen to login screen.
        sm.add_widget(LoginPage(name='loginpage'))
        sm.current = 'loginpage'


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

    # Method to select category when clicked against its checkbox (Add Transaction screen).
    def on_checkbox_active(self,category):
        self.category=category

    # Method that executes when Add Transaction button is clicked.
    def plus(self, addtrs):
        # Creating new Screen and setting it to current.
        sm.add_widget(AddTransaction(name='addtransaction'))
        sm.current = 'addtransaction'

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

    # Method that is executed when new trip button is clicked.
    def newtrip(self):
        # Add screen.
        # Set current screen to added screen.
        # Remove previous screen.
        sm.add_widget(NewTrip(name='newtrip'))
        sm.current = 'newtrip'
        sm.remove_widget(sm.get_screen('postlogin'))


    # Method executed when signup button from login oage is clicked.
    def signup(self):
        Snackbar(
            text="Enter your details",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()

        # Add signup screen.
        # Set current screen to signup screen.
        # Remove previous screen.
        sm.add_widget(Signup(name='signup'))

        sm.current = 'signup'
        sm.remove_widget(sm.get_screen('loginpage'))


    # Method that is executed when user clicks on submit button in signup screen.
    # All values entered as details are passed as arguments.
    def signupSubmit(self,name,age,gender,phone,email,password):

        # Checks if details are valid.
        x=self.checksignupdata(name,age,gender,phone,email,password)
        if x=="OK" and name!="" and age!="" and gender!="" and phone!="" and email!="" and password!="":
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
        try:
            sm.remove_widget(sm.get_screen('overview'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass
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
            for i in range(len(t2)):
                if t2[i]==teamdes and t1[i]==teamno:
                    team.append([t3[i],t4[i]])
            self.team=team
            t6 = tsheet.col_values(6)
            t5 = tsheet.col_values(5)
            t4 = tsheet.col_values(4)
            t3 = tsheet.col_values(3)
            t2 = tsheet.col_values(2)
            t1 = tsheet.col_values(1)
            print(t3, t2, t1)
            self.transactionsar = []

            for i in range(len(t2)):
                if t1[i] == self.teamname:
                    self.transactionsar.append([t2[i], t3[i], t4[i], t5[i], t6[i]])
            print(self.transactionsar)
            c=['Food','Utilities','Travelling','Parties','Others']
            self.cwisespends={"Food":0,"Utilities":0,"Travelling":0,"Parties":0,"Others":0}
            self.spends={self.team[0][0]:0,self.team[1][0]:0,self.team[2][0]:0,self.team[3][0]:0,}
            for i in range(len(self.transactionsar)):
                for j in range(len(self.team)):
                    if self.transactionsar[i][0]==self.team[j][0]:
                        self.spends[self.transactionsar[i][0]]=self.spends[self.transactionsar[i][0]]+int(self.transactionsar[i][1])
                for k in c:
                    if self.transactionsar[i][3]==k:
                        self.cwisespends[k]=self.cwisespends[k]+int(self.transactionsar[i][1])

            sm.add_widget(Overview(name='overview'))
            sm.current="overview"
            try:
                sm.remove_widget(sm.get_screen('transactions'))
            except kivy.uix.screenmanager.ScreenManagerException:
                pass
        else:
            Snackbar(
                text="Team not found. enroll in a trip macha!!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
    def viewteam(self):
        t4 = rsheet.col_values(4)
        t3 = rsheet.col_values(3)
        t2 = rsheet.col_values(2)
        t1 = rsheet.col_values(1)
        print(t3,t2,t1)
        team=[]
        found=False
        for i in range(0, len(t3)):
            if t3[i] == self.uname:
                teamdes=t2[i]
                teamno=t1[i]
                print('user found')
                found=True
                break
        if found==True:

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
        else:
            Snackbar(
                text="You are currently not in any team. Register for a trip",
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.95
            ).open()
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

    def addSubmit(self,amount,purpose):
        row=[self.teamname,self.uname,amount,purpose,self.category,datetime.now().strftime("%D %H:%M")]
        tsheet.insert_row(row,2)
        tsheet.sort(1,"asc")
        Snackbar(
            text="Transaction added successfully!!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.95
        ).open()
        try:
            sm.remove_widget(sm.get_screen('overview'))
            sm.remove_widget(sm.get_screen('transactions'))
        except kivy.uix.screenmanager.ScreenManagerException:
            pass
        sm.add_widget(Overview(name='overview'))
        sm.add_widget(Transactions(name='transactions'))
        self.track()
        sm.remove_widget(sm.get_screen('addtransaction'))

    def setcategory(self,x):
        pass
MainApp().run()