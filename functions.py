import csv
import os
from tkinter import messagebox
from tkinter import SEL_FIRST, SEL_LAST


def ajouter_reservation(data, affichage, effacer):
    if data['nom'] and data['telephone']:
        with open("reservations.csv", "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                data['nom'], data['telephone'], data['personnes'],
                data['date'], data['heure'], data['paiement'], data['evenement']
            ])
        affichage.insert("end", f" Réservation ajoutée pour {data['nom']}\n")
        effacer()
    else:
        messagebox.showerror("Erreur", "Veuillez remplir les champs")

def afficher_reservations(affichage):
    affichage.delete(1.0, "end")
    if os.path.exists("reservations.csv"):
        with open("reservations.csv", "r", encoding='utf-8') as f:
            for ligne in csv.reader(f):
                affichage.insert("end", f"{' | '.join(ligne)}\n")
    else:
        affichage.insert("end", " Aucun fichier trouvé.\n")

def rechercher_reservation(telephone, affichage):
    affichage.delete(1.0, "end")
    if os.path.exists("reservations.csv"):
        trouve = False
        with open("reservations.csv", "r", encoding='utf-8') as f:
            for ligne in csv.reader(f):
                if telephone.lower() in ligne[1].lower():
                    affichage.insert("end", f"{' | '.join(ligne)}\n")
                    trouve = True
        if not trouve:
                messagebox.showerror("Erreur", "Aucun résultat trouvé")

    else:
        affichage.insert("end", " Aucun fichier trouvé.\n")

def supprimer_reservation(affichage, effacer):
    """Supprime la réservation sélectionnée dans la zone d'affichage"""
    if not os.path.exists("reservations.csv"):
        affichage.insert("end", " Aucun fichier trouvé.\n")
        return

    # Récupérer la sélection
    try:
        selection = affichage.get(SEL_FIRST, SEL_LAST).strip()
        telephone = selection.split("|")[1].strip()  # On suppose que le téléphone est le 2ème élément
    except:
        messagebox.showerror("Erreur", "Aucune réservation sélectionnée")
        return

    # Lire et filtrer les réservations
    with open("reservations.csv", "r", encoding='utf-8') as f:
        reservations = list(csv.reader(f))

    nouvelles_reservations = [res for res in reservations if res[1].strip() != telephone]

    # Sauvegarder les modifications
    with open("reservations.csv", "w", newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(nouvelles_reservations)

    # Feedback
    affichage.insert("end", f"✅ Réservation pour {telephone} supprimée.\n")
    effacer()
    afficher_reservations(affichage)  # Rafraîchir l'affichage 