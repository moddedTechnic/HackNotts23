import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Text
from functools import partial
from data_player import play_data
from cryptography.fernet import Fernet

global key_text

def send_info():
    play_data(input_text.get(),key_text.get())

def generate_secret_key():
    print('putas')
    key_text.delete(0, tk.END)
    key_text.insert(0, Fernet.generate_key())
    #lbl = Fernet.generate_key()

##keep it first
input_window = tk.Tk()

#variables
window_width = 300
window_height = 200

#window title
input_window.title("Input")

#window size
input_window.geometry(f"{window_width}x{window_height}+0+0")

#Input
message = tk.Label(input_window, text="Input")
message.pack()
input_text = ttk.Entry()
input_text.pack(fill=tk.Y)

#Key
message2 = tk.Label(input_window, text="Key")
message2.pack()
key_text = ttk.Entry()
key_text.pack(fill=tk.Y)

input_send = input_text.get()
key_send = key_text.get()

#key button
intput_btn = ttk.Button(input_window ,text='Input',command=send_info)
intput_btn.pack()

#key button
genKey_btn = ttk.Button(input_window ,text='Generate Key',command=generate_secret_key)
genKey_btn.pack()

#keep last- main loop
input_window.mainloop()
