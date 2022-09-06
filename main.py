from tkinter import *


# ------------------------UI----------------------------#

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCard App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR )
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=check_image, background=BACKGROUND_COLOR)
wrong_button = Button(image=x_image, background=BACKGROUND_COLOR)
right_button.grid(column=0, row=2)
wrong_button.grid(column=1, row=2)

window.mainloop()