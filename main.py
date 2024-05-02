from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


word_data = pd.read_csv('data/french_words.csv')
word_dict = word_data.to_dict(orient="records")

####-------------words----------------####
current_words = []


def next_card():

    global current_words
    current_words = word_data.sample()
    print(type(current_words))
    french_word = current_words['French'].values[0]
    english_word = current_words['English'].values[0]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=f"{french_word}")




# def next_card():
#     current_words = random.choice(word_dict)
#
#     french_word = current_card
#     canvas.itemconfig(card_title, text="French")
#     canvas.itemconfig(card_word, text=current_card["French"])

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(canvas_image, image=back_img)


window = Tk()
window.title("Flashcards!")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

window.after(3000, func=flip_card)

canvas = Canvas(width=1000, height=600)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(500, 300, image=back_img)

canvas.itemconfig(canvas_image, image=front_img)
card_title = canvas.create_text(500, 150, text="French", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(500, 300, text="Placeholder", font=("Arial", 35, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


no_image = PhotoImage(file="images/wrong.png")
button = Button(image=no_image, highlightthickness=0, command=next_card)
button.grid(column=0, row=2)

yes_image = PhotoImage(file="images/right.png")
button = Button(image=yes_image, highlightthickness=0, command=next_card)
button.grid(column=1, row=2)



next_card()





window.mainloop()


