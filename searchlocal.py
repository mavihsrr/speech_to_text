import speech_recognition as sr
import pyttsx3
import os

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def perform_local_search(query, path):
    matches = []
    try:
        # Iterate over all items in the given path
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                # Check if the query is present in the file name
                if query.lower() in item.lower():
                    matches.append(item_path)
            elif os.path.isdir(item_path):
                # Recursively search within directories
                matches.extend(perform_local_search(query, item_path))
    except PermissionError:
        # Handle cases where access to certain directories is restricted
        pass

    return matches

def process_speech():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

        try:
            # Use the speech recognition engine to convert speech to text
            query = recognizer.recognize_google(audio)
            print("You said:", query)

            # Perform the local search based on the user's query
            root_dir = "/"  # Modify this according to your operating system
            results = perform_local_search(query, root_dir)

            if results:
                # Convert the search results to speech using the text-to-speech engine
                engine.say("Here are the matching files and directories:")
                for result in results:
                    print(result)
            else:
                engine.say("No matching files or directories found.")

            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("An error occurred while processing your request:", str(e))

# Call the process_speech function to start the voice search
process_speech()
