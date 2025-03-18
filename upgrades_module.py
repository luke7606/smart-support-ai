import streamlit as st
import pandas as pd

# Datos de ejemplo de upgrades
upgrades = [
    {"Machine": "ds14111", "Location": "iad1-a6/u1/3u", "Upgrade Date": "2025-03-04", "Who Will Upgrade": "Andrii"},
    {"Machine": "ds11564", "Location": "iad1-a6/u15/3u", "Upgrade Date": "2025-03-04", "Who Will Upgrade": "Andrii"}
]

def gestion_upgrades():
    st.subheader("🔧 Gestión de Upgrades Programados")
    df_upgrades = pd.DataFrame(upgrades)

    if not df_upgrades.empty:
        st.dataframe(df_upgrades)
        st.download_button(
            label="⬇️ Descargar Upgrades en CSV",
            data=df_upgrades.to_csv(index=False).encode('utf-8'),
            file_name='upgrades.csv',
            mime='text/csv'
        )
    else:
        st.info("No hay upgrades programados.")
