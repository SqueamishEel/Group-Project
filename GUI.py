from tkinter import *
window = Tk()

window.title("Movie recommendation system")
window.geometry("500x500")
window.configure(background="black")
tk.Label(text="genre").pack()
tk.Label(text="actors").pack()
tk.Label(text="director").pack()
tk.Label(text="Rating").pack()
tk.Label(text="Release Date").pack()

window.mainloop()
