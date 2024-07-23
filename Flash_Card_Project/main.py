from tkinter import *
import pandas
import random
import os
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARD = random.choice(to_learn)
    french_word = CURRENT_CARD["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    if len(to_learn) > 1:
        to_learn.remove(CURRENT_CARD)
        data_words = pandas.DataFrame(to_learn)
        data_words.to_csv("data/words_to_learn.csv", index=False)
        print(len(to_learn))
    else:
        messagebox.showinfo(title="There's no word to learn",
                            message="Congratulation! You've reviewed all the words!\n"
                                    "You good, keep going!")
        os.remove("data/words_to_learn.csv")

    next_card()

def flip_card():
    global CURRENT_CARD
    eng_word = CURRENT_CARD["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=eng_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)




window = Tk()

flip_timer = window.after(3000, func=flip_card)

window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)




canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back = PhotoImage(file="images/card_back.png")

card_front = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 260, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

tick = PhotoImage(file="images/right.png")
known_button = Button(image=tick, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
