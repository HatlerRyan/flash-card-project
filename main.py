from tkinter import *
import pandas as pd
import random

#----------------read the data-----------------#


def new_card():
    french_data = pd.read_csv("data/french_words.csv",)
    records = french_data.to_dict(orient='records')
    row_numb = 0
    random_number = random.randrange(0, 102)
    for row in records:
        row_numb += 1
        if row_numb == random_number:
            next_french = row['French']
            next_english = row['English']
            canvas.delete("french_title", "french_word")

            canvas.create_text(400, 150, text="French", font=("arial", 40, "italic"), tags="french_title")
            canvas.create_text(400, 263, text=next_french, font=("arial", 60, "bold"), tags="french_word")


# ------------------------UI----------------------------#

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCard App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR )
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"), tags="french_title")
canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"), tags="french_word")
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=check_image, background=BACKGROUND_COLOR, command=new_card)
wrong_button = Button(image=x_image, background=BACKGROUND_COLOR, command=new_card)
right_button.grid(column=0, row=2)
wrong_button.grid(column=1, row=2)





#----------------Flip and timer---------------#


window.mainloop()