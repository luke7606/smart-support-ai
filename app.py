import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from tickets_module import generar_ticket, ver_tickets
from multisheets_module import mostrar_upgrades_multisheets
from upgrades_module import gestion_upgrades
from cybersecurity_module import analisis_ciberseguridad
from project_processes_module import procesos_proyectos
from statistics_dashboard_module import dashboard_estadisticas
from ia_module import analisis_ia_tickets

st.set_page_config(page_title="Smart Support - Sistema de Tickets", layout="wide")

# ============================
# HEADER PRINCIPAL
# ============================
st.title("🎟️ Smart Support – Sistema de Tickets")
st.subheader("Tu Asistente de Seguridad y Soporte Post-Implementación")

# ============================
# MENÚ PRINCIPAL
# ============================
opciones = [
    "Seleccionar",
    "Generar Ticket",
    "Ver Tickets",
    "Ver Tutoriales",
    "Análisis de Ciberseguridad",
    "Procesos de Proyectos",
    "Dashboard de Estadísticas",
    "Análisis IA de Tickets",
    "Gestión de Upgrades",
    "Upgrades desde Google Sheets"
]

opcion = st.selectbox("🎯 Selecciona un módulo:", opciones)

# ============================
# LÓGICA DE NAVEGACIÓN
# ============================
if opcion == "Generar Ticket":
    generar_ticket()

elif opcion == "Ver Tickets":
    ver_tickets()

elif opcion == "Ver Tutoriales":
    st.info("Módulo en construcción...")

elif opcion == "Análisis de Ciberseguridad":
    analisis_ciberseguridad()

elif opcion == "Procesos de Proyectos":
    procesos_proyectos()

elif opcion == "Dashboard de Estadísticas":
    dashboard_estadisticas()

elif opcion == "Análisis IA de Tickets":
    analisis_ia_tickets()

elif opcion == "Gestión de Upgrades":
    gestion_upgrades()

elif opcion == "Upgrades desde Google Sheets":
    mostrar_upgrades_multisheets()

else:
    st.info("Por favor, selecciona una opción en el menú para comenzar.")
