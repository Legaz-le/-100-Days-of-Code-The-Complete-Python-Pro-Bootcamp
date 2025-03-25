
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwords():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


        password_list = [choice(letters) for _ in range(randint(8, 10))]
        password_symbol = [choice(symbols) for _ in range(randint(2,4))]
        password_number = [choice(numbers)for _ in range(randint(2, 4))]

        password_list = password_list + password_number + password_symbol

        shuffle(password_list)

        passwords = "".join(password_list)

        password_entry.insert(0,passwords)
        pyperclip.copy(passwords)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    websites = website_entry.get()
    emails = email_entry.get()
    passwords = password_entry.get()
    new_data = {
        websites: {
                "email": emails,
                "password": passwords,
        }
    }

    if len(websites) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        with open("password.json","r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

        with open("password.json", "w") as data_file:
            json.dump( data, data_file, indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
#Image
canvas =  Canvas(width=200,height=200)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= photo_image)
canvas.grid(row=0,column=1)
#Labels
website = Label(text="Website:")
website.grid(row=1,column=0)
email_username = Label(text="Email/Username:")
email_username.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)
#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0,"hardcore@gmai.com")
password_entry= Entry(width=21)
password_entry.grid(row=3,column=1)
#Buttons
generate_password = Button(text="Generate Password",command=generate_passwords)
generate_password.grid(row=3,column=2)
add = Button(text="Add",width=36,command=save)
add.grid(row=4,column=1, columnspan=3)





window.mainloop()