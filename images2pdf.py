from PIL import Image  # Image Recognition
import pyttsx3  # Conversion of Text to Speech
import config   # Importing File Path
import audioengine


print("Compiling Images to a PDF".center(400))
audioengine.speak("Compiling Images to a PDF")

print("Enter number of images to be compiled")
audioengine.speak("Enter number of images to be compiled")
imgNum = int(input())
imgList = []

pdfName = config.outputpath + str(imgNum) + "-images-compiled.pdf"


print("Enter name of first file with extension:")  # Taking first image file
audioengine.speak("Enter name of first file with extension")
name = config.inputpath+input()
# im1 = Image.open(name)

for i in range(imgNum-1):
    # Taking rest of the image files
    print("Enter name of next file with extension:\n")
    audioengine.speak("Enter name of next file with extension")
    name = config.inputpath+input()
    imgList.append(Image.open(name))

# Saving the pdf file with all the images
Image.open(name).save(pdfName, "PDF", resolution=100.0, save_all=True,
                      append_images=imgList)

print("Your file has been converted successfully".center(400))
