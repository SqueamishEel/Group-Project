import tkinter as tk
from tkinter import Label, messagebox, Listbox
from MovieRecommendations import top_filtered_movies, apply_filters, recommend_from_history, get_history
from Rating import Open_Recommendation_Window

window = tk.Tk()
window.title("Movie recommendation system")
window.geometry("500x675")
window.configure(background="lightblue")
window.resizable(0, 0)

title_var = tk.StringVar()
title_var.set("Find A Recommended Movie")
titlelabel = tk.Label(
    window,
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

user_var = tk.StringVar(value="UserA")
Label(window, text="User ID *",
      anchor="w",
      font=("Arial", 16, "bold"),
      bg="lightblue",
      fg="black").pack(pady=10, padx=10, anchor="w")
tk.Entry(window, textvariable=user_var, font=("Arial", 10, "normal")).pack(pady=1, padx=10, anchor="w")

genre_var = tk.StringVar()
label_genre = Label(window, text="Genre *",
                    anchor="w",
                    font=("Arial", 16, "bold"),
                    bg="lightblue",
                    fg="black")
genre_entry = tk.Entry(window, textvariable=genre_var, font=("Arial", 10, "normal"))
label_genre.pack(pady=10, padx=10, anchor="w")
genre_entry.pack(pady=1, padx=10, anchor="w")

name_var = tk.StringVar()
name_label = tk.Label(window, text="Director",
                      font=("Arial", 16, "bold"),
                      bg="lightblue",
                      fg="black")
name_entry = tk.Entry(window, textvariable=name_var, font=("Arial", 10, "normal"))
name_label.pack(pady=10, padx=10, anchor="w")
name_entry.pack(pady=1, padx=10, anchor="w")

year_var = tk.StringVar()
year_label = tk.Label(window, text="Release Year",
                      font=("Arial", 16, "bold"),
                      bg="lightblue",
                      fg="black")
year_entry = tk.Entry(window, textvariable=year_var, font=("Arial", 10, "normal"))
year_label.pack(pady=10, padx=10, anchor="w")
year_entry.pack(pady=1, padx=10, anchor="w")

language_label= tk.Label(window, text="Language",
font =( "Arial", 16, "bold"),
bg ="lightblue",
fg="black", )
language_label.pack(pady=10, padx=10, anchor="w")
language_listbox= tk.Listbox(window,height=5, exportselection=False)

languages_list= ["Afrikaans","Arabic","Chinese (Simplified)","Chinese (Traditional)","Czech","Danish","English","Farsi","French","German","Greek"
           ,"Hebrew","Hindi","Hungarian","Indonesian","Icelandic","Italian","Japanese","Korean","Kyrgyz","Norsk Bokmal","Netherlands"
           ,"Norwegian","Polish","Pashto","Portuguese","Romainian","Russian","Slovenian","Spanish","Swedish","Tamil","Telugu","Thai"
           ,"Turkish","Vietnamese","No Spoken Language"]

for lang in languages_list:
    language_listbox.insert(tk.END, lang)
    language_listbox.pack(pady=1, padx=10, anchor="w")

label_required = Label(window, text="* Indicates a required field",
                       anchor="w",
                       font=("Arial", 8, "bold"),
                       bg="lightblue",
                       fg="black")
label_required.pack(pady=5, padx=5, anchor="w")


def Open_Confirm_Popup(user_id, genre, director, year, chosen_language, mode):
    popup = tk.Toplevel(window)
    popup.title("Confirm")
    popup.geometry("300x300")
    popup.configure(background="lightblue")
    popup.resizable(0, 0)

    Label(popup, text="Is this correct?",
          anchor="w",
          font=("Arial", 12, "bold"),
          bg="lightblue",
          fg="black").pack(pady=5, padx=5, anchor="n")

    Label(popup, text="Genre: " + genre,
          anchor="n",
          font=("Arial", 10, "bold"),
          bg="lightblue",
          fg="black").pack(pady=5, padx=5, anchor="n")

    Label(popup, text="Director: " + director,
          anchor="n",
          font=("Arial", 10, "bold"),
          bg="lightblue",
          fg="black").pack(pady=5, padx=5, anchor="n")

    Label(popup, text="Release Year: " + year,
          anchor="n",
          font=("Arial", 10, "bold"),
          bg="lightblue",
          fg="black").pack(pady=5, padx=5, anchor="n")

    Label(popup, text="Language: " + chosen_language,
          anchor="n",
          font=("Arial", 10, "bold"),
          bg="lightblue",
          fg="black").pack(pady=5, padx=5, anchor="n")
    
    if chosen_language == "Chinese (Simplified)":
        language = "CN"
    elif chosen_language == "Chinese (Traditional)":
        language = "ZH"
    elif chosen_language == "Czech":
        language = "CS"
    elif chosen_language == "German":
        language = "DE"
    elif chosen_language == "Greek":
        language = "EL"
    elif chosen_language == "Spanish":
        language = "ES"
    elif chosen_language == "Icelandic":
        language = "IS"
    elif chosen_language == "Norsk Bokmal":
        language = "NB"
    elif chosen_language == "Polish":
        language = "PL"
    elif chosen_language == "Pashto":
        language = "PS"
    elif chosen_language == "Portuguese":
        language = "PT"
    elif chosen_language == "Swedish":
        language = "SV"
    elif chosen_language == "Turkish":
        language = "TR"
    elif chosen_language == "No Spoken Language":
        language = "XX"
    else:
        chosen_language = chosen_language.upper()
        language = chosen_language[:2]

    def Submit_Yes():
        popup.destroy()

        if mode == "search":
            recs = top_filtered_movies(genre, director, year, language, n=20)
        else:
            filtered = apply_filters(genre, director, year, language)
            try:
                recs = recommend_from_history(user_id, filtered, n=20, min_rating=4)
            except Exception as e:
                messagebox.showerror("Cannot recommend", str(e))
                return

        Open_Recommendation_Window(window, user_id, recs)

    def Submit_No():
        popup.destroy()

    yes_button = tk.Button(
        popup,
        text="Yes",
        command=Submit_Yes,
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
        highlightthickness=1,
        justify="left",
        overrelief="raised",
        padx=5,
        pady=5,
        width=5,
        wraplength=100
    )
    yes_button.pack(pady=5, padx=5, anchor="n")

    no_button = tk.Button(
        popup,
        text="No",
        command=Submit_No,
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
        highlightthickness=1,
        justify="left",
        overrelief="raised",
        padx=5,
        pady=5,
        width=5,
        wraplength=100
    )
    no_button.pack(pady=5, padx=5, anchor="n")


def Submit_Form(mode="search"):
    user_id = user_var.get().strip()
    genre = genre_var.get().strip()
    director = name_var.get().strip()
    year = year_var.get().strip()
    
    selection = language_listbox.curselection()
    if selection:
        language = language_listbox.get(selection[0])
    else:
        language = ""

    if  not user_id:
        messagebox.showerror("No User ID entered", "User ID cannot be empty.")
        return

    if mode == "search" and not genre:
        messagebox.showerror("The genre is empty", "The genre cannot be empty")
        return

    if mode == "similar":
        h = get_history(user_id)
        total_rated = len(h)
        liked = len(h[h["rating"] >= 4])

        if total_rated < 3:
            messagebox.showerror(
                "Not enough ratings",
                "Please rate at least 3 movies before using Recommend Similar."
            )
            return

        if liked < 2:
            messagebox.showerror(
                "Not enough liked movies",
                "Please rate at least 2 movies as 4 or 5 stars before using Recommend Similar."
            )
            return

    Open_Confirm_Popup(user_id, genre, director, year, language, mode)


button = tk.Button(
    window,
    text="Search Movies",
    command=lambda: Submit_Form("search"),
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
    padx=5,
    pady=5,
    width=28,
    wraplength=200
)
button.pack(padx=5, pady=5)

button2 = tk.Button(
    window,
    text="Recommend Similar\n     (From Ratings)",
    command=lambda: Submit_Form("similar"),
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
    padx=5,
    pady=5,
    width=28,
    wraplength=200
)
button2.pack(padx=5, pady=5)

window.mainloop()
