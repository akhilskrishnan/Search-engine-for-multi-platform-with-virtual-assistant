import speech_recognition as sr
import webbrowser
import tkinter as tk
from PIL import ImageTk, Image


def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def wikipedia_search(query):
    url = f"https://en.wikipedia.org/wiki/{query}"
    webbrowser.open(url)

def stackoverflow_search(query):
    url = f"https://stackoverflow.com/search?q={query}"
    webbrowser.open(url)

def github_search(query):
    url = f"https://github.com/search?q={query}"
    webbrowser.open(url)

def hearaudio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Taking input")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"Command: {query}")
            return query
        except sr.UnknownValueError:
            print("Couldn't Understand You.")
            return ""

def voice():
    query = hearaudio()
    if query:
        if "google" in query.lower():
            query = query.lower().replace("google", "").strip()
            google_search(query)
        elif "youtube" in query.lower():
            query = query.lower().replace("youtube", "").strip()
            youtube_search(query)
        elif "wikipedia" in query.lower():
            query = query.lower().replace("wikipedia", "").strip()
            wikipedia_search(query)
        elif "stackoverflow" in query.lower():
            query = query.lower().replace("stackoverflow", "").strip()
            stackoverflow_search(query)
        elif "github" in query.lower():
            query = query.lower().replace("github", "").strip()
            github_search(query)
        else:
            print("Please Tell a correct search option.")


def clickgoog():
    query = inputgoog.get()
    google_search(query)

def clickyt():
    query = inputyt.get()
    youtube_search(query)

def wkclick():
    query = inputwiki.get()
    wikipedia_search(query)

def stckclick():
    query = inputstacky.get()
    stackoverflow_search(query)

def github_clicked():
    query = inputgit.get()
    github_search(query)

def vsrch():
    voice()


window = tk.Tk()
window.title("Search Bot")
window.geometry("500x350")
window.configure(bg="#202020")


google_logo = ImageTk.PhotoImage(Image.open("google_logo.png").resize((40, 40)))
youtube_logo = ImageTk.PhotoImage(Image.open("youtube_logo.png").resize((40, 40)))
wikipedia_logo = ImageTk.PhotoImage(Image.open("wikipedia_logo.png").resize((40, 40)))
stackoverflow_logo = ImageTk.PhotoImage(Image.open("stackoverflow_logo.png").resize((40, 40)))
github_logo = ImageTk.PhotoImage(Image.open("github_logo.png").resize((40, 40)))


google_label = tk.Label(window, text="Google", fg="#ffffff", bg="#202020", font=("Times", 12))
google_label.grid(column=0, row=0, pady=10)
google_logo_label = tk.Label(window, image=google_logo, bg="#202020")
google_logo_label.grid(column=1, row=0)

youtube_label = tk.Label(window, text="YouTube", fg="#ffffff", bg="#202020", font=("Times", 12))
youtube_label.grid(column=0, row=1, pady=10)
youtube_logo_label = tk.Label(window, image=youtube_logo, bg="#202020")
youtube_logo_label.grid(column=1, row=1)

wikipedia_label = tk.Label(window, text="Wikipedia", fg="#ffffff", bg="#202020", font=("Times", 12))
wikipedia_label.grid(column=0, row=2, pady=10)
wikipedia_logo_label = tk.Label(window, image=wikipedia_logo, bg="#202020")
wikipedia_logo_label.grid(column=1, row=2)

stackoverflow_label = tk.Label(window, text="Stack Overflow", fg="#ffffff", bg="#202020", font=("Times", 12))
stackoverflow_label.grid(column=0, row=3, pady=10)
stackoverflow_logo_label = tk.Label(window, image=stackoverflow_logo, bg="#202020")
stackoverflow_logo_label.grid(column=1, row=3)

github_label = tk.Label(window, text="GitHub", fg="#ffffff", bg="#202020", font=("Times", 12))
github_label.grid(column=0, row=4, pady=10)
github_logo_label = tk.Label(window, image=github_logo, bg="#202020")
github_logo_label.grid(column=1, row=4)


inputgoog = tk.Entry(window, width=40)
inputgoog.grid(column=2, row=0, padx=10)
google_button = tk.Button(window, text="Search", command=clickgoog, bg="#4285f4", fg="#ffffff")
google_button.grid(column=3, row=0)

inputyt = tk.Entry(window, width=40)
inputyt.grid(column=2, row=1, padx=10)
youtube_button = tk.Button(window, text="Search", command=clickyt, bg="#ff0000", fg="#ffffff")
youtube_button.grid(column=3, row=1)

inputwiki = tk.Entry(window, width=40)
inputwiki.grid(column=2, row=2, padx=10)
wikipedia_button = tk.Button(window, text="Search", command=wkclick, bg="#000000", fg="#ffffff")
wikipedia_button.grid(column=3, row=2)

inputstacky = tk.Entry(window, width=40)
inputstacky.grid(column=2, row=3, padx=10)
stackoverflow_button = tk.Button(window, text="Search", command=stckclick, bg="#f48024", fg="#ffffff")
stackoverflow_button.grid(column=3, row=3)

inputgit = tk.Entry(window, width=40)
inputgit.grid(column=2, row=4, padx=10)
github_button = tk.Button(window, text="Search", command=github_clicked, bg="#171515", fg="#ffffff")
github_button.grid(column=3, row=4)

voice_button = tk.Button(window, text="Voice Search", command=vsrch, bg="#202020", fg="#ffffff")
voice_button.grid(column=2, row=5, pady=10)


window.mainloop()