import streamlit as st

def procesos_proyectos():
    st.title("📂 Procesos de Proyectos")

    procesos = [
        {"ID": 1, "Proceso": "Inicio del Proyecto", "Estado": "Completado"},
        {"ID": 2, "Proceso": "Planificación", "Estado": "En Progreso"},
        {"ID": 3, "Proceso": "Ejecución", "Estado": "Pendiente"},
        {"ID": 4, "Proceso": "Cierre", "Estado": "Pendiente"}
    ]

    st.write("📋 Lista de Procesos del Proyecto:")
    for proceso in procesos:
        st.write(f"🔹 {proceso['Proceso']} - Estado: {proceso['Estado']}")
