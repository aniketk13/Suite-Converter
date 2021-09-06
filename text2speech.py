from gtts import gTTS  # Conversion of Google Text to Speech
import pyttsx3  # Conversion of Text to Speech

# Initialization of Audio Engine


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Voice Automation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# String identifier of the active voice
engine.setProperty('voice', voices[1].id)
# Integer speech rate in words per minute, can be increased or decreased to change speed of speech
engine.setProperty('rate', 145)


print("Enter name of the file with extension:\n")
speak("Enter name of the file with extension")
name1 = input()
with open(name1, encoding="utf-8") as file:  # Opening the text file and reading the text
    file = file.read()

speak = gTTS(file, lang='en')  # Speaking text to audio
speak.save("converted.mp3")  # Saving the converted audio file

print("Your file has been converted successfully".center(400))
