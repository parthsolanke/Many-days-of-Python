import json
import random
import tkinter as tk
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p',
           'q', 'r', 's', 't',
           'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_dict = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Make sure to fill each field.")
    else:
        try:
            with open(r"Password-Manager\data\data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(r"Password-Manager\data\data.json", "w") as file:
                # saving updated data in json file
                json.dump(json_dict, file, indent=4)
        else:
            # updating old data with new data
            data.update(json_dict)
            
            with open(r"Password-Manager\data\data.json", "w") as file:
                # saving updated data in json file
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

def find_password():
        
    website = website_entry.get()
    
    try:
        with open(r"Password-Manager\data\data.json", "r") as file:
            # reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}"
                                f"\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, padx=2, pady=2)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=2, pady=2)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, padx=2, pady=2)

# entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
email_entry.insert(0, "DummyEmail@gmail.com")

password_entry = tk.Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2, padx=2, pady=2)

# buttons
generate_button = tk.Button(text="Generate", width=10, command=generate_password)
generate_button.grid(row=4, column=0, padx=2, pady=2)
generate_button.config(bd=0, bg="#ADD8E6")

add_button = tk.Button(text="Add", width=10, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
add_button.config(bd=0, bg="#ADD8E6")

search_button = tk.Button(text="Search", width=30, command=find_password)
search_button.grid(row=0, column=1, columnspan=3, padx=2, pady=2)
search_button.config(bd=0, bg="#ADD8E6")

window.mainloop()
