from modules import *

root = tkinter.Tk()
root.title('Digits')
# Code to add widgets will go here...
label = tkinter.Label(root, 'Угадай)')
frame = tkinter.Frame(root)
frame.pack(fill=tkinter.BOTH, expand=True)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

guess_digit = None
answer = None

def next_step():
	pass

response = None

entry_guess = tkinter.Entry(frame, width=7, textvariable=guess_digit)
entry_answer = tkinter.Entry(frame, width=20, textvariable=answer)

label_rules = tkinter.Label(frame, text=text.rules)
label_attempt = tkinter.Label(frame,text=text.attempt)
label_question_start = tkinter.Label(frame,text=text.wanna_play)
label_response = tkinter.Label(frame,text=response)
action_button = tkinter.Button(frame,text='Да',command=next_step)

label_rules.grid(row=0,column=0,colspan=2)

action_button.grid(row=2,column=0,colspan=2)

entry_guess.focus()

root.mainloop()

#
#
#
#

import tkinter as tk

# Declare global variables
temp_c = None
temp_f = None

# This function is called whenever the button is pressed
def convert():

    global temp_c
    global temp_f

    # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
        val = temp_c.get() # like input()
        temp_f.set((val * 9.0 / 5) + 32)
    except:
        pass

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container, specify that we want it to grow with window size
frame.pack(fill=tk.BOTH, expand=True)

# Allow middle cell of grid to grow when window is resized
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# Variables for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()

# Create widgets
entry_celsius = tk.Entry(frame, width=7, textvariable=temp_c)
label_unitc = tk.Label(frame, text="°C")
label_equal = tk.Label(frame, text="is equal to")
label_fahrenheit = tk.Label(frame, textvariable=temp_f)
label_unitf = tk.Label(frame, text="°F")
button_convert = tk.Button(frame, text="Convert", command=convert)

# Lay out widgets
entry_celsius.grid(row=0, column=1, padx=5, pady=5)
label_unitc.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
label_equal.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
label_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
label_unitf.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.E)

# Place cursor in entry box by default
entry_celsius.focus()

# Run forever!
root.mainloop()
