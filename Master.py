from subprocess import call  # Calling different files in one file
import time  # Module for delay
from docx2pdf import convert  # Conversion of document to pdf
from pdf2docx import Converter  # Conversion of Pdf to Document
from gtts import gTTS  # Conversion of Google Text to Speech
from PIL import Image  # Image Recognition
import speech_recognition as sr  # Speech Recognition
import pyttsx3  # Conversion of Text to Speech
import string  # String Module
import fitz  # PDF Manipulation
import sys  # System Module
import doc2pdf
import config

# settings.init()

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
engine.setProperty('rate', 250)

# Introduction
print("Welcome to the Suite Converter\n".center(400))
speak("Welcome to the Suite Converter")
print("Following are the Services we provide:")
speak("Following are the Services we provide")
print("\n A.Document to PDF")
speak("Document to PDF")
print("\n B.PDF to Document")
speak("PDF to Document")
print("\n C.Text to Audio file")
speak("Text to Audio file")
print("\n D.Voice to Text file")
speak("Voice to Text file")
print("\n E.Compiling multiple Images to PDF")
speak("Compiling multiple Images to PDF")
print("\n F.Extraction of multiple Images from a PDF")
speak("Extraction of multiple Images from a PDF")
print("\n G.Inter conversion of Images\n\n")
speak("Inter conversion of Images")
time.sleep(1)
# Taking choice as input in audio form and converting to text


def takecom():

    # Listening the choice in audio form
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Enter the option....\n".center(400))
        # audio = r.listen(source)
        speak("Enter the option")
        choiceinput = (input("Enter the option....\n".center(400)))

    # # Recognising and converting the choice in text
    # try:
    #     print("Recognising....")
    #     text = r.recognize_google(audio, language='en-in')
    #     print(text, "\n")

    # # Backup if choice not understood
    # except Exception:
    #     speak("Error...")
    #     print("Try Again..")
    #     return "none"
    return choiceinput


# for main function
if __name__ == "__main__":

    # Checking for choice and calling the respective python scripts
    while (1):
        query = takecom()

        if "1" in query:
            # Calling file for docx to pdf conversion
            call(["python", "doc2pdf.py"])
            print("Your file has been converted successfully".center(400))

        elif "2" in query:
            call(["python", "pdf2doc.py"])  # Calling file for pdf to docx

        elif "3" in query:
            # Calling file for Text to speech
            call(["python", "text2speech.py"])

        elif "4" in query:
            # Calling file for speech to text
            call(["python", "speech2text.py"])

        elif "5" in query or '5' in query:
            # Calling file for multiple images to pdf
            call(["python", "images2pdf.py"])

        elif "6" in query or 'six' in query:
            # Calling file for pdf to multiple images
            call(["python", "pdf2images.py"])

        elif "7" in query:
            call(["python", "imageconv.py"])  # Interconversion of Images

        elif query == 'none':  # If no choice given
            continue

        else:
            print("Invalid Input")  # If incorrect choice given
            continue

        speak("Your file has been converted successfully")

        print("Do you want to convert again?(Yes/No)")
        speak("Do you want to convert again")

        def takech():
            # Listening the choice in audio form
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say the option....\n".center(400))
                speak("Say Yes or No")
                audio = r.listen(source)

            # Recognising and converting the choice in text
            try:
                print("Recognising....")
                text = r.recognize_google(audio, language='en-in')
                print(text, "\n")

            # Backup if choice not understood
            except Exception:
                speak("Error...")
                print("Try Again..")
            return text

        query1 = takech()
        if 'yes' in query1:
            print(" A.Document to PDF \n\n B.PDF to Document \n\n C.Text to Audio file \n\n D.Voice to Text file \n\n E.Compiling multiple Images to PDF \n\n F.Extraction of multiple Images from a PDF \n\n G.Inter conversion of Images\n\n")
            continue

        print("Thank You for converting".center(400))
        speak("Thank you for converting")
        print("Developed by Team <define>".center(500))
        speak("Developed by Team Define")
        sys.exit()
