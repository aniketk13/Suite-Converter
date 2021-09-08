from PIL import Image  # Image Recognition
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

print("Interconversion of images".center(400))
speak("Interconversion of images")

print("Enter the file name without extension:")
speak("Enter the file name without extension")
filename = input()
print("Enter current file's extension:")
speak("Enter current file's extension")
fileextension = input()

inputfile = config.inputpath + filename + \
    fileextension     # Saving the input file path

print("Enter the extension in which you want your new file:")
speak("Enter the extension in which you want your new file")
newextension = input()

file2 = config.outputpath + filename + \
    newextension     # Saving the output file path

im = Image.open(inputfile)  # Opening the image file that is to be converted

rgb_im = im.convert('RGB')  # Converting RGBA image into RGB type

rgb_im.save(file2)  # Saving the new converted image

print("Your file has been converted successfully".center(400))
speak("Your file has been converted successfully")
