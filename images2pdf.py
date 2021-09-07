from PIL import Image  # Image Recognition
import pyttsx3  # Conversion of Text to Speech
import config
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


print("Enter number of images to be compiled")
speak("Enter number of images to be compiled")
n = input()
n = int(n)

im_list = []

# file1 = "D:\Own Work\Python Project\Suite-Converter\Output Directory\\" + "images-compiled.pdf"
file1 = config.outputpath + "images-compiled.pdf"

pdf1_filename = file1  # declaring the pdf file to be saved

# file2 = "D:\Own Work\Python Project\Suite-Converter\Input Directory\\"

print("Enter name of first file with extension:")  # Taking first image file
speak("Enter name of first file with extension")
# name = r"D:\Own Work\Python Project\Suite-Converter\Input Directory\\"+input()
name = config.inputpath+input()
im1 = Image.open(name)

for i in range(n-1):
    # Taking rest of the image files
    print("Enter name of another file with extension:\n")
    speak("Enter name of another file with extension")
    # name = input()
    # name = r"D:\Own Work\Python Project\Suite-Converter\Input Directory\\"+input()
    name = config.inputpath+input()
    im_list.append(Image.open(name))

im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True,
         append_images=im_list)  # Saving the pdf file with all the images

print("Your file has been converted successfully".center(400))
