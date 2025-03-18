import streamlit as st

# Importando módulos directamente (porque están en la raíz)
from tickets_module import generar_ticket, ver_tickets
from tutorials_module import ver_tutoriales
from cybersecurity_module import analisis_ciberseguridad
from project_processes_module import procesos_proyectos
from statistics_dashboard_module import dashboard_estadisticas
from ia_module import analisis_ia_tickets
from upgrades_module import gestion_upgrades
from multisheets_module import mostrar_upgrades_multisheets

# =========================================
# Configuración de la página
# =========================================
st.set_page_config(page_title="Smart Support – Sistema de Tickets", layout="wide")

# =========================================
# HEADER PRINCIPAL
# =========================================
st.title("🛠️ Smart Support – Sistema de Tickets")
st.subheader("Tu Asistente de Seguridad y Soporte Post-Implementación")

# =========================================
# MENÚ PRINCIPAL
# =========================================
menu = st.sidebar.selectbox(
    "Selecciona una opción",
    (
        "Inicio",
        "Generar Ticket",
        "Ver Tickets",
        "Tutoriales",
        "Ciberseguridad",
        "Procesos de Proyectos",
        "Dashboard de Estadísticas",
        "Análisis IA de Tickets",
        "Gestión de Upgrades",
        "MultiSheets Upgrades"
    )
)

# =========================================
# LÓGICA DEL MENÚ
# =========================================
if menu == "Inicio":
    st.write("Bienvenido al sistema de soporte Smart Support AI.")

elif menu == "Generar Ticket":
    generar_ticket()

elif menu == "Ver Tickets":
    ver_tickets()

elif menu == "Tutoriales":
    ver_tutoriales()

elif menu == "Ciberseguridad":
    analisis_ciberseguridad()

elif menu == "Procesos de Proyectos":
    procesos_proyectos()

elif menu == "Dashboard de Estadísticas":
    dashboard_estadisticas()

elif menu == "Análisis IA de Tickets":
    analisis_ia_tickets()

elif menu == "Gestión de Upgrades":
    gestion_upgrades()

elif menu == "MultiSheets Upgrades":
    mostrar_upgrades_multisheets()
