from tkinter import *
from PIL import Image, ImageTk
from functions import ajouter_reservation, afficher_reservations, rechercher_reservation, supprimer_reservation


app = Tk()
app.title("K & C - Réservations ")
app.geometry("900x800")
app.minsize(900, 700)
app.configure(bg="#FDF6F0")  


logo = Image.open("2.png")
logo = logo.resize((350, 150), Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(logo)

logo_label = Label(app, image=logo_img, bg="#FDF6F0")
logo_label.pack(pady=5)


card = Frame(app, bg="#FFFBF7", bd=0, highlightthickness=1, highlightbackground="#E0C3A0")
card.pack(pady=5, padx=30, fill="both", expand=False)

label_style = {"bg": "#FFFBF7", "fg": "#A67C00", "font": ("Helvetica", 10, "bold")}
entry_style = {"bg": "#FAFAFA", "fg": "#333", "insertbackground": "#A67C00", "relief":RIDGE, "bd": 1, "highlightthickness": 0}


Label(card, text="Nom du client:", **label_style).grid(row=0, column=0, padx=10, pady=6, sticky="e")
entry_c = Entry(card, width=40, **entry_style)
entry_c.grid(row=0, column=1, padx=10, pady=6)

Label(card, text="Téléphone:", **label_style).grid(row=1, column=0, padx=10, pady=6, sticky="e")
entry_num = Entry(card, width=40, **entry_style)
entry_num.grid(row=1, column=1, padx=10, pady=6)

Label(card, text="Nombre de personnes:", **label_style).grid(row=2, column=0, padx=10, pady=6, sticky="e")
entry_p = Entry(card, width=40, **entry_style)
entry_p.grid(row=2, column=1, padx=10, pady=6)

Label(card, text="Date:", **label_style).grid(row=3, column=0, padx=10, pady=6, sticky="e")
entry_d = Entry(card, width=40, **entry_style)
entry_d.grid(row=3, column=1, padx=10, pady=6)

Label(card, text="Heure:", **label_style).grid(row=4, column=0, padx=10, pady=6, sticky="e")
entry_h = Entry(card, width=40, **entry_style)
entry_h.grid(row=4, column=1, padx=10, pady=6)

Label(card, text="Mode de paiement:", **label_style).grid(row=5, column=0, padx=10, pady=6, sticky="e")
choix_paiement = StringVar(value="Espèces(Cash)")
OptionMenu(card, choix_paiement, "Espèces(Cash)", "Carte", "Mobile").grid(row=5, column=1, padx=10, pady=6, sticky="w")

Label(card, text="Événement:", **label_style).grid(row=6, column=0, padx=10, pady=6, sticky="e")
choix_evenement = StringVar(value="Fête d'anniversaire")
OptionMenu(card, choix_evenement, "Fête d'anniversaire", "Dîner", "Soirée musicale").grid(row=6, column=1, padx=10, pady=6, sticky="w")


Label(app, text="Rechercher par telephone:", bg="#FDF6F0", fg="#A67C00", font=("Helvetica", 10, "bold")).pack()
recherche_entry = Entry(app, width=40, **entry_style, justify=RIGHT)
recherche_entry.pack(pady=4)

btn_rechercher = Button(app, text="Rechercher", bg="#EAC79D", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=10, pady=3)
btn_rechercher.pack(pady=4)


btn_frame = Frame(app, bg="#FDF6F0")
btn_frame.pack(pady=8)

btn_style = {"bg": "#EAC79D", "fg": "white", "font": ("Helvetica", 10, "bold"), "bd": 0, "padx": 10, "pady": 3}
def effacer_champs():
    entry_c.delete(0, END)
    entry_num.delete(0, END)
    entry_p.delete(0, END)
    entry_d.delete(0, END)
    entry_h.delete(0, END)
    recherche_entry.delete(0, END)

def bouton_ajouter():
    data = {
        'nom': entry_c.get(),
        'telephone': entry_num.get(),
        'personnes': entry_p.get(),
        'date': entry_d.get(),
        'heure': entry_h.get(),
        'paiement': choix_paiement.get(),
        'evenement': choix_evenement.get()
    }
    ajouter_reservation(data, affichage, effacer_champs)

def bouton_afficher():
    afficher_reservations(affichage)

def bouton_rechercher():
    telephone = recherche_entry.get()
    rechercher_reservation(telephone, affichage)

def bouton_supprimer():
    telephone= recherche_entry.get()
    supprimer_reservation( affichage, effacer_champs)

Button(btn_frame, text="Ajouter", command=bouton_ajouter, **btn_style).grid(row=0, column=0, padx=8)
Button(btn_frame, text="Afficher", command=bouton_afficher, **btn_style).grid(row=0, column=1, padx=8)
Button(btn_frame, text="Supprimer", command=bouton_supprimer, **btn_style).grid(row=0, column=2, padx=8)
Button(btn_frame, text="Effacer", command=effacer_champs, **btn_style).grid(row=0, column=3, padx=8)
btn_rechercher.config(command=bouton_rechercher)




zone_frame = LabelFrame(app, text="Zone d'Affichage", bg="white", fg="#A67C00", font=("Helvetica", 10, "bold"))
zone_frame.pack(padx=30, pady=10, fill="both", expand=False)

affichage = Text(zone_frame, height=8, bg="#FDF6F0", fg="#444", insertbackground="#A67C00", relief=FLAT)
affichage.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()
