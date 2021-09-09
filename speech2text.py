import speech_recognition as sr  # Speech Recognition
import pyttsx3  # Conversion of Text to Speech
import config       # Importing input and output directory paths
import audioengine


# define the microphone

print("Converting speech to text".center(400))
audioengine.speak("Converting speech to text")

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
print("Please start speaking....")      # record your speech
audioengine.speak("Please start speaking")

result = r.recognize_google(audio, language='en-us')      # speech recognition
print("Recording Stopped")
print("Converting to Text File")
with open(config.outputpath+"speechtotext.txt", mode='w') as file:    # export the result
    file.write(result)

print("Your file has been converted successfully!".center(400))
audioengine.speak("Your file has been converted successfully!")
