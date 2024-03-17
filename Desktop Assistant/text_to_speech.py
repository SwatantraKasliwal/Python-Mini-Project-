import pyttsx3

def text_to_speech(text):
    # text = input("Enter the text:")
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-120')  # we can set speed of the voice here 
    engine.say(text)
    engine.runAndWait()