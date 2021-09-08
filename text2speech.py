import pyttsx3  # Conversion of Text to Speech
import config       # Importing input and output directory paths

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
engine.setProperty('rate', 200)

print("Converting text to speech".center(400))
speak("Converting text to speech")

print("Enter name of the file without extension:\n")
speak("Enter name of the file without extension")

filename = input()
# Opening the text file and reading the text
with open(config.inputpath+filename+".txt", encoding="utf-8") as file:
    file = file.read()

# Saving the converted audio file
engine.save_to_file(file, config.outputpath +
                    filename+"converted.mp3")
engine.runAndWait()


print("Your file has been converted successfully".center(400))
speak("Your file has been converted successfully")
