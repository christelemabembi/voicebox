import streamlit as st
import torch
import torchaudio

st.title("🎙️ Voicebox sur Render")
st.write("Bienvenue ! Cette app déployée sur Render utilise Voicebox en mode Streamlit.")

# Vérification des versions installées
st.write("Torch version:", torch.__version__)
st.write("Torchaudio version:", torchaudio.__version__)

# Exemple simple : champ texte
texte = st.text_input("Entrez du texte à transformer en voix :")

if st.button("Générer la voix"):
    if texte.strip() == "":
        st.error("Veuillez entrer un texte.")
    else:
        st.success(f"Simulation : génération de voix pour → {texte}")
        # Ici tu pourras brancher le vrai code Voicebox
