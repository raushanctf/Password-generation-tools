import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import random
from tkinter import PhotoImage
import string
import pyautogui

window = tk.Tk()
window.title("Password generator")
logo = PhotoImage(file ="images/icon.png")
window.iconphoto(False, logo)
window.resizable(width=False, height=False)
window.configure(height=112, width=300)

def generate_func():
    Rau = Rau_variable.get()
    caja_contra.delete('1.0', tk.END)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    chars = lower + upper + num + symbols
    temp = random.sample(chars, Rau)
    lol = "".join(temp)
    
    caja_contra.insert(tk.END, lol)

    window.clipboard_clear() 
    window.clipboard_append(lol)
    
    pyautogui.alert(text="Generated password copied to clipboard.", title="Password generator")

Rau_entry = ttk.Entry(window)
Rau_variable = tk.IntVar()
Rau_entry.configure(justify="center",textvariable=Rau_variable)
Rau_entry.place(anchor="nw", relx=0.25, rely=0.12, x=0, y=0)

generate_button = ttk.Button(window)
generate_button.configure(text='Gen password')
generate_button.place(anchor="nw", relx=0.40, rely=0.37, x=0, y=0)
generate_button.configure(command=generate_func)

caja_contra = ScrolledText(window)
caja_contra.place(anchor="nw",relheight=0.23,relwidth=0.68,relx=0.24,rely=0.68,x=0,y=0)


if __name__ == "__main__":
    window.mainloop()