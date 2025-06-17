import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Chef's Choice", layout="wide")

# Style CSS custom pour design haut de gamme
st.markdown("""
    <style>
    body { background-color: #fcf9f2; }
    .title-section { font-size: 44px; font-weight: 800; margin-bottom: 0; color: #2e2e2e; }
    .subtitle-section { font-size: 20px; margin-top: 0; color: #4d4d4d; }
    .centered { display: flex; justify-content: center; text-align: center; }
    .card { border-radius: 12px; padding: 20px; background-color: white; box-shadow: 0px 2px 15px rgba(0,0,0,0.1); }
    .menu-block { border-radius: 20px; overflow: hidden; position: relative; text-align: center; color: white; font-weight: bold; font-size: 24px; }
    .menu-block img { width: 100%; height: 320px; object-fit: cover; }
    .menu-block div { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
    </style>
""", unsafe_allow_html=True)

# Header navigation
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
        <div style='font-weight: bold; font-size: 24px;'>Chef'sChoice</div>
        <div>
            <input type='text' placeholder='Trouver la recette qui vous fait envie ..' style='padding: 5px 10px; border-radius: 5px; border: 1px solid #ddd;'>
            <a style='margin-left: 20px;' href='#'>Accueil</a>
            <a style='margin-left: 10px;' href='#'>Menu</a>
            <a style='margin-left: 10px;' href='#'>Recettes</a>
            <a style='margin-left: 10px;' href='#'>♥</a>
            <a style='margin-left: 10px;' href='#'>👤</a>
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Section d’accueil
col1, col2 = st.columns([1.1, 1.9])

with col1:
    st.image("https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=700&q=80")

with col2:
    st.markdown("""
        <p class="title-section">DES RECETTES <br> QUE POUR VOUS</p>
        <p class="subtitle-section">Rendez-vous sur l'application mobile 📱</p>
    """, unsafe_allow_html=True)

# Section profil utilisateur
st.markdown("### 👤 Créer votre profil")
col1, col2 = st.columns(2)

with col1:
    nom = st.text_input("Nom complet", "Omar Moudni")
    email = st.text_input("Email", "omar@email.com")
    mdp = st.text_input("Mot de passe", type="password")

with col2:
    st.image("https://images.unsplash.com/photo-1562967916-eb82221dfb36", width=320)

if st.button("Suivant"):
    st.success(f"Bonjour {nom} 👋")

# Section Menu Catégories
st.markdown("""
    <h2 style='text-align: center;'>AU MENU</h2>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='menu-block'>
            <img src='https://images.unsplash.com/photo-1605475122014-7c55a04630a6' />
            <div>Plats gourmets</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='menu-block'>
            <img src='https://images.unsplash.com/photo-1603052877564-5bbf9b9442b5' />
            <div>Salades</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='menu-block'>
            <img src='https://images.unsplash.com/photo-1599785209798-cd3c3bd09d9c' />
            <div>Desserts</div>
        </div>
    """, unsafe_allow_html=True)

# Section Recettes proposées
st.markdown("""
    <h2 style='text-align: center;'>Cela peut vous intéresser..</h2>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1604908554044-7d00548ef5a5")
    st.caption("Cabillaud rôti au four ♡")

with col2:
    st.image("https://images.unsplash.com/photo-1606491956689-2b9c0e6611e4")
    st.caption("Tajine de boulettes de viande hachée ♡")

with col3:
    st.image("https://images.unsplash.com/photo-1613145998971-6d8a74c5d017")
    st.caption("Saumon grillé ♡")
