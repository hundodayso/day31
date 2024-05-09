from tkinter import *
from tkinter import messagebox

import pandas
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





# def next_card():
#
#     global current_words, flip_timer,word_data
#     window.after_cancel(flip_timer)
#     current_words = word_data.sample()
#     print(type(current_words))
#     french_word = current_words['French'].values[0]
#     english_word = current_words['English'].values[0]
#
#     print(f"French: {french_word} \nEnglish: {english_word}")
#     canvas.itemconfig(card_title, text="French",  fill="black")
#     canvas.itemconfig(canvas_image, image=front_img)
#     canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
#     flip_timer = window.after(3000, func=flip_card)




def next_card():
    global current_words, flip_timer
    window.after_cancel(flip_timer)
    current_words = random.choice(to_learn)
    french_word = current_words["French"]
    print(french_word)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_word, text=current_words["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_words
    english_word = current_words["English"]
    canvas.itemconfig(card_title, text="English",  fill="white")
    canvas.itemconfig(card_word, text=f"{english_word}", fill="white")
    canvas.itemconfig(canvas_image, image=back_img)

def is_known():
    to_learn.remove(current_words)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


    next_card()



window = Tk()
window.title("Flashcards!")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

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
button = Button(image=yes_image, highlightthickness=0, command=is_known)
button.grid(column=1, row=2)



next_card()





window.mainloop()


