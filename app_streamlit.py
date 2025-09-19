import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualization App")

# Charger les données
file = st.file_uploader("Charger un fichier CSV ou Excel", type=["csv", "xlsx"])

if file:
    if file.name.endswith(".csv"):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)

    st.subheader(" Aperçu des données")
    st.dataframe(data)

    # Choix des colonnes pour X et Y
    cols = list(data.columns)
    x_col = st.selectbox("Axe X", options=[""] + cols, index=0)
    y_col = st.selectbox("Axe Y", options=[""] + cols, index=0)

    # Boutons pour afficher les graphiques
    if st.button("Graphique en Barres"):
        if x_col and y_col:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(data[x_col], data[y_col])
            ax.set_title(f"{y_col} par {x_col}")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            plt.xticks(rotation=45, ha="right", fontsize=9)
            st.pyplot(fig)
        else:
            st.warning(" Veuillez choisir une colonne X et une colonne Y.")

    if st.button("Graphique Linéaire"):
        if x_col and y_col:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data[x_col], data[y_col], marker="o")
            ax.set_title(f"{y_col} en fonction de {x_col}")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            plt.xticks(rotation=45, ha="right", fontsize=9)
            st.pyplot(fig)
        else:
            st.warning(" Veuillez choisir une colonne X et une colonne Y.")

    if st.button("Graphique Circulaire"):
        if x_col and y_col:
            if pd.api.types.is_numeric_dtype(data[y_col]):
                grouped_data = data.groupby(x_col)[y_col].sum()
                fig, ax = plt.subplots()
                wedges, texts, autotexts = ax.pie(
                    grouped_data,
                    autopct="%1.1f%%",
                    startangle=90
                )
                ax.legend(
                    wedges,
                    grouped_data.index,
                    title=x_col,
                    loc="upper left",
                    bbox_to_anchor=(1, 1),
                )
                ax.set_title(f"Répartition de {y_col} par {x_col}")
                fig.subplots_adjust(right=0.8)
                st.pyplot(fig)
            else:
                st.error(f" La colonne '{y_col}' doit être numérique pour un graphique circulaire.")

    if st.button("Graphique total"):
        if x_col and y_col:
            if not pd.api.types.is_numeric_dtype(data[y_col]):
                st.error(f" La colonne '{y_col}' doit être numérique.")
            else:
                color_col = "Filière" if "Filière" in data.columns else None
                fig, ax = plt.subplots(figsize=(12, 6))
                
                if color_col:
                    categories = data[color_col].unique()
                    colors = plt.cm.tab20.colors
                    color_dict = {cat: colors[i % len(colors)] for i, cat in enumerate(categories)}
                    bar_colors = [color_dict[val] for val in data[color_col]]
                else:
                    bar_colors = "skyblue"

                x_positions = range(len(data))
                ax.bar(x_positions, data[y_col], color=bar_colors)
                ax.set_xticks(x_positions)
                ax.set_xticklabels(data[x_col], rotation=45, ha="right", fontsize=9)

                if color_col:
                    handles = [plt.Line2D([0], [0], color=color_dict[c], lw=4) for c in categories]
                    ax.legend(handles, categories, title=color_col, loc="upper right")

                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"{y_col} par {x_col}")
                st.pyplot(fig)
        else:
            st.warning(" Veuillez choisir une colonne X et une colonne Y.")
