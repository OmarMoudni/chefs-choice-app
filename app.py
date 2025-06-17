col1, col2 = st.columns([1, 1.2])

with col1:
    st.image("https://raw.githubusercontent.com/OmarMoudni/chefs-choice-app/main/assets/saveur_header.png", use_column_width=True)

with col2:
    st.markdown("""
        <div style='margin-top:100px;'>
            <h1 style='font-size:50px; color:#2F2F2F;'>DES RECETTES<br>QUE POUR VOUS</h1>
            <p style='color:#666;'>RENDEZ-VOUS SUR L’APPLICATION MOBILE 📱</p>
        </div>
    """, unsafe_allow_html=True)
