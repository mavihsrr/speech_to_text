import os
import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()

def transcribe_speech():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print("Request error: ", e)

#text-to-Speech function
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')


def search_files_and_directories(query):
    results = []
    for root, dirs, files in os.walk('/'):  
        for file in files:
            if query.lower() in file.lower():
                results.append(os.path.join(root, file))
        for dir in dirs:
            if query.lower() in dir.lower():
                results.append(os.path.join(root, dir))
    return results


while True:
    query = transcribe_speech()
    if query:
        search_results = search_files_and_directories(query)
        if len(search_results) > 0:
            print("Search results:")
            for result in search_results:
                print(result)
        else:
            print("No files or directories found matching the search query.")
