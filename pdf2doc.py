from pdf2docx import Converter  # Conversion of Pdf to Document
import config   # Importing input and output directory paths
import audioengine


print("Converting PDF to document".center(400))
audioengine.speak("Converting PDF to document")

print("Enter name of your file without extension")
audioengine.speak("Enter name of your file without extension")
filename = input()

inputfile = config.inputpath+filename+".pdf"     # Saving the input file path
outputfile = config.outputpath+filename + \
    "-converted.docx"       # Saving the output file path

# convert pdf to docx
cv = Converter(inputfile)  # initialized a converter object
cv.convert(outputfile, start=0, end=None)  # converting pdf to docx
cv.close()      # closed the pdf file

print("Your file has been converted successfully".center(400))
audioengine.speak("Your file has been converted successfully")
