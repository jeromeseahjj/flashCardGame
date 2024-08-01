# ---------------------------- IMPORT ------------------------------- #
from tkinter import *
import pandas as pd
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
else:
    to_learn = df.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #

def generate():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_card, image=card_front)
    flip_timer = window.after(3000, func=flip)

def flip():
    canvas.itemconfig(canvas_card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash me Plz")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
cross_image = PhotoImage(file="images/wrong.png")
unknown_button  = Button(image=cross_image, command=generate)
unknown_button.grid(row=1,column=0)
unknown_button.config(highlightthickness=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)
known_button.config(highlightthickness=0)

generate()

window.mainloop()