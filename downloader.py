from pytube import YouTube
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.geometry("500x500")
radiovar = ctk.IntVar()

def download():
    link = entry1.get()
    yt = YouTube(link)

    if radiovar.get() == 1:
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Video Downloaded")

    elif radiovar.get() == 2:
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        print("Audio Downloaded")



def radiobutton_event():
    print("radiobutton toggled, current value: " + radiovar.get())

    

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Youtube Downloader", font=("Arial", 20))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Enter the link")
entry1.pack(pady=12, padx=10)

radio1 = ctk.CTkRadioButton(master=frame, text="Video", variable=radiovar, value="1")
radio1.pack(pady=12, padx=10)

radio2 = ctk.CTkRadioButton(master=frame, text="Audio", variable=radiovar, value="2")
radio2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Download", command=download)
button.pack(pady=12, padx=10)

root.mainloop()
