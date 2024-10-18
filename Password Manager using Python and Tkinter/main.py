from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    entry3.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_letters = random.sample(letters, random.randint(3,6))
    random_numbers = random.sample(numbers, random.randint(3,6))
    random_symbols = random.sample(symbols, random.randint(3,6))
    password = random_letters + random_numbers + random_symbols
    random.shuffle(password)
    password = "".join(password)
    entry3.insert(0,string = password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    if len(entry1.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showwarning(title="OOPS", message="Do not leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=entry1.get(),message=f"You entered:\nMAIL: {entry2.get()}\nPASSWORD: {entry3.get()}\n is this okay?")
    if is_ok:
        with open("data.txt", 'a') as f:
            f.writelines([entry1.get()," | ",entry2.get()," | ",entry3.get(),"\n"])
            entry1.delete(0,END)
            entry3.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row = 0)

website_label = Label(text ="Website:")
website_label.grid(column = 0 , row =1)

entry1 = Entry(width=35)
entry1.grid(column =1, row  =1, columnspan=2)

email_label = Label(text ="Email/User Name:")
email_label.grid(column = 0 , row =2)

entry2 = Entry(width=35)
entry2.grid(column =1, row  =2, columnspan=2)

pw_label = Label(text ="Password:")
pw_label.grid(column = 0 , row =3)

entry3 = Entry(width=21)
entry3.grid(column =1, row =3)

button1 = Button(text="generate", command=generator)
button1.grid(column=2, row = 3)

button2 = Button(text="ADD", width=36, command=save_pw)
button2.grid(column =1, row = 4, columnspan = 2)


window.mainloop()
