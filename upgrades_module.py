import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# Función para obtener upgrades desde Google Sheets
def obtener_upgrades():
    try:
        # Acceso al secret del JSON de la cuenta de servicio
        service_account_json = st.secrets["SERVICE_ACCOUNT_JSON"]

        # Definir el scope
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # Crear las credenciales usando el JSON (cuidado con la doble conversión de string a dict)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(eval(service_account_json), scope)

        # Autenticarse con gspread
        client = gspread.authorize(creds)

        # Abrir la hoja de cálculo
        sheet = client.open("Upgrades_Servers").sheet1

        # Obtener todos los registros
        records = sheet.get_all_records()

        # Convertir a DataFrame
        upgrades_df = pd.DataFrame(records)

        return upgrades_df

    except Exception as e:
        st.error(f"❌ Error obteniendo datos de Google Sheets: {e}")
        return pd.DataFrame()

# Función para enviar datos a Slack
def enviar_a_slack(df):
    try:
        slack_token = st.secrets["SLACK_BOT_TOKEN"]
        slack_channel = st.secrets["SLACK_CHANNEL"]

        # Formatear el mensaje con la info del DataFrame
        mensaje = "*Reporte de Upgrades de Servidores:*\n\n"
        for idx, row in df.iterrows():
            mensaje += f"🔧 *Servidor:* {row.get('Servidor', 'N/A')} | 🗓️ *Fecha Upgrade:* {row.get('Fecha Upgrade', 'N/A')} | 👤 *Responsable:* {row.get('Who upgrade', 'N/A')}\n"

        payload = {
            "channel": slack_channel,
            "text": mensaje
        }

        headers = {
            "Authorization": f"Bearer {slack_token}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://slack.com/api/chat.postMessage", json=payload, headers=headers)

        if response.status_code == 200 and response.json().get("ok"):
            return True
        else:
            st.error(f"❌ Error en la respuesta de Slack: {response.text}")
            return False

    except Exception as e:
        st.error(f"❌ Error enviando a Slack: {e}")
        return False
