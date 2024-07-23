from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# PyPassword Generator
def password_generator():
    let = random.randint(8, 10)
    num = random.randint(2, 4)
    sym = random.randint(2, 4)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y',
               'Z']
    numbers = ['0', '1', ' 2', '3', '4', '5', '6', ' 7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    p_letters = [random.choice(letters) for _ in range(let)]
    p_numbers = [random.choice(numbers) for _ in range(num)]
    p_symbols = [random.choice(symbols) for _ in range(sym)]

    password_list = p_letters + p_numbers + p_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}, Password: {password}.\n"
                                                              f" Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # read old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # replace old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # save them all together
                    json.dump(data, data_file, indent= 4)

            finally:
                web_input.delete(0, END)
                password_input.delete(0, END)

# ----------------------------  ------------------------------- #
def search_func():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data Found!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error!", message=f"No details of {website} exists!")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=("Times New Roman", 12, "bold"))
web_label.grid(row=1, column=0)

email_label = Label(text="Email/ Username:", font=("Times New Roman", 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Times New Roman", 12, "bold"))
password_label.grid(row=3, column=0)

web_input = Entry(width=30)
web_input.grid(row=1, column=1)
web_input.focus()

email_input = Entry(width=48)
email_input.insert(0, "Saditi.7@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

search = Button(text="Search", highlightthickness=0, width= 13, command= search_func)
search.grid(row=1, column=2)

generate = Button(text="Generate Password", command=password_generator, highlightthickness=0)
generate.grid(row=3, column=2)

add = Button(text="Add", width=36, bg="blue", fg="white", command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
