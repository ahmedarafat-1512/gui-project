from tkinter import *

from tkinter import ttk, filedialog
from pytube import YouTube

root = Tk()
root.title("YouTube Downloader")
root.geometry("400x400")
root.config(bg="#89A8B2")

folder_path = StringVar()

def select_folder(): folder_path.set(filedialog.askdirectory() or ".")

def download_video(resolution):
    try:
        yt = YouTube(link_entry.get(), on_progress_callback=update_progress)
        stream = yt.streams.get_highest_resolution() if resolution == "high" else yt.streams.get_lowest_resolution() if resolution == "low" else yt.streams.filter(only_audio=True).first()
        stream.download(output_path=folder_path.get())
        status_label.config(text="Download Successful!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

def update_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress['value'] = percentage
    root.update_idletasks()

Label(root, text="YouTube Downloader", font=("Arial", 16, "bold"), bg="#89A8B2", fg="#d6bd98").pack(pady=10)
Label(root, text="Add your YouTube link here", font=("Arial", 10), bg="#89A8B2", fg="#4d4d4d").pack(pady=5)
link_entry = Entry(root, width=50); link_entry.pack(pady=10); link_entry.focus()
Button(root, text="Select Folder", command=select_folder).pack(pady=5)
Label(root, textvariable=folder_path, font=("Arial", 10), fg="blue", bg="#89A8B2").pack(pady=5)

Button(root, text="High Resolution", command=lambda: download_video("high"), width=20, height=1, bg="#d6bd98").pack(pady=5)
Button(root, text="Low Resolution", command=lambda: download_video("low"), width=18, height=1, bg="#d6bd98").pack(pady=5)
Button(root, text="Audio Only", command=lambda: download_video("audio"), width=16, height=1, bg="#d6bd98").pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

status_label = Label(root, text="", font=("Arial", 12), bg="#89A8B2", fg="white"); status_label.pack(pady=10)

root.mainloop()
