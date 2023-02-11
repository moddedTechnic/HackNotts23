import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Text
from data_player import play_data

##keep it first
input_window = tk.Tk()

#variables
window_width = 350
window_height = 100

#window title
input_window.title("Input")

#window size
input_window.geometry(f"{window_width}x{window_height}")

#form
fields = {}

fields['input'] = ttk.Label(text='Input:')
fields['input'] = ttk.Entry()

for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Input').pack(anchor=tk.W, padx=10, pady=5)



#message = tk.Label(input_window, text="Hello, World!")
#message.pack()

#keep last- main loop
input_window.mainloop()