#Made by Kacper Palka
#Date: 10/10/2021
#This program is a youtube downloader that can download videos and convert mp4 files to mp3 files
from pytube import YouTube
import customtkinter as ctk
from threading import Thread
from moviepy.editor import *

#Sets the apperance of the program based on the users theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

#creates the window
root = ctk.CTk()
root.geometry("500x500")

#function to download the video
def download():
    progressbar.set(0)
    link = entry1.get()
    yt = YouTube(link)

    
    video = yt.streams.get_highest_resolution()
    progressbar.set(50)
    video.download()
    print("Video Downloaded")
    progressbar.set(100)

#function to start the download thread
def downloadFile():
    Thread(target=download).start()

#function to upload a file and convert it to mp3
def UploadAction(event=None):
    filename = ctk.filedialog.askopenfilename()
    print('Selected:', filename)
    progressbar2.set(50)

    #converts the file
    video = VideoFileClip(filename)
    video.audio.write_audiofile(filename[:-4] + ".mp3")
    progressbar2.set(100)
    

#GUI
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

progressbar2 = ctk.CTkProgressBar(master=frame,mode="determinate", width=400)
progressbar2.pack(pady=20, padx=10)
progressbar2.set(0)

#runs the program
root.mainloop()
