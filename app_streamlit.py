import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualization App")

file = st.file_uploader("Charger un fichier CSV ou Excel", type=["csv", "xlsx"])

if file:
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("Aperçu des données")
    st.dataframe(df)

    if st.button("Graphique en Barres"):
        st.subheader("Âge des étudiants (Graphique en Barres)")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(df["Nom"], df["Âge"])
        ax.set_xlabel("Nom")
        ax.set_ylabel("Âge")
        ax.set_title("Âge des étudiants")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    if st.button("Graphique Linéaire"):
        st.subheader("Âge des étudiants (Graphique Linéaire)")
        fig, ax = plt.subplots(figsize=(10, 5))
        df_sorted = df.sort_values(by="Âge")  # trier par âge pour plus de lisibilité
        ax.plot(df_sorted["Nom"], df_sorted["Âge"], marker="o")
        ax.set_xlabel("Nom")
        ax.set_ylabel("Âge")
        ax.set_title("Âge des étudiants (ordonnés)")
        plt.xticks(rotation=90)
        st.pyplot(fig)

    if st.button("Graphique Circulaire"):
        st.subheader("Répartition des Filières (Graphique Circulaire)")
        fig, ax = plt.subplots()
        df["Filière"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title("Répartition des Filières")
        st.pyplot(fig)
