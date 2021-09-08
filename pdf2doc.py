from pdf2docx import Converter  # Conversion of Pdf to Document
import pyttsx3  # Conversion of Text to Speech
import config   # Importing input and output directory paths


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

print("Converting PDF to document".center(400))
speak("Converting PDF to document")

print("Enter name of your file without extension")
speak("Enter name of your file without extension")
filename = input()

inputfile = config.inputpath+filename+".pdf"     # Saving the input file path
outputfile = config.outputpath+filename + \
    "-converted.docx"       # Saving the output file path

# convert pdf to docx
cv = Converter(inputfile)  # initialized a converter object
cv.convert(outputfile, start=0, end=None)  # converting pdf to docx
cv.close()      # closed the pdf file

print("Your file has been converted successfully".center(400))
speak("Your file has been converted successfully")
