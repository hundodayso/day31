from tkinter import *
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashcards!")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=1000, height=600)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(500, 300, image=front_img)

#timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button = Button(text="Yes", width=10)
button.grid(column=0, row=2)

button = Button(text="No", width=10)
button.grid(column=1, row=2)



window.mainloop()


