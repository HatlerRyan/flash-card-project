from tkinter import *
import pandas as pd
import random


#----------------read the data-----------------#

new_word = {}
def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_side, image=card_front)
    french_data = pd.read_csv("data/french_words.csv", )
    french_words_to_learn = french_data.to_dict(orient='records')
    new_word = random.choice(french_words_to_learn)
    next_french = new_word['French']
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(next_word_up, text=next_french, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(language_title, text="English", fill="white")
    next_english = new_word['English']
    canvas.itemconfig(next_word_up, text=next_english, fill="white")



# ------------------------UI----------------------------#

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCard App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR )
card_side = canvas.create_image(400, 263, image=card_front)
language_title = canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
next_word_up = canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=check_image, background=BACKGROUND_COLOR, command=new_card)
wrong_button = Button(image=x_image, background=BACKGROUND_COLOR, command=new_card)
right_button.grid(column=0, row=2)
wrong_button.grid(column=1, row=2)

new_card()



window.mainloop()