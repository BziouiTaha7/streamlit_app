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
        st.subheader("Graphique en Barres")
        st.bar_chart(df.iloc[:, 0:2])

    if st.button("Graphique Linéaire"):
        st.subheader("Graphique Linéaire")
        st.line_chart(df.iloc[:, 0:2])

    if st.button("Graphique Circulaire"):
        st.subheader("Graphique Circulaire")
        fig, ax = plt.subplots()
        df.iloc[:, 1].plot(kind="pie", labels=df.iloc[:, 0], autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)
