import os
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from yt_dlp import YoutubeDL

def download_video():
    url = url_entry.get()
    format_choice = format_var.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    save_path = filedialog.askdirectory()
    if not save_path:
        return

    try:
        if format_choice == "Best Video":
            fmt = "best"
        elif format_choice == "Audio Only":
            fmt = "bestaudio"
        else:
            fmt = "best"

        ydl_opts = {
            'format': fmt,
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'noplaylist': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo("Success", f"Downloaded:\n{info.get('title')}")

    except Exception as e:
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"Failed to download.\nError: {str(e)}")

# GUI
root = Tk()
root.title("YouTube Video Downloader Pro")
root.geometry("550x300")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 11), padding=6, background="#00aa5b", foreground="white")
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Arial", 12))
style.configure("TEntry", padding=6)

Label(root, text="YouTube Downloader Pro", font=("Arial Black", 18), bg="#1e1e2f", fg="#00ffcc").pack(pady=10)
Label(root, text="Enter YouTube URL:").pack(pady=5)

url_entry = Entry(root, width=60, font=("Arial", 10))
url_entry.pack(pady=5)

Label(root, text="Select Format:").pack(pady=5)
format_var = StringVar(value="Best Video")
format_menu = ttk.Combobox(root, textvariable=format_var, values=["Best Video", "Audio Only"], state="readonly", width=20)
format_menu.pack(pady=5)

ttk.Button(root, text="Download", command=download_video).pack(pady=20)

Label(root, text="Developed by: Mohammad Nagani \n Faiz Idrisi \n Moinuddin khan \n Aman khan", font=("Arial", 10), fg="#888888").pack(side=BOTTOM, pady=10)

root.mainloop()
