import fitz  # PDF Manipulation
import config  # Importing File Path
import audioengine

print("Extracting Images from PDF".center(400))
audioengine.speak("Extracting Images from PDF")

print("Enter name of the file without extension")
audioengine.speak("Enter name of the file without extension")

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
audioengine.speak("Your file has been converted successfully")
