import tkinter as tk
from pathlib import Path

def get_data_dir():
    return Path.home() / "missions"

def init_arborescence():
    data_dir = get_data_dir()
    (data_dir / "profil").mkdir(parents=True, exist_ok=True)
    (data_dir / "missions").mkdir(parents=True, exist_ok=True)
    return True

def pageProfil(container, profil, on_retour=None):
    """
    Affiche la page Profil avec bouton retour vers missions
    Args:
        container: Conteneur Tkinter
        profil: Dictionnaire du profil ou None
        on_retour: Fonction de callback pour retourner à missions
    """
    for widget in container.winfo_children():
        widget.destroy()

    # Titre
    tk.Label(container, text="Profil", font=("Arial", 24)).pack(pady=20)

    # Frame pour le contenu
    content_frame = tk.Frame(container)
    content_frame.pack(fill="x", padx=20, pady=10)

    if profil is None:
        label_info = tk.Label(
            content_frame,
            text="Aucun profil détecté. Cliquez pour initialiser.",
            wraplength=400,
            bg="white"
        )
        label_info.pack(pady=10)

        def on_init_click():
            init_arborescence()
            for widget in content_frame.winfo_children():
                widget.destroy()
            tk.Label(
                content_frame,
                text="✅ Arborescence créée dans ~/missions/",
                fg="green"
            ).pack(pady=10)

        tk.Button(
            content_frame,
            text="Initialiser le profil",
            command=on_init_click,
            font=("Arial", 16)
        ).pack(pady=10)
    else:
        tk.Label(
            content_frame,
            text="✅ Profil correctement initialisé",
            fg="green"
        ).pack(pady=10)

    # Bouton Retour vers missions (toujours affiché)
    if on_retour:
        tk.Button(
            container,
            text="← Retour aux missions",
            command=on_retour,
            font=("Arial", 12)
        ).pack(pady=20)
