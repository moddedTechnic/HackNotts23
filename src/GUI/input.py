import tkinter as tk
from tkinter import ttk


##keep it first
input_window = tk.Tk()

#variables
window_width = 400
window_height = 400

#window title
input_window.title("Input")

#window size
input_window.geometry(f'{window_width}x{window_height}+0+0')
input_window.resizable(False, False)

#buttons
submit_input = ttk.Button(
   input_window,
   text="Input"
)

submit_input.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#message = tk.Label(input_window, text="Hello, World!")
#message.pack()

#keep last- main loop
input_window.mainloop()