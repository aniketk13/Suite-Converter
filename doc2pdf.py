from docx2pdf import convert        #Conversion of document to pdf module
import pyttsx3                      #Conversion of Text to Speech

#Initialization of Audio Engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Voice Automation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#String identifier of the active voice
engine.setProperty('voice', voices[1].id)
#Integer speech rate in words per minute, can be increased or decreased to change speed of speech
engine.setProperty('rate', 145)

print("Enter the name of file with extension:")
speak("Enter the name of file with extension")
name=input()
convert(name)
convert(name, r"C:\Users\ANIKET KHAJANCHI\Downloads\Project2", name)

# print("Your file has been converted successfully".center(400))
