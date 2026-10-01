import tkinter as tk
import webbrowser

def initialiserIndexDistant(index): 
    return 

def pageMissions(container, profil, liste_missions, index_missions, on_profil=None):
    """
    Affiche la page Missions avec bouton vers profil
    Args:
        container: Conteneur Tkinter
        profil: Dictionnaire du profil
        liste_missions: Liste des missions
        index_missions: Index actuel
        on_profil: Fonction de callback pour aller à profil
    """
    global url_entry, bouton_precedent, bouton_suivant

    for widget in container.winfo_children():
        widget.destroy()

    # Titre
    tk.Label(container, text="Missions", font=("Arial", 24)).pack(pady=20)

    # Si liste_missions est vide, afficher un message
    if not liste_missions:
        tk.Label(
            container,
            text="Aucune mission disponible",
            font=("Arial", 14),
            fg="gray"
        ).pack(pady=40)

        # Bouton vers profil
        if on_profil:
            tk.Button(
                container,
                text="Aller au profil",
                command=on_profil,
                font=("Arial", 12)
            ).pack(pady=20)
        return

    # Frame de navigation
    navigation_frame = tk.Frame(container)
    navigation_frame.pack(fill="x", padx=20, pady=20)

    # Label pour les infos
    label_info = tk.Label(
        container,
        text="",
        font=("Arial", 10),
        wraplength=400,
        bg="white"
    )
    label_info.pack(pady=10)

    # Fonctions de navigation
    def afficher_lien():
        mission = liste_missions[index_missions]
        url_entry.delete(0, tk.END)
        url_entry.insert(0, mission["lien"])
        print(f"Lien actuel : {mission['lien']}")

        liste_couleur = {"commentaire": "orange", "jaime": "blue", "test": "white", None: "black"}
        couleur = liste_couleur.get(mission.get("action", mission.get("ation")), "red")
        container.config(bg=couleur)

        label_info.config(text=mission.get("info", ""))

        if mission["lien"]:
            webbrowser.open(mission["lien"], new=0, autoraise=True)

        if index_missions == 0:
            bouton_precedent.grid_remove()
        else:
            bouton_precedent.grid()

        if index_missions == len(liste_missions) - 1:
            bouton_suivant.grid_remove()
        else:
            bouton_suivant.grid()

    def precedent():
        global index_missions
        if index_missions > 0:
            index_missions -= 1
            print("clique précédent")
            afficher_lien()

    def suivant():
        global index_missions
        if index_missions < len(liste_missions) - 1:
            index_missions += 1
            print("clique suivant")
            afficher_lien()

    # Boutons Précédent et Suivant
    bouton_precedent = tk.Button(
        navigation_frame,
        text="←",
        command=precedent,
        font=("Arial", 16),
        width=3
    )
    bouton_precedent.grid(row=0, column=0, padx=5, pady=10, sticky="ns")

    url_entry = tk.Entry(navigation_frame, font=("Arial", 11))
    url_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

    bouton_suivant = tk.Button(
        navigation_frame,
        text="→",
        command=suivant,
        font=("Arial", 16),
        width=3
    )
    bouton_suivant.grid(row=0, column=2, padx=5, pady=10, sticky="ns")

    navigation_frame.grid_columnconfigure(1, weight=1)

    afficher_lien()

    # Bouton vers profil
    if on_profil:
        tk.Button(
            container,
            text="Aller au profil",
            command=on_profil,
            font=("Arial", 12)
        ).pack(pady=20)
