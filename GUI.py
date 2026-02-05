import tkinter as tk
from tkinter import Tk, Label
import tkinter.messagebox
from easygui import *

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
genre_var = tk.StringVar()
label_genre = Label(window, text="Genre *",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
genre_entry = tk.Entry(window, textvariable=genre_var, font=('Arial', 10, 'normal'))
label_genre.pack(pady=10, padx=10, anchor="w")
genre_entry.pack(pady=1, padx=10, anchor="w")

#Director Label
name_var = tk.StringVar()
name_label = tk.Label(window, text='Director', 
                      font=('Arial', 16, 'bold'),
                      bg="lightblue",
                      fg="black")
name_entry = tk.Entry(window, textvariable=name_var, font=('Arial', 10, 'normal'))
name_label.pack(pady=10, padx=10, anchor="w")
name_entry.pack(pady=1, padx=10, anchor="w")

#Year Label
year_var = tk.StringVar()
year_label = tk.Label(window, text='Release Year', 
                      font=('Arial', 16, 'bold'),
                      bg="lightblue",
                      fg="black")
year_entry = tk.Entry(window, textvariable=year_var, font=('Arial', 10, 'normal'))
year_label.pack(pady=10, padx=10, anchor="w")
year_entry.pack(pady=1, padx=10, anchor="w")

#Langauge Label
language_var = tk.StringVar()
language_label = tk.Label(window, text='Language', 
                      font=('Arial', 16, 'bold'),
                      bg="lightblue",
                      fg="black")
language_entry = tk.Entry(window, textvariable=language_var, font=('Arial', 10, 'normal'))
language_label.pack(pady=10, padx=10, anchor="w")
language_entry.pack(pady=1, padx=10, anchor="w")

#Required Label
label_required = Label(window, text="* Indicates a required field",
                    anchor="w",
                    font=("Arial", 8, "bold"),
                    bg="lightblue",
                    fg="black")
label_required.pack(pady=5, padx=5, anchor="w")

#Search Button function
def Submit_Form():
    genre = genre_var.get()
    print("The Genre is : " + genre)
    genre_var.set("")
    name = name_var.get()
    print("The Directors name is : " + name)
    name_var.set("")
    year = year_var.get()
    print("The Release Year is : " + year)
    year_var.set("")
    langauge = language_var.get()
    print("The Langauge name is : " + langauge)
    language_var.set("")
    
    #popup
    message = "Is this correct? \n Genre: ", genre ,"\n Director: ", name, "\n Release Year: ", year ,"\n Director: ", langauge
    title = "Confirm"
    ynbox(message, title)

#search button label
button = tk.Button(window,
                   text="Search",
                   command=Submit_Form,
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
