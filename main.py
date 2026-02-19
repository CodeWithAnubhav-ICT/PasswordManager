from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD HISTORY --------------------------------- #
def show_passwords():
    # Passwords Window
    passwords = Toplevel()
    passwords.title("Password Manager")
    passwords.wm_iconphoto(False, PhotoImage(file="icon.png"))
    passwords.config(pady=50, padx=50, border=0,bg="black")
    passwords.resizable(False, False)
    # Data Label
    data_label = Label(passwords,text="Passwords:", bg="black",fg="Red", font=("Courier", 15, "bold"),pady=10)
    data_label.pack()
    # Reading Data
    with open("data.txt","r") as file:
        content = file.read()
    # Text Widget
    password = Text(passwords,height=18,width=55,bg="black",fg="white",highlightthickness=0,relief="flat")
    password.delete(1.0,END)
    password.insert(END,content)
    password.pack()

    passwords.mainloop()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    password_entry.delete(0,END)
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_entry.insert(END,string=generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website)==0  or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!",message="Do not leave any fields empty",icon="error")
    else:
        confirm = messagebox.askokcancel(title=website,message=f"These are the details entered:\n"
                                                     f"Username: {username}\nPassword: {password}\nDo You want to save?")

        if confirm:
            filepath = "data.txt"
            with open(filepath,"a") as file:
                data = f"{website} | {username} | {password}\n"
                file.write(data)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.wm_iconphoto(False, PhotoImage(file="icon.png"))
window.config(pady=50,padx=50,border=0,relief="solid",bg="black")
window.resizable(False,False)
window.rowconfigure((1,2,3,4,5),pad=5)
window.columnconfigure((1,2,3,4),pad=5)

# Canvas
canvas = Canvas(height=200,width=200,highlightthickness=0,bg="black")
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:", fg="white", font=("Courier",10,"bold"),bg="black")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:", fg="white", font=("Courier",10,"bold"),bg="black")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:", fg="white", font=("Courier",10,"bold"),bg="black")
password_label.grid(column=0,row=3)

credit_label = Label(text="Created with 💖\nby Anubhav\n@ICT Mumbai", fg="white", font=("Courier",10,"bold"),bg="black")
credit_label.grid(column=0,row=4,rowspan=2)

# Entry
website_entry = Entry(width=52,relief="solid")
website_entry.focus()
website_entry.insert(END, string="")
website_entry.grid(column=1,row=1,columnspan=2)

username_entry = Entry(width=52,relief="solid")
username_entry.insert(END, string="someone@gmail.com")
username_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=33,relief="solid")
password_entry.insert(END, string="")
password_entry.grid(column=1,row=3,columnspan=1)

# Buttons
generate_button = Button(text="Generate Password",border=1,highlightthickness=0,
                         relief="solid",command=generate_password)
generate_button.grid(column=2,row=3,columnspan=1)

add_button = Button(text="Add", width=44, border=1, cursor="hand2", highlightthickness=0,
                    relief="solid", command=save)
add_button.grid(column=1,row=4,columnspan=2)

my_passwords_button = Button(text="My Passwords", width=44, border=1, cursor="hand2", highlightthickness=0,
                      relief="solid",command=show_passwords)
my_passwords_button.grid(column=1,row=5,columnspan=2)
window.mainloop()
