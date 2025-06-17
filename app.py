import streamlit as st

# Configuration de la page
st.set_page_config(page_title="SaveurMagique", layout="wide")

# ---------- Barre de navigation ----------
st.markdown("""
    <style>
        .topnav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 15px 30px;
            font-family: 'Segoe UI', sans-serif;
            font-size: 17px;
        }
        .topnav .left, .topnav .right {
            display: flex;
            align-items: center;
            gap: 25px;
        }
        .topnav a {
            text-decoration: none;
            color: black;
            font-weight: 500;
        }
        .search-box input {
            padding: 7px 15px;
            border-radius: 20px;
            border: 1px solid #ccc;
            font-size: 15px;
        }
    </style>
    <div class="topnav">
        <div class="left">
            <img src="https://via.placeholder.com/100x40?text=SaveurMagique" alt="logo">
            <a href="#">Accueil</a>
            <a href="#">Menu</a>
            <a href="#">Recettes</a>
            <a href="#">Nous contacter</a>
        </div>
        <div class="right">
            <div class="search-box"><input type="text" placeholder="Trouver la recette qui vous fait envie..."></div>
            <a href="#">Se connecter</a> | <a href="#">S'inscrire</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------- Section image + texte ----------
col1, col2 = st.columns([1, 1.3])

with col1:
    st.image("https://raw.githubusercontent.com/OmarMoudni/chefs-choice-app/main/assets/saveur_header.png", use_column_width=True)

with col2:
    st.markdown(
        """
        <div style='margin-top:100px;'>
            <h1 style='font-size:52px; color:#2F2F2F; font-weight:800;'>DES RECETTES<br>QUE POUR VOUS</h1>
            <p style='color:#444; font-size:16px; margin-top:15px;'>RENDEZ-VOUS SUR L’APPLICATION MOBILE 📱</p>
        </div>
        """,
        unsafe_allow_html=True
    )
