# This miniproject titled *MAKING ANDROID APPLICATION_TV REMOTE* is made by
# CHANDRASHEKAR OLLALA 1602-20-733-076
# Vasavi college of engineering


from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRound
import webbrowser
# webbrowser module is used to open a particular link in default browser.
import speech_recognition as sr
# speech_recognition package is used to extract speech text from audio file.
import pyttsx3
# pyttsx3 is text to speech converting module.


# Global variables.
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#function that executews when user clicks on voice search button.
def voicesearch():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source) #the recorded audio is saved in the name of "voice"
        command = listener.recognize_google(voice) #text is extracted from voice.
        command = command.lower() #all text is coverted into lower case
        print(command)
    print(command)
    if '6' in command:
        webbrowser.open('https://www.youtube.com/watch?v=bl9VaUaI0r0')
    elif 'telangana' in command:
        webbrowser.open('https://www.youtube.com/watch?v=zVe4WWkxRIs')
    elif 'andhra' in command or 'pradesh' in command:
        webbrowser.open('https://www.youtube.com/watch?v=OVp1u3PkBiA')
    elif 'sakshi' in command or 'saakshi' in command:
        webbrowser.open('https://www.youtube.com/watch?v=8McTsOqeueE')
    elif '9' in command or 'nine'in command:
        webbrowser.open('https://www.youtube.com/watch?v=Q6QR4979KIQ')
    elif 'ntv' in command:
        webbrowser.open('https://www.youtube.com/watch?v=HUiHKse-YgM')
    elif "NDTV" in command:
        webbrowser.open('https://www.youtube.com/watch?v=WB-y7_ymPJ4')
    elif 'Movies' in command:
        webbrowser.open('https://www.hotstar.com/in/star-maa-movies/1260000008')
    elif 'star' in command or 'maa' in command:
        webbrowser.open('https://www.hotstar.com/in/star-maa/1260000016')
    elif 'zee' in command or 'telugu' in command:
        webbrowser.open('https://www.zee5.com/channels/details/zee-telugu/0-9-zeetelugu')
    elif 'gold' in command:
        webbrowser.open('https://www.hotstar.com/in/maa-gold/1260000019')
    elif 'gemini' in command:
        webbrowser.open('https://www.sunnxt.com/live/14019/gemini-tv-hd')
    elif '5' in command or 'five' in command:
        webbrowser.open('https://www.youtube.com/watch?v=iZHpAj8cHsw')
    else:
        pass

#this function is instruction to speak the given text.
def talk(text):
    engine.say(text)
    engine.runAndWait()


class MainApp(MDApp):

    def build(self):

        main_layout = MDBoxLayout(orientation="vertical")
        p = MDLabel(text='CHANDRASHEKAR OLLALA',
                  size_hint=(1, .5),
                  font_size=40)
        main_layout.add_widget(p)  # Label is added to the box layout
        p=MDLabel(text='Links for TV- Click button',
                size_hint=(1,.5),
                font_size=45)
        main_layout.add_widget(p) #Label is added to the box layout
        buttons = [
            ["Voice search"],
            ["Gemini TV","Gemini Movies"],
            ["Star Maa", "Maa Movies","Maa Gold"],
            ["Zee Telugu","Zee Cinemalu"],
            ["V6 News","Sakshi","TV5 News"],
            ["TV9 News","ETV Telangana","ETV AndhraPradesh"]
        ]
        for row in buttons:  #all the buttons are added to boxlayout.
            h_layout = MDBoxLayout()
            for label in row:
                width= 1/len(row)
                button = MDRaisedButton(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint=(width,0.8),
                )
                button.bind(on_release=self.on_button_press) #function is assigned to operate when button is clicked
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        return main_layout

    # this fuction is executed when any button is clicked based on the text of button.
    def on_button_press(self, instance):
        button_text = instance.text
        if button_text == "V6 News":
            webbrowser.open('https://www.youtube.com/watch?v=bl9VaUaI0r0')
        elif button_text == "ETV Telangana":
            webbrowser.open('https://www.youtube.com/watch?v=zVe4WWkxRIs')
        elif button_text == "ETV AndhraPradesh":
            webbrowser.open('https://www.youtube.com/watch?v=OVp1u3PkBiA')
        elif button_text == "Sakshi":
            webbrowser.open('https://www.youtube.com/watch?v=8McTsOqeueE')
        elif button_text == "TV9 News":
            webbrowser.open('https://www.youtube.com/watch?v=Q6QR4979KIQ')
        elif button_text == "NTv Telugu":
            webbrowser.open('https://www.youtube.com/watch?v=HUiHKse-YgM')
        elif button_text == "NDTV English":
            webbrowser.open('https://www.youtube.com/watch?v=WB-y7_ymPJ4')
        elif button_text == "Maa Movies":
            webbrowser.open('https://www.hotstar.com/in/star-maa-movies/1260000008')
        elif button_text == "Star Maa":
            webbrowser.open('https://www.hotstar.com/in/star-maa/1260000016')
        elif button_text == "Zee Telugu":
            webbrowser.open('https://www.zee5.com/channels/details/zee-telugu/0-9-zeetelugu')
        elif button_text == "Maa Gold":
            webbrowser.open('https://www.hotstar.com/in/maa-gold/1260000019')
        elif button_text == "Zee Cinemalu":
            webbrowser.open('https://www.zee5.com/channels/details/zee-cinemalu/0-9-zeecinemalu')
        elif button_text == "Gemini Movies":
            webbrowser.open('https://www.sunnxt.com/live/9015/gemini-movies/')
        elif button_text == "Gemini TV":
            webbrowser.open('https://www.sunnxt.com/live/14019/gemini-tv-hd')
        elif button_text == "TV5 News":
            webbrowser.open('https://www.youtube.com/watch?v=iZHpAj8cHsw')
        elif button_text == 'Voice search':
            voicesearch() #this function takes command as voice. mentioned above.

if __name__ == "__main__":
    app = MainApp()
    app.run() # runs the app.

# this app runs on Kivy GUI and can be extracted into an .apk file that can be installed on Android devices.
# Buildozer is used to extract the .apk file.
# Hosting OS while extracting .apk file should be LINUX or Mac.