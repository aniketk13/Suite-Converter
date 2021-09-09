from PIL import Image  # Image Recognition
import config       # Importing input and output directory paths
import audioengine

print("Interconversion of images".center(400))
audioengine.speak("Interconversion of images")

print("Enter the file name without extension:")
audioengine.speak("Enter the file name without extension")
filename = input()
print("Enter current file's extension:")
audioengine.speak("Enter current file's extension")
fileextension = input()

inputfile = config.inputpath + filename + \
    fileextension     # Saving the input file path

print("Enter the extension in which you want your new file:")
audioengine.speak("Enter the extension in which you want your new file")
newextension = input()

file2 = config.outputpath + filename + \
    newextension     # Saving the output file path

im = Image.open(inputfile)  # Opening the image file that is to be converted

rgb_im = im.convert('RGB')  # Converting RGBA image into RGB type

rgb_im.save(file2)  # Saving the new converted image

print("Your file has been converted successfully".center(400))
audioengine.speak("Your file has been converted successfully")
