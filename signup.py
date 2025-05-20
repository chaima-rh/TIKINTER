from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import subprocess
import re
conn = sqlite3.connect("utilisateurs.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

app = Tk()
app.title("K&C Restaurant - Signup")
app.geometry("450x500")
app.configure(bg="#f9f8f4")

frame = Frame(app, bg="#f9f8f4")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

logo_img = Image.open("2.png")
logo_img = logo_img.resize((250, 150))
logo_tk = ImageTk.PhotoImage(logo_img)


def email_valide(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(pattern, email)

def page_inscription():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, image=logo_tk, bg="#f9f8f4").grid(row=0, column=0, columnspan=2, pady=10)
    Label(frame, text="Bienvenue chez K&C Restaurant", font=("Helvetica", 20, "bold"),
          bg="#f9f8f4", fg="#5a4033").grid(row=1, column=0, columnspan=2, pady=(0, 20))
    Label(frame, text="Créer un compte", font=("Helvetica", 20, "bold"),
          bg="#f9f8f4", fg="#5a4033").grid(row=2, column=0, columnspan=2, pady=(0, 20))

  
    Label(frame, text="Email:", font=("Helvetica", 12), bg="#f9f8f4").grid(row=3, column=0, padx=15, pady=10, sticky='e')
    entry_mail = Entry(frame, font=("serif", 12), width=25)
    entry_mail.grid(row=3, column=1, padx=10, pady=10)

    Label(frame, text="Password", font=("Helvetica", 12), bg="#f9f8f4").grid(row=4, column=0, padx=15, pady=10, sticky='e')
    entry_mdp = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    entry_mdp.grid(row=4, column=1, padx=10, pady=10)
    
    Label(frame, text="Confirmer password", font=("Helvetica", 12), bg="#f9f8f4").grid(row=5, column=0, padx=15, pady=10, sticky='e')
    entry_mdp_c = Entry(frame, font=("Helvetica", 12), show="*", width=25)
    entry_mdp_c.grid(row=5, column=1, padx=10, pady=10)

    def creer_compte():
        
      nom = entry_mail.get()
      motdepasse = entry_mdp.get()
      motdepasse_conf = entry_mdp_c.get() 
      
      if not nom or not motdepasse or not motdepasse_conf:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
        return
      if not email_valide(entry_mail.get()):
            messagebox.showerror("Erreur", "Adresse e-mail invalide")
            return

      if motdepasse != motdepasse_conf:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
        return

      try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (nom, motdepasse))
        conn.commit()
        messagebox.showinfo("Succès", "Compte créé avec succès")
        to_login()
      except:
        messagebox.showerror("Erreur", "Ce compte existe déjà ou une erreur est survenue")

    Button(frame, text="Créer un compte", font=("Helvetica", 11, "bold"),
           bg="#d79e63", fg="white", activebackground="#c88745",
           width=20, bd=0, cursor="hand2", command=creer_compte).grid(row=6, column=0, columnspan=2, pady=10)

    Button(frame, text="Retour à la connexion", font=("Helvetica", 11, "bold"),
           bg="#d79e63", fg="white", activebackground="#c88745",
           width=20, bd=0, cursor="hand2", command=to_login).grid(row=7, column=0, columnspan=2, pady=5)

def to_login():
    app.destroy()
    subprocess.run(["python", "login.py"])

page_inscription()
app.mainloop()
