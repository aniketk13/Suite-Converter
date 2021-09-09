import audioengine
import config       # Importing input and output directory paths


print("Converting text to speech".center(400))
audioengine.speak("Converting text to speech")

print("Enter name of the file without extension:\n")
audioengine.speak("Enter name of the file without extension")

filename = input()
# Opening the text file and reading the text
with open(config.inputpath+filename+".txt", encoding="utf-8") as file:
    file = file.read()

# Saving the converted audio file
audioengine.engine.save_to_file(file, config.outputpath +
                                filename+"-converted.mp3")
audioengine.engine.runAndWait()


print("Your file has been converted successfully".center(400))
audioengine.speak("Your file has been converted successfully")
