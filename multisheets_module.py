import streamlit as st
import gspread
import pandas as pd
import json
from oauth2client.service_account import ServiceAccountCredentials

# Autenticación con gspread usando secrets de Streamlit
def authenticate_gspread():
    service_account_info = json.loads(st.secrets["SERVICE_ACCOUNT_JSON"])
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, scope)
    client = gspread.authorize(creds)
    return client

# Obtener datos de una hoja de cálculo de Google Sheets
def obtener_datos_sheet(sheet_url):
    try:
        client = authenticate_gspread()
        sheet = client.open_by_url(sheet_url)
        worksheet = sheet.sheet1
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Error al obtener datos de la sheet: {e}")
        return pd.DataFrame()

# Interfaz en Streamlit
def mostrar_upgrades_multisheets():
    st.title("📋 Gestión de Upgrades por Equipos")
    st.write("Agregá los links de los Google Sheets que contienen los upgrades de cada equipo.")

    sheet_links = st.text_area("Pegá aquí los links (uno por línea):", height=200)

    if st.button("Cargar Datos de Google Sheets"):
        urls = sheet_links.strip().split("\n")
        for url in urls:
            if url:
                st.subheader(f"Datos de: {url}")
                df = obtener_datos_sheet(url)
                if not df.empty:
                    st.dataframe(df)
                else:
                    st.warning("No se encontraron datos en esta hoja.")
