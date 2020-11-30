from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


def clear_input_fields():
    website_input.delete(0,END)
    password_input.delete(0,END)
    website_input.focus()


def get_inputs():
    return f"{website_input.get()} | {email_input.get()} | {password_input.get()} \n"


def save_input():
    with open("data.txt", mode="a") as file:
        file.write(get_inputs())
        clear_input_fields()


website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password")
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