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

window.mainloop()
