import os
import tkinter as tk
from tkinter import Label, messagebox
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# What needs doing is all the labels and all the input boxes apart from user id also need a search button and a recommend button
##need a required label for Genre as well, Title needs doing too
csv_path= "C:/Users/fitz_/Downloads/movies.csv"
user_history = "user_ratings.csv"

 # Data and model.
df = pd.read_csv(csv_path)[[
    "id", "genres", "original_title", "original_language", "release_date", "overview",
    "runtime", "vote_average", "director"
]].copy()

df["runtime"]= df["runtime"].replace(0, np.nan)
df["runtime"]= df["runtime"].fillna(df["runtime"].median())

for c in ["genres", "original_language", "original_title", "release_date","overview" , "director"]:
 df[c]= df[c].fillna("").astype(str)

df["Joined"] = (
    df["genres"] + " " +
    df["original_language"] + " " +
    df["original_title"] + " " +
    df["overview"] + " " +
    df["release_date"] + " " +
    df["director"]
).str.lower()

tfidf= TfidfVectorizer(stop_words="english")
X= tfidf.fit_transform(df["Joined"])
cosim= cosine_similarity(X,X)

id_to_idx=pd.Series(df.index, index=df["id"]).drop_duplicates()

def year_only(d):
    return d[:4] if isinstance(d, str) and len(d) >= 4 else ""

def apply_filters(genre, director, year, language):
    d = df.copy()

    g = genre.strip()
    if g:
        parts = [p.strip() for p in g.replace(",", " ").split() if p.strip()]
        for p in parts:
            d = d[d["genres"].str.contains(p, case=False, na=False, regex=False)]

    if director.strip():
        d = d[d["director"].str.contains(director.strip(), case=False, na=False, regex=False)]

    if year.strip():
        d = d[d["release_date"].str.contains(year.strip(), case=False, na=False, regex=False)]

    if language.strip():
        d = d[d["original_language"].str.contains(language.strip(), case=False, na=False, regex=False)]

    return d

def history(user_id):
    if not os.path.exists(user_history):
        return pd.DataFrame(columns=["user_id", "movie_id", "rating"])
    h= pd.read_csv(user_history)
    return h[h["user_id"] == user_id].copy()

def saving_rating(user_id, movie_id, rating):
    row = pd.DataFrame([{"user_id":user_id, "movie_id":int(movie_id), "rating":int(rating)}])
    if os.path.exists(user_history):
        h = pd.read_csv(user_history)
        h = h[~((h["user_id"] == user_id) & (h["movie_id"] == int(movie_id)))]
        h = pd.concat([h, row], ignore_index=True)
    else:
        h = row
    h.to_csv(user_history, index=False)

def recommendation(user_id, filtered_df , n=10, min_rating=4):
    h = history(user_id)
    liked = h[h["rating"]>= min_rating]
    if liked.empty:
        raise ValueError("Rate movies 4 or 5 first.")

    seed_idx= [int(id_to_idx[mid]) for mid in liked["movie_id"].tolist() if mid in id_to_idx.index]
    if not seed_idx:
        raise ValueError("Rated movies not found.")

    scores = cosim[seed_idx].sum(axis=0)

    rated_ids = set(h["movie_id"].tolist())
    cand = filtered_df[~filtered_df["id"].isin(rated_ids)]
    if cand.empty:
        raise ValueError("No movies left after removing rated ones (try different filters).")

    ranked = sorted(cand.index.tolist(), key=lambda i: scores[i], reverse=True)[:n]
    return df.loc[ranked].reset_index(drop=True)


