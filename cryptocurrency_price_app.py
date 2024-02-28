import streamlit as st
import pandas as pd

# Titre de l'application
st.markdown('''# **Application de Prix Binance**
Une application simple affichant les prix des cryptomonnaies en utilisant l'API de *Binance*.
''')

# En-tête pour les prix sélectionnés
st.header('**Prix Sélectionnés**')

# Charger les données du marché depuis l'API de Binance
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Fonction personnalisée pour arrondir les valeurs
# Fonction personnalisée pour arrondir les valeurs
def arrondir_valeur(valeur):
    if (valeur > 1).all():
        valeur_arrondie = valeur.round(2)
    else:
        valeur_arrondie = valeur.round(8)
    return valeur_arrondie


# Création de trois colonnes pour afficher les prix
col1, col2, col3 = st.columns(3)

# Sélection des cryptomonnaies dans la barre latérale
crypto_selection1 = st.sidebar.selectbox('Prix 1', df.symbol, list(df.symbol).index('BTCBUSD'))
crypto_selection2 = st.sidebar.selectbox('Prix 2', df.symbol, list(df.symbol).index('ETHBUSD'))
crypto_selection3 = st.sidebar.selectbox('Prix 3', df.symbol, list(df.symbol).index('BNBBUSD'))

# DataFrame des cryptomonnaies sélectionnées
crypto_df1 = df[df.symbol == crypto_selection1]
crypto_df2 = df[df.symbol == crypto_selection2]
crypto_df3 = df[df.symbol == crypto_selection3]

# Application de la fonction personnalisée pour arrondir les prix
crypto_prix1 = arrondir_valeur(crypto_df1.weightedAvgPrice)
crypto_prix2 = arrondir_valeur(crypto_df2.weightedAvgPrice)
crypto_prix3 = arrondir_valeur(crypto_df3.weightedAvgPrice)

# Sélection de la colonne priceChangePercent
crypto_variation1 = f'{float(crypto_df1.priceChangePercent)}%'
crypto_variation2 = f'{float(crypto_df2.priceChangePercent)}%'
crypto_variation3 = f'{float(crypto_df3.priceChangePercent)}%'

# Création de boîtes pour afficher les prix
col1.metric(crypto_selection1, crypto_prix1, crypto_variation1)
col2.metric(crypto_selection2, crypto_prix2, crypto_variation2)
col3.metric(crypto_selection3, crypto_prix3, crypto_variation3)

# En-tête pour afficher tous les prix
st.header('**Tous les Prix**')

# Affichage de l'ensemble des données
st.dataframe(df)

# Intégration des scripts Bootstrap pour le style
st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
