import tkinter as tk
from tkinter import Tk, Label

window = tk.Tk()

window.title("Movie recommendation system")
window.geometry("500x500")
window.configure(background="lightblue")

#Page title
title_var = tk.StringVar()
title_var.set("Find A Recommended Movie​")
titlelabel = tk.Label(window,
                 textvariable=title_var,
                 anchor=tk.CENTER,
                 bg="darkblue",
                 height=2,
                 width=30,
                 bd=3,
                 font=("Arial", 16, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                 wraplength=2500
                )
titlelabel.pack(pady=20)

#Genre Label
label_genre = Label(window, text="Genre *",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
label_genre.pack(pady=10, padx=10, anchor="w")

#Director Label
name_var = tk.StringVar()

def submit():
    name = name_var.get()


    print("The Directors name is : " + name)
    name_var.set("")

name_label = tk.Label(window, text='Director', font=('Arial', 16, 'bold'))
name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))

name_label.pack(pady=10, padx=10, anchor="w")
name_entry.pack(pady=10, padx=10, anchor="w")




#Year Label
label_Year = Label(window, text="Release Year",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
label_Year.pack(pady=10, padx=10, anchor="w")

#Language Label
label_Language = Label(window, text="Language",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
label_Language.pack(pady=10, padx=10, anchor="w")

#Required Label
label_required = Label(window, text="* Indicates a required field",
                    anchor="w",
                    font=("Arial", 8, "bold"),
                    bg="lightblue",
                    fg="black")
label_required.pack(pady=5, padx=5, anchor="w")

#Search Button
def button_clicked():
    print("Button clicked!")


button = tk.Button(window,
                   text="Search",
                   command=button_clicked,
                   activebackground="darkgrey",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="darkblue",
                   cursor="hand2",
                   fg="white",
                   font=("Arial", 12, "bold"),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="left",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

window.resizable(0,0)

window.mainloop()
