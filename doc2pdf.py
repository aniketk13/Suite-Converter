from docx2pdf import convert  # Conversion of document to pdf module
import pyttsx3  # Conversion of Text to Speech
import config  # Importing input and output directory paths


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

print("Converting document to PDF".center(400))
speak("Converting document to PDF")

print("Enter the name of file without extension:")
speak("Enter the name of file without extension")
filename = input()

inputfile = (config.inputpath+filename+".docx")  # Saving the input file path

outputfile = config.outputpath+filename + \
    "-converted.pdf"  # Saving the output file path

convert(inputfile, outputfile)

print("Your file has been converted successfully".center(400))
speak("Your file has been converted successfully")
