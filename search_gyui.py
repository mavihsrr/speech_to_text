import os
import speech_recognition as sr
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

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

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')
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

def open_path(path):
    try:
        if os.path.isfile(path):
            os.startfile(path)
        elif os.path.isdir(path):
            os.system(f'explorer "{path}"')
    except OSError:
        messagebox.showerror("Error", "Failed to open the file or directory.")

window = tk.Tk()
window.title("Search Results")
window.geometry("400x400")
listbox = tk.Listbox(window, selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH, expand=True)

while True:
    query = transcribe_speech()
    if query:
        search_results = search_files_and_directories(query)
        if search_results:
            listbox.delete(0, tk.END)  
            for result in search_results:
                listbox.insert(tk.END, result)
            def on_double_click(event):
                selection = listbox.curselection()
                if selection:
                    index = selection[0]
                    path = listbox.get(index)
                    open_path(path)
            listbox.bind("<Double-Button-1>", on_double_click)

            window.deiconify()  
            window.mainloop()
        else:
            speak("No files or directories found matching the search query.")
