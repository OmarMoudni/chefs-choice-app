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
            padding: 5px 12px;
            border-radius: 20px;
            border: 1px solid #ccc;
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
            <div class="se
