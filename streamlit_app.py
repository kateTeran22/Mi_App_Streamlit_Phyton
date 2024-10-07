import streamlit as st

import pandas as pd
import plotly.express as px


def pagina_principal():
    st.title("Pagina Principal")
    st.write("Bienvenido a la aplicación de demostración")
    st.write("Usa el menú de la izquierda para navegar entre las paginas")

def visualizar_datos():
    st.title("Visualización de Datos")
    st.write("Carga un archivo de excel para visualizar los datos")
    archivo_cargado = st.file_uploader("Elige un archivo excel", type="xlsx")

    if archivo_cargado is not None:
        df = pd.ExcelFile(archivo_cargado, engine='openpyxl')
        hojasA = df.sheet_names
        hoja_seleccionadaA = st.selectbox("Selecciona una hoja", hojasA)

        # Cargar los datos de la hoja seleccionada
        df = pd.read_excel(archivo_cargado, sheet_name=hoja_seleccionadaA)

        if df.empty:
            st.write("La hoja seleccionada está vacía o no tiene datos.")
        else:
         st.write("Datos del archivo excel: ")
         st.write(df)
         st.write("Estadisticas descriptivas: ")
         st.write(df.describe())

def graficos_interactivos():
    st.title("Gráficos Interactivos")
    st.write("Carga un archivo excel para crear gráficos interactivos.")
    archivo_cargado = st.file_uploader("Elige un archivo excel", type="xlsx",key="2")
    if archivo_cargado is not None:
        df = pd.ExcelFile(archivo_cargado,engine='openpyxl')
        # Mostrar lista de hojas disponibles en el archivo
        hojas = df.sheet_names
        hoja_seleccionada = st.selectbox("Selecciona una hoja", hojas)

        # Cargar los datos de la hoja seleccionada
        df = pd.read_excel(archivo_cargado, hoja_seleccionada, engine='openpyxl')

        if df.empty:
            st.write("La hoja seleccionada está vacía o no tiene datos.")
        else:
            # Mostrar las primeras filas del dataframe para ver los encabezados
            st.write("Datos de la hoja seleccionada:")
            st.write(df.head())

        st.write("Elige una columna para el eje X: ")
        eje_x = st.selectbox("Eje x", df.columns)
        st.write("Elige una columna para el eje Y: ")
        eje_y = st.selectbox("Eje Y", df.columns)

        if st.button("Crear Gráfico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)




st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Seleccione una pagina",["Página principal", "Visualización de Datos","Gráficos interactivos"])

if pagina=="Página principal":
    pagina_principal()
elif pagina=="Visualización de Datos":
    visualizar_datos()
elif pagina=="Gráficos interactivos":
    graficos_interactivos()