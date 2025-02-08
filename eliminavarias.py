import streamlit as st
import pandas as pd

# Título de la app
st.title("Elimina columnas de un DataFrame")

# Subir archivo CSV
uploaded_file = st.file_uploader("Carga un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### DataFrame original:")
    st.dataframe(df)
    
    # Seleccionar múltiples columnas para eliminar
    columns_to_drop = st.multiselect("Selecciona las columnas a eliminar:", df.columns)
    
    if st.button("Eliminar columnas"):
        df = df.drop(columns=columns_to_drop)
        st.write("### DataFrame modificado:")
        st.dataframe(df)
else:
    st.write("Por favor, carga un archivo CSV.")
