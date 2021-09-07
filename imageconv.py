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
engine.setProperty('rate', 145)


print("Enter the file name without extension:")
speak("Enter the file name without extension")
name2 = input()
print("Enter current file's extension:")
speak("Enter current file's extension")
name4 = input()

# file1 = "D:\Own Work\Python Project\Suite-Converter\Input Directory\\"+ name2 + name4
file1 = config.inputpath + name2 + name4

print("Enter the extension in which you want your new file:")
speak("Enter the extension in which you want your new file")
name3 = input()

# file2 = "D:\Own Work\Python Project\Suite-Converter\Output Directory\\" + name2 + name3
file2 = config.outputpath + name2 + name3

# im = Image.open(name2+name4)        #Opening the image file that is to be converted
im = Image.open(file1)  # Opening the image file that is to be converted

rgb_im = im.convert('RGB')  # Converting RGBA image into RGB type
# rgb_im.save(name2+name3)            #Saving the new converted image

rgb_im.save(file2)  # Saving the new converted image

print("Your file has been converted successfully".center(400))
