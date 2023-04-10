import pyttsx3  #pip install pyttsx3
import speech_recognition as sr      #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
import cv2      #pip install opencv-python
from requests import get    #pip install requests
# import pywhatkit as kit     #pip install opencv-python
import smtplib      #pip install secure-smtplib
import pyjokes         #pip install pyjokes
import pyautogui        #pip install pyautogui
import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader #pip install instaloader
import operator #for calculation using voice
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi
from bs4 import BeautifulSoup



"""
IN PLACEOF PYTTSX3 WE CAN ALSO USE WIN32COM.CLIENT

# Python program to convert 
# text to speech 
  
# import the required module from text to speech conversion 
import win32com.client 
  
# Calling the Disptach method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
while 1: 
    print("Enter the word you want to speak it out by computer") 
    s = input() 
    speaker.Speak(s) 
  
# To stop the program press 
# CTRL + Z 
"""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# def speak(audio):
#     speaker = Dispatch("SAPI.SpVoice")
#     print(audio)
#     speaker.Speak(audio)



#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am online sir. please tell me how may i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()

#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# def Sweather():
#     ipAdd = requests.get('https://api.ipify.org').text
#     print(ipAdd)
#     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
#     geo_requests = requests.get(url)
#     geo_data = geo_requests.json()
#     # print(geo_data)
#     city = geo_data['city']
#     api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     city_name = (f'{city}')
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#     response = requests.get(complete_url)
#     x = response.json()
#     if x["cod"] != "404":
#         y = x["main"]
#         current_temperature = y["temp"]
#         # current_pressure = y["pressure"]
#         # current_humidiy = y["humidity"]
#         z = x["weather"]
#         weather_description = z[0]["description"]
#         r = ("outside " + " the Temperature is " +
#              str(int(current_temperature - 273.15)) + " degree celsius " +
#              ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
#              ", humidity is " + str(current_humidiy) + " percent"
#              " and " + str(weather_description))
#         speak(r)
#     else:
#         speak(" City Not Found ")

# To read PDF
def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    # jarvis speaking speed should be controlled by user


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            # audio = r.listen(source,timeout=4,phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return "none"
        query = query.lower()
        return query


    def run(self):
        self.TaskExecution()
        # speak("please say wakeup to continue")
        # while True:
        #     self.query = self.takecommand()
        #     if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
        #         self.TaskExecution()

                        

    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()


            elif "play music" in self.query:
                music_dir = "E:\\Ddrive\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))



            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")

            # elif "send whatsapp message" in self.query:
            #     kit.sendwhatmsg("+91 user_number", "your_message",4,13)
            #     time.sleep(120)
            #     speak("message has been sent")

            # elif "song on youtube" in self.query:
            #     kit.playonyt("see you again")

            # elif "email to avinash" in self.query:
            #     try:
            #         speak("what should i say?")
            #         content = takecommand()
            #         to = "EMAIL OF THE OTHER PERSON"
            #         sendEmail(to,content)
            #         speak("Email has been sent to avinash")

            #     except Exception as e:
            #         print(e)
            #         speak("sorry sir, i am not able to sent this mail to avi")

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                # sys.exit()
                # gifThread.exit()
                break
                


            #to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            #to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22: 
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            # elif "shut down the system" in self.query:
            #     os.system("shutdown /s /t 5")

            # elif "restart the system" in self.query:
            #     os.system("shutdown /r /t 5")

            # elif "sleep the system" in self.query:
            #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")
            
            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")



            ###################################################################################################################################
            ###########################################################################################################################################



            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                    

            elif "tell me news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()


            elif "email to avinash" in self.query:
                
                speak("sir what should i say")
                self.query = self.takecommand()
                if "send a file" in self.query:
                    email = 'your@gmail.com' # Your email
                    password = 'yourpass@123' # Your email account password
                    send_to_email = 'to_person@gmail.com' # Whom you are sending the message to
                    speak("okay sir, what is the subject for this email")
                    self.query = self.takecommand()
                    subject = self.query   # The Subject in the email
                    speak("and sir, what is the message for this email")
                    self.query2 = self.takecommand()
                    message = self.query2  # The message in the email
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")    # The File attachment in the email

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to avinash")

                else:                
                    email = 'your@gmail.com' # Your email
                    password = 'your_pass@123' # Your email account password
                    send_to_email = 'to_person@gmail.com' # Whom you are sending the message to
                    message = query # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                    server.starttls() # Use TLS
                    server.login(email, password) # Login to the email server
                    server.sendmail(email, send_to_email , message) # Send the email
                    server.quit() # Logout of the email server
                    speak("email has been sent to avinash")


            ##########################################################################################################################################
            ###########################################################################################################################################

            elif "do some calculations" in self.query or "can you calculate" in self.query:            
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))


            #-----------------To find my location using IP Address

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass


            

            #-------------------To check a instagram profile----
            elif "instagram profile" in  self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            #-------------------  To take screenshot -------------
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")


            # speak("sir, do you have any other work")

            #-------------------  To Read PDF file -------------
            elif "read pdf" in self.query:
                pdf_reader()

            #--------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("sir, all the files in this folder are now hidden.")                

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")
                    
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif "temperature" in self.query:
                search = "weather in delhi"
                url = f"https://www.google.com/search?q={search}"
                req = requests.get(url)
                save = BeautifulSoup(req.text,"html.parser")
                tempp = save.find("div",class_= "BNeawe").text
                speak(f"current {search} is {tempp}")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/wallpaper/jar/iron.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/wallpaper/jar/intial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

#self.textBrowser.setText("Hello world")
 #       self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())
