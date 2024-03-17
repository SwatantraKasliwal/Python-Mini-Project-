import text_to_speech as tts
import speech_to_text as stt
import datetime as dt
import webbrowser as wb
import weather as w
from AppOpener import open


# Customise the command according to you ^_^ :
def action(data):
    user_data = str(data.lower())

    if "what is your name" in user_data:
        tts.text_to_speech("My name is DeskoAi")
        return "My name is DeskoAi" 
    
    elif "hello" in user_data or "hi" in user_data or "hye" in user_data:
        tts.text_to_speech("Hello sir, How i can Serve you ") 
        return "Hello sir, How i can Serve you "
    
    elif "good morning" in user_data:
        tts.text_to_speech("Good morning Sir")
        return "Good morning Sir"
    
    elif "what is the time now" in user_data:
        current_time = dt.datetime.now()
        time = (str)(current_time) + "Hour:", (str)(current_time.minute) + "minutes"
        tts.text_to_speech(f"your time is {time}")
        return f"your time is {time}"
    
    elif "shutdown" in user_data:
        tts.text_to_speech("okay sir")
        return "okay sir"
    
    elif "play music" in user_data or "open spotify" in user_data:
        wb.open("https://open.spotify.com/")
        tts.text_to_speech("Opening Spotify")
        return "Opening Spotify"
        
    elif "open mail" in user_data:
        wb.open("https://mail.google.com/mail?hl=en")
        tts.text_to_speech("OPening your mail")
        return "OPening your mail"
    
    elif "open youtube" in user_data:
        wb.open("https://www.youtube.com/")
        tts.text_to_speech("opening youtube")
        return "opening youtube"
    
    elif "open whatsapp" in user_data:
        wb.open("https://web.whatsapp.com/")
        tts.text_to_speech("opening Whatsup")
        return "opening Whatsup"
    
    elif "open google" in user_data:
        wb.open("https://www.google.co.in/")
        tts.text_to_speech("opening google")
        return "opening google"
    
    # elif "open demo folder" in user_data or "open demo" in user_data:
    #     # open(r"C:\Users\swata\OneDrive\Desktop\demo")
    #     # tts.text_to_speech("opening demo folder")
    #     # return "opening demo folder"
    #     try:
    #         with open(r"C:\Users\swata\OneDrive\Desktop\demo", 'r') as file:
    #             print(file.read())
    #     except FileNotFoundError:
    #         print("File not found")
    #     except Exception as e:
    #         print("An error occurred: ", str(e))

    elif "what is the weather" in user_data or "weather" in user_data or "what is the weather condition" in user_data:
        weather = w.weather()
        tts.text_to_speech(f"the weather condition is {weather} ")
        return f"the weather condition is {weather} "
    elif "what is my screen time" in user_data:
        pass




    else:
        tts.text_to_speech("Sorry i didn't get it ")
        return "Sorry i didn't get it "
