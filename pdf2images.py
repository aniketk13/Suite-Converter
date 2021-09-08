import fitz  # PDF Manipulation
import pyttsx3  # Conversion of Text to Speech
import config  # Inporting File Path


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

print("Extracting Images from PDF".center(400))
speak("Extracting Images from PDF")

print("Enter name of the file without extension")
speak("Enter name of the file without extension")

filename = config.inputpath+input()+".pdf"
# Opening the Pdf file
doc = fitz.open(filename)

# Running a loop to find the images
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        # this is GRAY or RGB
        if pix.n < 5:
            # saving the images
            pix.writePNG(config.outputpath+"Image-%s.png" % (i))
        # CMYK: convert to RGB first
        else:
            pix = fitz.Pixmap(fitz.csRGB, pix)
            # saving the images
            pix.writePNG(config.outputpath+"Image-%s.png" % (i))
        pix = None

print("Your file has been converted successfully".center(400))
