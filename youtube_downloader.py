from pytube import YouTube
from tkinter import *
from tkinter import messagebox

youtube_app = Tk()
youtube_app.title("YouTube Downloader")
youtube_app.geometry("400x100")
youtube_app.config(background="#333")
# youtube_app.resizable(False, False)


def css():
    text = Label(youtube_app, text="YouTube Video", bg="red", fg="white")
    text.grid(row=1, column=0, pady=5, padx=5)

    link = Entry(youtube_app, width=48, textvariable=url)
    link.grid(row=1, column=1, pady=5, padx=5)

    btn = Button(youtube_app, width=20, text="Download", height=1, borderwidth=0,
             font=("Times"), bg="#4AA96C", fg="white", command=btn_fun)
    btn.grid(row=3, column=1, pady=5, padx=5)


def btn_fun():
    link_value = url.get()
    video = YouTube(link_value)
    video.streams.get_highest_resolution().download(output_path="D:\15 Development\25 Data Analyst\13 Google Course")

    messagebox.showinfo("Download Successful!!")


url = StringVar()

css()
youtube_app.mainloop()
