import streamlit as st
import base64
from PIL import Image
import io

image = Image.open('laTete.JPG')
image = image.rotate(-90, expand=True)
new_width = 300
new_height = 400
image = image.resize((new_width, new_height))

# Convertir l'image en base64
image_bytes = io.BytesIO()
image.save(image_bytes, format="PNG")
image_base64 = base64.b64encode(image_bytes.getvalue()).decode()



NAME = "VONIN--KABEL YVENLEE"
st.title(NAME)

st.header('Bachelor 2 à :orange[Paris Ynov Campus]',divider='rainbow')
#création de variables pour les colonnes comme pour les div html
col1, col2 = st.columns(2)
col1.header(':handshake: SoftSkills :handshake:')
col1.write(
    """
- :white_check_mark: MOTIVATION SANS FAILLE
- :white_check_mark: GESTION DU STRESS
- :white_check_mark: TRAVAIL EN GROUPE
- :white_check_mark: CAPACITE D'ADAPTATION
- :white_check_mark: OPTIMISME
- :white_check_mark: SENS DU CHALLENGE

"""
)
col2.header(':white_check_mark: HardSkills :white_check_mark:')
col2.write(
    """
- :large_blue_square: :large_yellow_square: Python 
- :hotsprings: Java 
- HTML/CSS | JavaScript | SQL (SQLite)
- :globe_with_meridians: Excel | CiscoPacketTracer | Canvas
- Linux

""")
st.divider()
#inclusion d'un code html pour la bordure de la photo
st.markdown(
    f'<div style="display: flex; border: 2px solid #ccc; border-radius: 10px; padding: 10px;">'
    f'<img src="data:image/png;base64,{image_base64}" style="flex: 1; border-radius: 10px;">'
    f'<div style="flex: 1; padding-left: 10px;">'
    f'<p>Acquis Etudiant :</p>'
    f'<p>-Hangman/Hangman Web-(Golang&HTML|CSS)</p>'
    f'<p>-Forum---------------(Golang&HTML|CSS)</p>'
    f'<p>-Groupie-Tracker--------------(Golang)</p>'
    f'<p>-Emulateur Chip-8-------------(Golang)</p>'
    f'<p>-PacMan-------------------(JavaScript)</p>'
    f'<p>-DB de site E-commerce----(SQL&Python)</p>'
    f'<p><span style="color: #FF5733;">-------------------Un peu plus sur moi!--------------------</span></p>'
    f'<p>Patissier du dimanche / Tente de coder un jeu vidéo / Joueur de jeux vidéos / Chanteur / Sportif / Fan de musique </p>'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

st.divider()

st.header('Experience Professionelle', divider='orange')
st.write('Stage de 3eme en entreprise: :sparkle: BNP Paribas (Opera)')
st.write(
    """
- Methode efficace pour prendre des notes à l'aide de schemas
- Découverte de leur pôle communication et RH
""")
st.write('Preparation Militaire de Decouverte :helicopter::flag-fr:1RHC (Phalsbourg)')
st.write(
    """
- Discipline, Ponctualité, "Etre à l'heure c'est déjà être en retard"
- Dépassement de soi
- Découverte des nombreux métiers dont la mécanique et la météorologie
- Tir à munitions inertes au FAMAS
""")