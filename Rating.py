import tkinter as tk
from tkinter import Label, messagebox
from Movierecommendations import save_rating, year_only

# Rating gui pop up
def Rating_Popup(parent, movie_row, user_id):
    popup = tk.Toplevel(parent)
    popup.title("Rate Movie")
    popup.geometry("320x190")
    popup.configure(background="lightblue")
    popup.resizable(0, 0)

    label_title = tk.Label(
        popup,
        text=movie_row["original_title"],
        font=("Arial", 15, "bold"),
        bg="lightblue",
        wraplength=280
    )
    label_title.pack(pady=10)

    rating_value = {"v": 0}
    stars = []

    # Helps so you can rate multiple films
    def Refresh_Stars():
        for i, b in enumerate(stars, start=1):
            b.config(text="★" if i <= rating_value["v"] else "☆")

    def Set_Rating(v):
        rating_value["v"] = v
        Refresh_Stars()

    row = tk.Frame(popup, bg="lightblue")
    row.pack(pady=6)

    for i in range(1, 6):
        b = tk.Button(
            row,
            text="☆",
            font=("Arial", 24),
            bd=0,
            bg="lightblue",
            activebackground="lightblue",
            command=lambda v=i: Set_Rating(v)
        )
        b.pack(side="left", padx=2)
        stars.append(b)

    Refresh_Stars()
    # this is the submit function for rating
    def Submit_Rating():
        if rating_value["v"] == 0:
            messagebox.showerror("Missing rating", "Pick 1 to 5 stars.")
            return

        save_rating(user_id, int(movie_row["id"]), rating_value["v"])
        messagebox.showinfo("Saved", f"Saved {rating_value['v']} star(s) for:\n{movie_row['original_title']}")
        popup.destroy()

    submit_button = tk.Button(
        popup,
        text="Submit Rating",
        command=Submit_Rating,
        bg="darkblue",
        fg="white",
        font=("Arial", 11, "bold"),
        bd=3,
        cursor="hand2",
        padx=10,
        pady=5
    )
    submit_button.pack(pady=12)


