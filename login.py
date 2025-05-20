from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import subprocess

conn = sqlite3.connect("utilisateurs.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

app = Tk()
app.title("K&C Restaurant - Login")
app.geometry("450x500")
app.configure(bg="#f9f8f4")

frame = Frame(app, bg="#f9f8f4")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

logo_img = Image.open("2.png")
logo_img = logo_img.resize((250, 150))
logo_tk = ImageTk.PhotoImage(logo_img)

def page_connexion():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, image=logo_tk, bg="#f9f8f4").grid(row=0, column=0, columnspan=2, pady=10)
    Label(frame, text="Bienvenue chez K&C Restaurant", font=("Helvetica", 20, "bold"),
          bg="#f9f8f4", fg="#5a4033").grid(row=1, column=0, columnspan=2, pady=(0, 20))

    Label(frame, text="Email:", font=("Helvetica", 12), bg="#f9f8f4").grid(row=2, column=0, padx=15, pady=10, sticky='e')
    entry_mail = Entry(frame, font=("Helvetica", 12), width=25)
    entry_mail.grid(row=2, column=1, padx=10, pady=10)

    Label(frame, text="Password", font=("Helvetica", 12), bg="#f9f8f4").grid(row=3, column=0, padx=15, pady=10, sticky='e')
    entry_mdp = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    entry_mdp.grid(row=3, column=1, padx=10, pady=10)

    def se_connecter():
        email = entry_mail.get()
        motdepasse = entry_mdp.get()
        if not email or not motdepasse :
         messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
         return
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (email, motdepasse))
        if c.fetchone():
            messagebox.showinfo("Succès", "Connexion réussie!")
            app.destroy()
            subprocess.run(["python", "interface.py"])  
        else:
            messagebox.showerror("Erreur", "Login ou mot de passe incorrect")

    Button(frame, text="Se connecter", font=("Helvetica", 11, "bold"),
           bg="#d79e63", fg="white", activebackground="#c88745",
           width=20, bd=0, cursor="hand2", command=se_connecter).grid(row=4, column=0, columnspan=2, pady=10)

    Button(frame, text="Créer un compte", font=("Helvetica", 11, "bold"),
           bg="#d79e63", fg="white", activebackground="#c88745",
           width=20, bd=0, cursor="hand2", command=lambda: to_signup()).grid(row=5, column=0, columnspan=2, pady=5)

def to_signup():
    app.destroy()
    subprocess.run(["python", "signup.py"])

page_connexion()
app.mainloop()
