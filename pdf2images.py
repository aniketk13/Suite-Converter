import fitz                         #PDF Manipulation
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


print("Enter name of the file with extension")
speak("Enter name of the file with extension")
name=input()
doc = fitz.open(name)       #Opening the Pdf file

for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("converted%s.png" % (i))       #saving the images
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("converted%s.png" % (i))      #saving the images
            pix1 = None
        pix = None

print("Your file has been converted successfully".center(400))