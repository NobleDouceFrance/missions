import tkinter as tk
from pages import profil, missions
from donnees import local,distant 

# Variables globales
INDEX_DISTANT=None
INDEX_LOCAL=None 
PROFIL = None
LISTE_MISSIONS = []  # Peut être vide
INDEX_MISSIONS = 0

def showProfil():
    """Affiche la page profil"""
    profil.pageProfil(container, PROFIL, on_retour=showMissions)

def showMissions():
    """Affiche la page missions"""
    
    missions.pageMissions(container, PROFIL, LISTE_MISSIONS, INDEX_MISSIONS, on_profil=showProfil)

# Création de la fenêtre
root = tk.Tk()
root.geometry("800x600")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Affiche la page missions par défaut

def main(): 
    PROFIL=local.chargerProfil()
    if PROFIL: showMissions()
    else: showProfil()
    return 

main()

root.mainloop()
