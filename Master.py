from subprocess import call  # Calling different files in one file
import time  # Module for delay
import speech_recognition as sr  # Speech Recognition
import sys  # System Module
import audioengine  # importing audio engine


# Introduction
print("Welcome to the Suite Converter\n".center(400))
audioengine.speak("Welcome to the Suite Converter")
print("Following are the Services we provide:")
audioengine.speak("Following are the Services we provide")
print("\n A.Document to PDF")
audioengine.speak("Document to PDF")
print("\n B.PDF to Document")
audioengine.speak("PDF to Document")
print("\n C.Text to Audio file")
audioengine.speak("Text to Audio file")
print("\n D.Voice to Text file")
audioengine.speak("Voice to Text file")
print("\n E.Compiling multiple Images to PDF")
audioengine.speak("Compiling multiple Images to PDF")
print("\n F.Extraction of multiple Images from a PDF")
audioengine.speak("Extraction of multiple Images from a PDF")
print("\n G.Inter conversion of Images\n\n")
audioengine.speak("Inter conversion of Images")
time.sleep(1)
# Taking choice as input in audio form and converting to text


def takecom():
    audioengine.speak("Enter the option")
    choiceinput = (input("Enter the option....\n".center(400)))
    return choiceinput


# for main function
if __name__ == "__main__":

    # Checking for choice and calling the respective python scripts
    while (1):
        query = takecom()

        if "1" or "A" in query:
            # Calling file for docx to pdf conversion
            call(["python", "doc2pdf.py"])

        elif "2" or "B" in query:
            call(["python", "pdf2doc.py"])      # Calling file for pdf to docx

        elif "3" or "C" in query:
            # Calling file for Text to speech
            call(["python", "text2speech.py"])

        elif "4" or "D" in query:
            # Calling file for speech to text
            call(["python", "speech2text.py"])

        elif "5" or "E" in query or '5' in query:
            # Calling file for multiple images to pdf
            call(["python", "images2pdf.py"])

        elif "6" or "F" in query or 'six' in query:
            # Calling file for pdf to multiple images
            call(["python", "pdf2images.py"])

        elif "7" or "G" in query:
            call(["python", "imageconv.py"])  # Interconversion of Images

        elif query == 'none':  # If no choice given
            continue

        else:
            print("Invalid Input")  # If incorrect choice given
            continue

        print("Do you want to convert again?(Yes/No)")
        audioengine.speak("Do you want to convert again")

        def takech():
            # Listening the choice in audio form
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say the option....\n".center(400))
                audioengine.speak("Say Yes or No")
                audio = r.listen(source)

            # Recognising and converting the choice in text
            try:
                print("Recognising....")
                text = r.recognize_google(audio, language='en-in')
                print(text, "\n")

            # Backup if choice not understood
            except Exception:
                audioengine.speak("Error...")
                print("Try Again..")
            return text

        query1 = takech()
        if 'yes' in query1:
            print(" A.Document to PDF \n\n B.PDF to Document \n\n C.Text to Audio file \n\n D.Voice to Text file \n\n E.Compiling multiple Images to PDF \n\n F.Extraction of multiple Images from a PDF \n\n G.Inter conversion of Images\n\n")
            continue

        print("Thank You for converting".center(400))
        audioengine.speak("Thank you for converting")
        print("Developed by Team <define>".center(500))
        audioengine.speak("Developed by Team Define")
        sys.exit()
