import tkinter as tk
from tkinter import Label, messagebox

from easygui import *

window = tk.Tk()

window.title("Movie recommendation system")
window.geometry("500x500")
window.configure(background="lightblue")

# Page title
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

# Genre Label
genre_var = tk.StringVar()
label_genre = Label(window, text="Genre *",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
genre_entry = tk.Entry(window, textvariable=genre_var, font=('Arial', 10, 'normal'))
label_genre.pack(pady=10, padx=10, anchor="w")
genre_entry.pack(pady=1, padx=10, anchor="w")

# Director Label
name_var = tk.StringVar()
name_label = tk.Label(window, text='Director',
                      font=('Arial', 16, 'bold'),
                      bg="lightblue",
                      fg="black")
name_entry = tk.Entry(window, textvariable=name_var, font=('Arial', 10, 'normal'))
name_label.pack(pady=10, padx=10, anchor="w")
name_entry.pack(pady=1, padx=10, anchor="w")

# Year Label
year_var = tk.StringVar()
year_label = tk.Label(window, text='Release Year',
                      font=('Arial', 16, 'bold'),
                      bg="lightblue",
                      fg="black")
year_entry = tk.Entry(window, textvariable=year_var, font=('Arial', 10, 'normal'))
year_label.pack(pady=10, padx=10, anchor="w")
year_entry.pack(pady=1, padx=10, anchor="w")

# Langauge Label
language_var = tk.StringVar()
language_label = tk.Label(window, text='Language',
                          font=('Arial', 16, 'bold'),
                          bg="lightblue",
                          fg="black")
language_entry = tk.Entry(window, textvariable=language_var, font=('Arial', 10, 'normal'))
language_label.pack(pady=10, padx=10, anchor="w")
language_entry.pack(pady=1, padx=10, anchor="w")

# Required Label
label_required = Label(window, text="* Indicates a required field",
                       anchor="w",
                       font=("Arial", 8, "bold"),
                       bg="lightblue",
                       fg="black")
label_required.pack(pady=5, padx=5, anchor="w")


# Search Button function
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

    if not genre:
        messagebox.showerror("The genre is empty", "The genre cannot be empty")

    elif genre:
        # popup
        message = "Is this correct? \n Genre: ", genre, "\n Director: ", name, "\n Release Year: ", year, "\n Director: ", langauge
        title = "Confirm"
        output = ynbox(message, title)
        if output:

            # recommendation window
            recommendation_window = tk.Tk()
            recommendation_window.title("Movie recommendation system - Recommendations")
            recommendation_window.geometry("500x500")
            recommendation_window.configure(background="lightblue")
            recommendation_window.columnconfigure(0, weight=1)
            recommendation_window.columnconfigure(1, weight=8)
            recommendation_window.columnconfigure(2, weight=1)
            recommendation_window.rowconfigure(0, weight=9)
            recommendation_window.rowconfigure(1, weight=1)
            recommendation_window.resizable(0, 0)

            # left arrow button
            left_arrow_img = tk.PhotoImage(master=recommendation_window, file="Images/Left Arrow.png")
            left_arrow = tk.Button(recommendation_window,
                                   image=left_arrow_img,
                                   activebackground="lightblue",
                                   relief="flat",
                                   cursor="hand2",
                                   bg='lightblue')
            left_arrow.grid(row=0, column=0)

            # middle section
            recommendation_mid_section = tk.Frame(recommendation_window,
                                                  borderwidth=2,
                                                  bg='lightblue')
            recommendation_mid_section.grid(row=0, column=1)

            # right arrow button
            right_arrow_img = tk.PhotoImage(master=recommendation_window, file="Images/Right Arrow.png")
            right_arrow = tk.Button(recommendation_window,
                                    image=right_arrow_img,
                                    activebackground="lightblue",
                                    relief="flat",
                                    cursor="hand2",
                                    bg='lightblue')
            right_arrow.grid(row=0, column=2)

            # white section
            white_section = tk.Frame(recommendation_mid_section,
                                     padx=10,
                                     pady=10,
                                     bg="white")
            white_section.grid(row=0, column=0)

            # recommended movie attributes
            recommended_movie_title = "Avatar"
            recommended_movie_genre = "Action Adventure"
            recommended_movie_director = "James Cameron"
            recommended_movie_release_year = "2009"
            recommended_movie_language = "English"
            recommended_movie_rating = "7.2"
            recommended_movie_runtime = "162 Minutes"
            recommended_movie_description = "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization."
            recommended_movie_number = 1

            # movie title
            recommended_movie_title_lbl = tk.Label(white_section,
                                                   text=recommended_movie_title,
                                                   font=("Arial", 24, "bold"),
                                                   bg='white')
            recommended_movie_title_lbl.grid(row=0, column=0, columnspan=2, sticky=(tk.W))

            # movie genre
            recommended_movie_genre_lbl = tk.Label(white_section,
                                                   text="Genre:",
                                                   font=("Arial", 10, "normal"),
                                                   bg='white')
            recommended_movie_genre_lbl.grid(row=1, column=0, sticky=(tk.W))
            recommended_movie_genre_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_genre_entry.insert(0, recommended_movie_genre)
            recommended_movie_genre_entry.grid(row=1, column=1)

            # movie director
            recommended_movie_director_lbl = tk.Label(white_section,
                                                      text="Director:",
                                                      font=("Arial", 10, "normal"),
                                                      bg='white')
            recommended_movie_director_lbl.grid(row=2, column=0, sticky=(tk.W))
            recommended_movie_director_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_director_entry.insert(0, recommended_movie_director)
            recommended_movie_director_entry.grid(row=2, column=1)

            # movie release year
            recommended_movie_release_year_lbl = tk.Label(white_section,
                                                          text="Release Year:",
                                                          font=("Arial", 10, "normal"),
                                                          bg='white')
            recommended_movie_release_year_lbl.grid(row=3, column=0, sticky=(tk.W))
            recommended_movie_release_year_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_release_year_entry.insert(0, recommended_movie_release_year)
            recommended_movie_release_year_entry.grid(row=3, column=1)

            # movie language
            recommended_movie_language_lbl = tk.Label(white_section,
                                                      text="Language:",
                                                      font=("Arial", 10, "normal"),
                                                      bg='white')
            recommended_movie_language_lbl.grid(row=4, column=0, sticky=(tk.W))
            recommended_movie_language_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_language_entry.insert(0, recommended_movie_language)
            recommended_movie_language_entry.grid(row=4, column=1)

            # movie rating
            recommended_movie_rating_lbl = tk.Label(white_section,
                                                    text="Rating:",
                                                    font=("Arial", 10, "normal"),
                                                    bg='white')
            recommended_movie_rating_lbl.grid(row=5, column=0, sticky=(tk.W))
            recommended_movie_rating_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_rating_entry.insert(0, recommended_movie_rating)
            recommended_movie_rating_entry.grid(row=5, column=1)

            # movie runtime
            recommended_movie_runtime_lbl = tk.Label(white_section,
                                                     text="Runtime:",
                                                     font=("Arial", 10, "normal"),
                                                     bg='white')
            recommended_movie_runtime_lbl.grid(row=6, column=0, sticky=(tk.W))
            recommended_movie_runtime_entry = tk.Entry(white_section, font=('Arial', 10, 'normal'))
            recommended_movie_runtime_entry.insert(0, recommended_movie_runtime)
            recommended_movie_runtime_entry.grid(row=6, column=1)

            # movie description
            recommended_movie_description_lbl = tk.Label(white_section,
                                                         text="Description:",
                                                         font=("Arial", 10, "normal"),
                                                         bg='white')
            recommended_movie_description_lbl.grid(row=7, column=0, sticky=(tk.W))
            recommended_movie_description_tb = tk.Text(white_section,
                                                       width=40,
                                                       height=5,
                                                       font=('Arial', 10, 'normal'))
            recommended_movie_description_tb.insert("1.0", recommended_movie_description)
            recommended_movie_description_tb.grid(row=8, column=0, columnspan=2, sticky=(tk.W))

            # select button
            select_button = tk.Button(white_section,
                                      text="Select",
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
            select_button.grid(row=9, column=0, columnspan=3)

            # recommended movie counter label.
            recommendation_counter = tk.Label(recommendation_mid_section,
                                              text=str(recommended_movie_number) + " out of 10",
                                              font=("Arial", 8, "bold"),
                                              bg='lightblue')
            recommendation_counter.grid(row=1, column=0, sticky=(tk.S))

            recommendation_window.mainloop()


# search button label
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

window.resizable(0, 0)

window.mainloop()
