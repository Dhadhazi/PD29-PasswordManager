from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    return "".join(password_list)


def add_generated_password():
    password_input.delete(0, END)
    password = generate_password()
    pyperclip.copy(password)
    password_input.insert(0, password)


def clear_input_fields():
    website_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()


def no_empty_check():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(message="Please don't leave any field empty!")
        return False
    return True


def get_inputs():
    data = {
        website_input.get():
            {
                "email": email_input.get(),
                "password": password_input.get()
            }
    }
    return data


def inputs_are_ok():
    return messagebox.askokcancel(title={website_input.get()},
                                  message=f"These are the details entered: \nEmail: {email_input.get()} "
                                          f"\nPassword: {password_input.get()} \n Is it ok to save?")


def get_file_data(filename):
    try:
        with open(filename, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def write_file(filename, data):
    with open(filename, mode="w") as file:
        json.dump(data, file, indent=4)


def save_input():
    if no_empty_check():
        if inputs_are_ok():
            try:
                data = get_file_data("data.json")

            except FileNotFoundError:
                write_file(filename="data.json", data=get_inputs())

            else:
                data.update(get_inputs())
                write_file(filename="data.json", data=data)

            finally:
                clear_input_fields()


website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", command=add_generated_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_input)
add_button.grid(column=1, row=4, columnspan=2)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "usual@email.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

window.mainloop()
