from PIL import Image, ImageTk
import tkinter as tk
import time
import subprocess

def display_image(image_path, duration, command):
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry(f"+{root.winfo_screenwidth() // 2 - 250}+{root.winfo_screenheight() // 2 - 150}")
    img = Image.open(image_path)
    img = img.resize((500, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.pack()
    label.image = photo

    def run_command():
        root.destroy()
        subprocess.call(command)

    root.after(duration * 1500, run_command) 
    root.mainloop()

display_image("Logo.png", 3, ["python", "Intro.py"])