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
st.set_page_config(page_title="Chef's Choice", layout="centered")
st.title("🍽️ Chef’s Choice")
st.subheader("Des recettes que pour vous 🍲")
st.write("Entrez vos ingrédients pour recevoir les meilleures suggestions de recettes.")

ingredients = st.text_input("🧺 Ingrédients (ex: poulet, citron, ail)")

if st.button("🔍 Trouver des recettes"):
    if not ingredients.strip():
        st.warning("Veuillez saisir des ingrédients.")
    else:
        resultats = recommander_recette(ingredients)
        st.success("Voici les recettes recommandées :")
        st.dataframe(resultats.reset_index(drop=True))
