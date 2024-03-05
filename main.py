from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_loc):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res = stream.get_highest_resolution()

        highest_res.download(save_loc)
        print("Download completed!!")

    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder{folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the Youtube video url: ")
    save_location = open_file_dialog()

    if not save_location:
        print("Please select a folder to save the video...")
    else:
        print("Downloading...")
        download_video(video_url, save_location)
