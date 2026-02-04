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

label_genre = Label(window, text="Genre",
                    anchor="w",
                    font=("Arial", 16, "bold"),       
                    bg="lightblue",   
                    fg="black")
label_genre.pack(pady=10, padx=10, anchor="w")

label_Actor = Label(window, text="Actor",
                    anchor="w",
                    font=("Arial", 16, "bold"),       
                    bg="lightblue",   
                    fg="black")
label_Actor.pack(pady=10, padx=10, anchor="w")

label_Director = Label(window, text="Director",
                       anchor="w",
                       font=("Arial", 16, "bold"),       
                       bg="lightblue",   
                       fg="black")
label_Director.pack(pady=10, padx=10, anchor="w")

def button_clicked():
    print("Button clicked!")

# Creating a button with specified options
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

window.mainloop()
