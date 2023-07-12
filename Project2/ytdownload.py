from pytube import YouTube
import tkinter as tk
from tkinter import ttk
def download_video(event=None):
    url = url_entry.get()
    quality = quality_var.get()
    yt = YouTube(url, on_progress_callback=on_progress)
    video = yt.streams.filter(res=quality).first()
    if quality in ["1080p","2160p","1440p"]:
        print("Audio Cannot be downloaded beacause high resolution ")
    if not video:
        video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    video.download()
def download_audio():
    url = url_entry.get()
    yt = YouTube(url, on_progress_callback=on_progress)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
def on_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size
    progress_var.set(progress)
    progress_label.config(text=f"{progress:.0%}")
    root.update_idletasks()

root = tk.Tk()
root.title("YouTube Video Downloader")
url_label = tk.Label(root, text="Enter YouTube video URL:")
url_label.pack()

url_entry = tk.Entry(root,width=30)
url_entry.pack()
url_entry.bind("<Return>", download_video)

quality_label = tk.Label(root, text="Select video quality:")
quality_label.pack()

quality_var = tk.StringVar(root)
quality_var.set("1080p") # default value

quality_options = ["144p","240p","360p","480p", "720p", "1080p","1440p","2160p"]

quality_menu = tk.OptionMenu(root, quality_var, *quality_options)
quality_menu.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()
download_audio=tk.Button(root,text="Audio",command=download_audio)
download_audio.pack()
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=1)
progress_bar.pack()

progress_label = tk.Label(root, text="0%")
progress_label.pack()

root.mainloop()
