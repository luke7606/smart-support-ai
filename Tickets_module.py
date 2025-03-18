import streamlit as st
import pandas as pd

def generar_ticket():
    st.title("Generar Nuevo Ticket")
    titulo = st.text_input("Título del Ticket")
    descripcion = st.text_area("Descripción del Ticket")
    if st.button("Enviar Ticket"):
        st.success(f"Ticket '{titulo}' ha sido enviado correctamente.")

def ver_tickets():
    st.title("Ver Tickets Existentes")
    tickets = [
        {"ID": 1, "Título": "Error de red", "Estado": "Abierto"},
        {"ID": 2, "Título": "Falla de disco", "Estado": "En progreso"}
    ]
    df = pd.DataFrame(tickets)
    st.table(df)
