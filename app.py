import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Données
data = {
    'name': [
        'Tajine de poulet au citron',
        'Pâtes au saumon',
        'Salade quinoa avocat',
        'Couscous aux légumes',
        'Pizza végétarienne'
    ],
    'ingredients': [
        'poulet citron olives oignon ail huile épices',
        'pâtes saumon crème fraîche citron aneth',
        'quinoa avocat tomate concombre citron huile',
        'semoule carotte courgette pois chiches navet épices',
        'pâte à pizza poivron champignon oignon mozzarella tomate'
    ]
}
df = pd.DataFrame(data)
df['ingredients'] = df['ingredients'].str.lower()

# Vectorisation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['ingredients'])

# Fonction de recommandation
def recommander_recette(ingredients_utilisateur):
    user_vec = vectorizer.transform([ingredients_utilisateur.lower()])
    sim_scores = cosine_similarity(user_vec, X).flatten()
    top_indices = sim_scores.argsort()[::-1][:3]
    return df.iloc[top_indices][['name', 'ingredients']]

# Interface
st.set_page_config(page_title="Chef's Choice", layout="wide")

# Style CSS
st.markdown(
    """
    <style>
    .big-title {
        font-size: 50px;
        font-weight: 800;
        color: #2e2e2e;
        padding-top: 50px;
    }
    .subtext {
        font-size: 16px;
        color: #666;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Image + texte en 2 colonnes
col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.image("https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=1200&q=80", use_column_width=True)

with col2:
    st.markdown('<div class="big-title">DES RECETTES<br>QUE POUR VOUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Rendez-vous sur l\'application mobile 📱</div>', unsafe_allow_html=True)

# Formulaire utilisateur
with st.form("profil_formulaire"):
    st.markdown("### 👤 Créez votre profil")
    
    col1, col2 = st.columns(2)
    sexe = col1.radio("Sexe", ["Femme", "Homme"])
    pays = col2.text_input("Pays d’origine")

    col3, col4 = st.columns(2)
    allergies = col3.multiselect(
        "Allergies et intolérances",
        ["Aucune", "Gluten", "Lactose", "Fruits à coque", "Œufs", "Poisson"]
    )

    regime = col4.selectbox(
        "Régime alimentaire",
        ["Aucun", "Végétarien", "Vegan", "Sans gluten", "Halal", "Casher"]
    )

    preferences = st.multiselect(
        "Préférences gastronomiques",
        ["Cuisine marocaine", "Cuisine italienne", "Cuisine asiatique", "Cuisine indienne", "Cuisine française"]
    )

    bouton_profil = st.form_submit_button("Suivant ➡️")

# Une fois que l’utilisateur a cliqué
if bouton_profil:
    st.success(f"Bonjour {sexe} de {pays} 👋")
    st.markdown("### 🧺 Entrez vos ingrédients")
    ingredients = st.text_input("Ingrédients (ex: poulet, citron, ail)")

    if st.button("🔍 Trouver des recettes"):
        if not ingredients.strip():
            st.warning("Veuillez saisir des ingrédients.")
        else:
            resultats = recommander_recette(ingredients)
            st.success("Voici les recettes recommandées :")
            st.dataframe(resultats.reset_index(drop=True))

        resultats = recommander_recette(ingredients)
        st.success("Voici les recettes recommandées :")
        st.dataframe(resultats.reset_index(drop=True))
