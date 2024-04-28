from tkinter import *
from tkinter import messagebox
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

word_data = pd.read_csv('data/french_words.csv')

####-------------words----------------####


def create_word():

    words = word_data.sample()
    french_word = words['French'].value[0]
    english_word = words['English'].value[0]

    canvas.itemconfig(visible_word, text=f"{french_word}")




window = Tk()
window.title("Flashcards!")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=1000, height=600)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(500, 300, image=front_img)
language = canvas.create_text(500, 150, text="French", font=("Ariel", 30, "italic"))
visible_word = canvas.create_text(500, 300, text="Oui", font=("Arial", 35, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


no_image = PhotoImage(file="images/wrong.png")
button = Button(image=no_image, highlightthickness=0, command=create_word)
button.grid(column=0, row=2)

yes_image = PhotoImage(file="images/right.png")
button = Button(image=yes_image, highlightthickness=0, command=create_word)
button.grid(column=1, row=2)






window.mainloop()


