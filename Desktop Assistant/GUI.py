from tkinter import *
from PIL import Image , ImageTk
import speech_to_text as stt
import action

# Color Pallet
BLUE = "#008DDA"
LIGHT_BLUE = "#41C9E2"
SKY_BLUE = "#ACE2E1"
PINK = "#F7EEDD"
FONT = "Courier"



# ----------------------Creating the window-------------------------
window = Tk()
window.title("Desktop Assistant")
window.geometry("550x400")
window.resizable(False, False)
window.config(bg=LIGHT_BLUE, padx=20,borderwidth=3, relief="raised")

# ----------------------Creating Functions-------------------------
def ask():
    user_val = stt.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, f'User --->{user_val} \n')
    if bot_val != None:
        text.insert(END, f"Bot <--- {str(bot_val)}\n")
    if bot_val == "ok sir":
        window.destroy()

def sent():
    send = text_input.get()
    bot = action.action(send)
    text.insert(END, f'User --->{send} \n')
    if bot != None:
        text.insert(END, f"Bot <--- {str(bot)}\n")
    if bot == "ok sir":
        window.destroy()
    

def delete():
    text.delete('1.0', "end")


# ----------------------Creating Labels-------------------------
text_label = Label(window, text="Desktop Assistant", bg=SKY_BLUE, font=(FONT, 15, "bold"))
text_label.grid(column=1, row=0, pady=10)


# ----------------------Creating text box-------------------------
text = Text(window, font=(FONT, 10, "bold"), bg=PINK, height=15, width=40)
text.place(x=1, y=2)
text.grid(column=1, row=1)

#----------------------Creating Entry box-------------------------
text_input = Entry(window, justify=CENTER, width=50)
text_input.place(x=1, y=2)
text_input.grid(column=1, row=3, pady=10)


# ----------------------Creating Buttons-------------------------
ask_btn = Button(window, text="Ask", bg=PINK, font=("Courier", 10, "bold"), width=10, borderwidth=3, relief=SOLID, command=ask)
ask_btn.grid(column=0, row= 4, pady=10)
sent_btn = Button(window, text="Sent", bg=PINK, font=("Courier", 10, "bold"), width=10, borderwidth=3, relief=SOLID, command=sent)
sent_btn.grid(column=1, row= 4, pady=10)
delete_btn = Button(window, text="Delete", bg=PINK, font=("Courier", 10, "bold"), width=10, borderwidth=3, relief=SOLID, command=delete)
delete_btn.grid(column=2, row= 4, pady=10)





window.mainloop()