def Open_Recommendation_Window(parent, user_id, recs_df):
    if recs_df.empty:
        messagebox.showerror("No results", "No Movies Found with these filters.")
        return

    recs_df = recs_df.reset_index(drop=True)

    global recommended_movie_number
    global recommended_movie_count
    recommended_movie_number = 1
    recommended_movie_count = len(recs_df)
   ## Shows the description of the film recommended
    def Load_Recommendation():
        global recommended_movie_number
        recommended_movie_index = recommended_movie_number - 1
        row = recs_df.iloc[recommended_movie_index]

        recommended_movie_title_lbl.configure(text=str(row["original_title"]))

        recommended_movie_genre_entry.delete(0, "end")
        recommended_movie_genre_entry.insert(0, str(row["genres"]))

        recommended_movie_director_entry.delete(0, "end")
        recommended_movie_director_entry.insert(0, str(row["director"]))

        recommended_movie_release_year_entry.delete(0, "end")
        recommended_movie_release_year_entry.insert(0, year_only(str(row["release_date"])))

        recommended_movie_language_entry.delete(0, "end")
        recommended_movie_language_entry.insert(0, str(row["original_language"]))

        recommended_movie_rating_entry.delete(0, "end")
        recommended_movie_rating_entry.insert(0, str(row["vote_average"]))

        recommended_movie_runtime_entry.delete(0, "end")
        recommended_movie_runtime_entry.insert(0, f"{int(row['runtime'])} Minutes")

        recommended_movie_description_tb.delete("1.0", "end")
        recommended_movie_description_tb.insert("1.0", str(row["overview"]).strip() or "(No overview available.)")

        recommendation_counter.configure(text=f"{recommended_movie_number} out of {recommended_movie_count}")

    def Load_Previous_Recommendation():
        global recommended_movie_number
        if recommended_movie_number > 1:
            recommended_movie_number -= 1
            Load_Recommendation()

    def Load_Next_Recommendation():
        global recommended_movie_number
        global recommended_movie_count
        if recommended_movie_number < recommended_movie_count:
            recommended_movie_number += 1
            Load_Recommendation()

    def Rate_Current_Movie():
        row = recs_df.iloc[recommended_movie_number - 1]
        Rating_Popup(recommendation_window, row, user_id)
     ## recommendation GUI
    recommendation_window = tk.Toplevel(parent)
    recommendation_window.title("Movie recommendation system - Recommendations")
    recommendation_window.geometry("500x500")
    recommendation_window.configure(background="lightblue")
    recommendation_window.columnconfigure(0, weight=1)
    recommendation_window.columnconfigure(1, weight=8)
    recommendation_window.columnconfigure(2, weight=1)
    recommendation_window.rowconfigure(0, weight=9)
    recommendation_window.rowconfigure(1, weight=1)
    ## Arrows to change the movie
    left_arrow = tk.Button(
        recommendation_window,
        command=Load_Previous_Recommendation,
        text="◀",
        activebackground="lightblue",
        relief="flat",
        cursor="hand2",
        bg="lightblue",
        font=("Arial", 18, "bold")
    )
    left_arrow.grid(row=0, column=0)

    recommendation_mid_section = tk.Frame(
        recommendation_window,
        borderwidth=2,
        bg="lightblue"
    )
    recommendation_mid_section.grid(row=0, column=1)

    right_arrow = tk.Button(
        recommendation_window,
        command=Load_Next_Recommendation,
        text="▶",
        activebackground="lightblue",
        relief="flat",
        cursor="hand2",
        bg="lightblue",
        font=("Arial", 18, "bold")
    )
    right_arrow.grid(row=0, column=2)

    white_section = tk.Frame(
        recommendation_mid_section,
        padx=10,
        pady=10,
        bg="white"
    )
    white_section.grid(row=0, column=0)

    recommended_movie_title_lbl = tk.Label(
        white_section,
        text="",
        font=("Arial", 24, "bold"),
        bg="white",
        wraplength=300
    )
    recommended_movie_title_lbl.grid(row=0, column=0, columnspan=2, sticky=(tk.W), pady=10)

    recommended_movie_genre_lbl = tk.Label(
        white_section,
        text="Genre:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_genre_lbl.grid(row=1, column=0, sticky=(tk.W))
    recommended_movie_genre_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_genre_entry.grid(row=1, column=1)

    recommended_movie_director_lbl = tk.Label(
        white_section,
        text="Director:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_director_lbl.grid(row=2, column=0, sticky=(tk.W))
    recommended_movie_director_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_director_entry.grid(row=2, column=1)

    recommended_movie_release_year_lbl = tk.Label(
        white_section,
        text="Release Year:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_release_year_lbl.grid(row=3, column=0, sticky=(tk.W))
    recommended_movie_release_year_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_release_year_entry.grid(row=3, column=1)

    recommended_movie_language_lbl = tk.Label(
        white_section,
        text="Language:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_language_lbl.grid(row=4, column=0, sticky=(tk.W))
    recommended_movie_language_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_language_entry.grid(row=4, column=1)

    recommended_movie_rating_lbl = tk.Label(
        white_section,
        text="Rating:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_rating_lbl.grid(row=5, column=0, sticky=(tk.W))
    recommended_movie_rating_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_rating_entry.grid(row=5, column=1)

    recommended_movie_runtime_lbl = tk.Label(
        white_section,
        text="Runtime:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_runtime_lbl.grid(row=6, column=0, sticky=(tk.W))
    recommended_movie_runtime_entry = tk.Entry(white_section, font=("Arial", 10, "normal"))
    recommended_movie_runtime_entry.grid(row=6, column=1)

    recommended_movie_description_lbl = tk.Label(
        white_section,
        text="Description:",
        font=("Arial", 10, "normal"),
        bg="white"
    )
    recommended_movie_description_lbl.grid(row=7, column=0, sticky=(tk.W))
    recommended_movie_description_tb = tk.Text(
        white_section,
        width=40,
        height=5,
        font=("Arial", 10, "normal")
    )
    recommended_movie_description_tb.grid(row=8, column=0, columnspan=2, sticky=(tk.W))

    recommendation_counter = tk.Label(
        recommendation_mid_section,
        text="",
        font=("Arial", 8, "bold"),
        bg="lightblue"
    )
    recommendation_counter.grid(row=1, column=0, sticky=(tk.S))

    select_button = tk.Button(
        white_section,
        text="Rate Movie",
        command=Rate_Current_Movie,
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
        wraplength=100
    )
    select_button.grid(row=9, column=0, columnspan=3)

    recommendation_window.resizable(0, 0)
    Load_Recommendation()
