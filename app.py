import streamlit as st

# Configuration générale
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
