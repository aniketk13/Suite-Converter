from docx2pdf import convert  # Conversion of document to pdf module
import config  # Importing input and output directory paths
import audioengine


print("Converting document to PDF".center(400))
audioengine.speak("Converting document to PDF")

print("Enter the name of file without extension:")
audioengine.speak("Enter the name of file without extension")
filename = input()

inputfile = (config.inputpath+filename+".docx")  # Saving the input file path

outputfile = config.outputpath+filename + \
    "-converted.pdf"  # Saving the output file path

convert(inputfile, outputfile)

print("Your file has been converted successfully".center(400))
audioengine.speak("Your file has been converted successfully")
