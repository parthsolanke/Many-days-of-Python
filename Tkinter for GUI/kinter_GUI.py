import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Widgets")
window.minsize(width=500, height=500)

# Create a label
label = tk.Label(text="Old label", font=("Arial", 24, "bold"))
label.config(text="New text")
label.pack()

# Create a button
def action():
    print("button clicked")

button = tk.Button(text="Click Me", command=action)
button.pack()

# Create an entry
inp = tk.Entry(width=30)
inp.insert(tk.END, string="Some text to begin with.")
print(inp.get())
inp.pack()

# Create a textbox
text = tk.Text(height=5, width=30)
text.focus() # Puts cursor in textbox.
text.insert(tk.END, "loreum ipsum dolor sit amet, ut labore et dolore magna aliqua.")
print(text.get("1.0", tk.END)) # Get's current value in textbox at line 1, character 0s
text.pack()

# Create a spinbox
def spinbox_used():
    print(spinbox.get())
    
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Create a scale
def scale_used(value):
    print(value)
    
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Create a checkbutton
def checkbutton_used():
    print(checked_state.get())
    
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Create a radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Create a listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    
listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
