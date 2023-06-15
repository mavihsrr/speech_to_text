import speech_recognition as sr


recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    if text.lower() == "stop":
        print("Recording stopped.")
    else:
        print("Keyword not spoken. Recording continued.")
except sr.UnknownValueError:
    print("Unable to recognize speech")
except sr.RequestError as e:
    print("Error:", str(e))


#Dependicies - 
###sudo apt-get install portaudio19-dev
####pip install pyaudio
##pip3 install SpeechRecognition