def rating_popup(parent, title, on_submit):
    win = tk.Toplevel(parent)
    win.title("Rate Movie")
    win.geometry("320x190")
    win.configure(background="lightblue")
    win.resizable(0,0)

    tk.Label(win, text=title , font=("Arial", 15 ,"bold"), wraplength=280).pack(pady=10)

    rating = {"v":0}
    stars=[]

    def refresh():
        for i, b in enumerate(stars, start=1):
            b.config(text="★" if i <= rating["v"] else "☆")


    def set_v(v):
        rating["v"] = v
        refresh()


    row = tk.Frame(win, bg="lightblue")
    row.pack(pady=6)

    for i in range(1, 6):
        b = tk.Button(row, text="☆", font=("Arial", 24), bd=0,
                      bg="lightblue", activebackground="lightblue",
                      command=lambda v=i: set_v(v))
        b.pack(side="left", padx=2)
        stars.append(b)

    refresh()

    def submit():
        if rating["v"] == 0:
            messagebox.showerror("Missing rating", "Pick 1 to 5 stars.")
            return
        on_submit(rating["v"])
        win.destroy()

    tk.Button(win, text="Submit Rating", command=submit,
              bg="darkblue", fg="white", font=("Arial", 11, "bold"),
              bd=3, cursor="hand2", padx=10, pady=5).pack(pady=12)
 ## GUI

window = tk.Tk()

window.title("Movie recommendation system")
window.geometry("500x650")
window.configure(background="lightblue")
window.resizable(width=False, height=False)


user_var = tk.StringVar(value="UserA")
tk.Label(window, text="User ID", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10, padx=10, anchor="w")
tk.Entry(window, textvariable=user_var).pack(padx=10, anchor="w")

def open_recommendation_window(user_id, recs_df):
    if recs_df.empty:
        messagebox.showerror("no results", "No Movies Found with these filters.")
        return

    recs_df = recs_df.reset_index(drop=True)
    state = {"pos": 0, "count": len(recs_df)}

    w = tk.Toplevel(window)
    w.title("Movie recommendation system - Recommendations")
    w.geometry("500x500")
    w.configure(background="lightblue")
    w.resizable(False, False)
    w.columnconfigure(0, weight=1)
    w.columnconfigure(1, weight=8)
    w.columnconfigure(2, weight=1)
    w.rowconfigure(0, weight=9)
    w.rowconfigure(1, weight=1)


    def set_entry(ent, val):
        ent.delete(0, "end")
        ent.insert(0, val)

    def load_movie():
        r = recs_df.iloc[state["pos"]]
        movie_title_lbl.config(text=str(r["original_title"]))
        set_entry(ent_genre, str(r["genres"]))
        set_entry(ent_director, str(r["director"]))
        set_entry(ent_year, year_only(str(r["release_date"])))
        set_entry(ent_lang, str(r["original_language"]))
        set_entry(ent_vote, str(r["vote_average"]))
        set_entry(ent_runtime, f"{int(r['runtime'])} Minutes")

        txt_desc.delete("1.0", "end")
        ov = str(r["overview"]).strip()
        txt_desc.insert("1.0", ov if ov else "(No overview available.)")

        counter_lbl.config(text=f"{state['pos'] + 1} out of {state['count']}")

    def previous_movie():
        if state["pos"] > 0:
            state["pos"] -= 1
            load_movie()

    def next_movie():
        if state["pos"] < state["count"] - 1:
            state["pos"] += 1
            load_movie()

    def rate_movie():
        r = recs_df.iloc[state["pos"]]
        movie_id = int(r["id"])
        movie_title = str(r["original_title"])

        def submit(stars):
            saving_rating(user_id, movie_id, stars)
            messagebox.showinfo("Saved", f"Saved {stars} star(s) for:\n{movie_title}")

        rating_popup(w, movie_title, submit)

    left_btn = tk.Button(w, text="◀", command=previous_movie, bg="lightblue", relief="flat",
                         font=("Arial", 18, "bold"))
    left_btn.grid(row=0, column=0)

    mid = tk.Frame(w, bg="lightblue")
    mid.grid(row=0, column=1)

    right_btn = tk.Button(w, text="▶", command=next_movie, bg="lightblue", relief="flat",
                          font=("Arial", 18, "bold"))
    right_btn.grid(row=0, column=2)

         #Displays movie details
    white = tk.Frame(mid, bg="white", padx=10, pady=10)
    white.grid(row=0, column=0)

    # Movie title
    movie_title_lbl = tk.Label(white, text="", font=("Arial", 24, "bold"), bg="white", wraplength=300)
    movie_title_lbl.grid(row=0, column=0, columnspan=2, sticky="w", pady=10)

    white = tk.Frame(mid, bg="white", padx=10, pady=10)
    white.grid(row=0, column=0)

    movie_title_lbl = tk.Label(white, text="", font=("Arial", 24, "bold"), bg="white", wraplength=300)
    movie_title_lbl.grid(row=0, column=0, columnspan=2, sticky="w", pady=10)

    def row(label_text, r):
        tk.Label(white, text=label_text, font=("Arial", 10, "normal"), bg="white").grid(row=r, column=0, sticky="w")
        e = tk.Entry(white, font=("Arial", 10, "normal"))
        e.grid(row=r, column=1)
        return e

            #Movie details
    ent_genre = row("Genre:", 1)
    ent_director = row("Director:", 2)
    ent_year = row("Release Year:", 3)
    ent_lang = row("Language:", 4)
    ent_vote = row("Rating:", 5)
    ent_runtime = row("Runtime:", 6)

    tk.Label(white, text="Description:", font=("Arial", 10, "normal"), bg="white").grid(row=7, column=0, sticky="w")
    txt_desc = tk.Text(white, width=40, height=5, font=("Arial", 10, "normal"))
    txt_desc.grid(row=8, column=0, columnspan=2, sticky="w")

    counter_lbl = tk.Label(mid, text="", font=("Arial", 8, "bold"), bg="lightblue")
    counter_lbl.grid(row=1, column=0)

    tk.Button(white, text="Rate", command=rate_movie, bg="darkblue", fg="white",
    font=("Arial", 12, "bold"), bd=3, cursor="hand2", padx=10, pady=5, width=15).grid(row=9, column=0,
     columnspan=2,
    pady=(10, 0))
    load_movie()

