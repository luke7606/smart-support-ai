import streamlit as st

# Importando módulos directamente
from tickets_module import generar_ticket, ver_tickets
from tutorials_module import ver_tutoriales
from cybersecurity_module import analisis_ciberseguridad
from projects_module import procesos_proyectos

st.sidebar.title("Smart Support AI 🚀")

opcion = st.sidebar.radio(
    "Selecciona una opción:",
    (
        "🏠 Inicio",
        "🎫 Gestión de Tickets",
        "📖 Tutoriales",
        "🔒 Análisis de Ciberseguridad",
        "📂 Procesos de Proyectos"
    )
)

if opcion == "🏠 Inicio":
    st.title("Bienvenido a Smart Support AI")
    st.write("Selecciona una opción del menú para comenzar.")

elif opcion == "🎫 Gestión de Tickets":
    generar_ticket()
    ver_tickets()

elif opcion == "📖 Tutoriales":
    ver_tutoriales()

elif opcion == "🔒 Análisis de Ciberseguridad":
    analisis_ciberseguridad()

elif opcion == "📂 Procesos de Proyectos":
    procesos_proyectos()
