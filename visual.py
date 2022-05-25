from modules import *

root = tkinter.Tk()
root.title('Digits')
# Code to add widgets will go here...
label = tkinter.Label(root, )
frame = tkinter.Frame(root)
frame.pack(fill=tkinter.BOTH, expand=True)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

guess_digit = None
answer = None


def next_step():
    pass


user_response = None

entry_by_user = tkinter.Entry(frame, width=7, textvariable=user_response)

label_rules = tkinter.Label(frame, text=text.rules)
label_attempt = tkinter.Label(frame, text=text.attempt)
label_question_start = tkinter.Label(frame, text=text.wanna_play)
label_response = tkinter.Label(frame, text=response)
action_button = tkinter.Button(frame, text='Да', command=next_step)

label_rules.grid(row=0, column=0, columnspan=2)
label_question_start.grid(row=1, column=0)
lab
entry_by_user.grid(row=1, column=1)
action_button.grid(row=2, column=0, columnspan=2)

entry_by_user.focus()

root.mainloop()

#
#
#
#