def open_confirm_popup(user_id, genre, director, year, language, mode):
        popup = tk.Toplevel(window)
        popup.title("Confirm")
        popup.geometry("300x300")
        popup.configure(background="lightblue")
        popup.resizable(False, False)

        Label(popup, text="Is this correct?", font=("Arial", 12, "bold"), bg="lightblue", fg="black").pack(pady=8)
        Label(popup, text="Genre: " + genre, font=("Arial", 10, "bold"), bg="lightblue", fg="black").pack(pady=4)
        Label(popup, text="Director: " + director, font=("Arial", 10, "bold"), bg="lightblue", fg="black").pack(pady=4)
        Label(popup, text="Release Year: " + year, font=("Arial", 10, "bold"), bg="lightblue", fg="black").pack(pady=4)
        Label(popup, text="Language: " + language, font=("Arial", 10, "bold"), bg="lightblue", fg="black").pack(pady=4)

        def yes():
            popup.destroy()
            filtered = apply_filters(genre, director, year, language)

            if mode == "search":
                recs = filtered.sort_values("vote_average", ascending=False).head(20)
            else:
                try:
                    recs = recommendation(user_id, filtered, n=20, min_rating=4)
                except Exception as e:
                    messagebox.showerror("Cannot recommend", str(e))
                    return

            open_recommendation_window(user_id, recs)

        def no():
            popup.destroy()

        tk.Button(popup, text="Yes", command=yes, bg="darkblue", fg="white",
                  font=("Arial", 12, "bold"), bd=3, cursor="hand2", padx=10, pady=5, width=8).pack(pady=8)
        tk.Button(popup, text="No", command=no, bg="darkblue", fg="white",
                  font=("Arial", 12, "bold"), bd=3, cursor="hand2", padx=10, pady=5, width=8).pack(pady=4)


def Submit_Form(mode="search"):
    user_id = user_var.get().strip()
    genre = genre_var.get().strip()
    director = name_var.get().strip()
    year = year_var.get().strip()
    language = language_var.get().strip()

    if not user_id:
        messagebox.showerror("Missing", "User ID cannot be empty.")
        return
    if not genre:
        messagebox.showerror("Missing", "Genre is required.")
        return

    open_confirm_popup(user_id, genre, director, year, language, mode)


window.mainloop()