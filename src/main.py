import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Text
from functools import partial
from data_player import play_data

def send_info():
    play_data(input_text.get(),key_text.get())

##keep it first
input_window = tk.Tk()

#variables
window_width = 300
window_height = 200

#window title
input_window.title("Input")

#window size
input_window.geometry(f"{window_width}x{window_height}+0+0")

#form
fields = {}

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
btn = ttk.Button(text='Input',command=send_info)
btn.pack()

#keep last- main loop
input_window.mainloop()
