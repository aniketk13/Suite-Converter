import speech_recognition as sr  # Speech Recognition
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


r = sr.Recognizer()

mic = sr.Microphone(device_index=0)     # define the microphone

print("Converting speech to text".center(400))
speak("Converting speech to text")

print("Please start speaking....")      # record your speech
speak("Please start speaking")
with mic as source:
    audio = r.listen(source)

result = r.recognize_google(audio)      # speech recognition

with open(config.outputpath+"speechtotext.txt", mode='w') as file:    # export the result
    file.write(result)

print("Your file has been converted successfully!".center(400))
