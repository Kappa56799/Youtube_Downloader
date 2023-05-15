from pytube import YouTube
import customtkinter as ctk
from threading import Thread
from moviepy.editor import *

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.geometry("500x500")
radiovar = ctk.IntVar()

def download():
    progressbar.set(0)
    link = entry1.get()
    yt = YouTube(link)

    video = yt.streams.get_highest_resolution()
    progressbar.set(50)
    video.download()
    print("Video Downloaded")
    progressbar.set(100)


def downloadFile():
    Thread(target=download).start()

def UploadAction(event=None):
    filename = ctk.filedialog.askopenfilename()
    print('Selected:', filename)

    video = VideoFileClip(filename)
    video.audio.write_audiofile(filename[:-4] + ".mp3")
    

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Youtube Downloader", font=("Arial", 40))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, width=350, height=30, placeholder_text="Enter the link")
entry1.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, width=150, text="Download", command=downloadFile)
button.pack(pady=12, padx=10)

progressbar = ctk.CTkProgressBar(master=frame,mode="determinate", width=400)
progressbar.pack(pady=20, padx=10)
progressbar.set(0)

label = ctk.CTkLabel(master=frame, text="Convert A file from MP4 to MP3", font=("Arial", 40))
label.pack(pady=12, padx=10)


button = ctk.CTkButton(master=frame, width=150, text="Select A File and Convert", command=UploadAction)
button.pack(pady=12, padx=10)


root.mainloop()
