import streamlit as st
import pandas as pd

# Datos de prueba de tickets
tickets = [
    {"ID": 1, "Título": "Error de red", "Estado": "Abierto"},
    {"ID": 2, "Título": "Falla de disco", "Estado": "En progreso"}
]

def generar_ticket():
    st.subheader("📝 Generar Nuevo Ticket")
    titulo = st.text_input("Título del ticket")
    descripcion = st.text_area("Descripción del problema")

    if st.button("Crear Ticket"):
        nuevo_ticket = {
            "ID": len(tickets) + 1,
            "Título": titulo,
            "Estado": "Abierto"
        }
        tickets.append(nuevo_ticket)
        st.success(f"✅ Ticket '{titulo}' creado exitosamente!")

def ver_tickets():
    st.subheader("📋 Lista de Tickets")
    df_tickets = pd.DataFrame(tickets)

    if not df_tickets.empty:
        st.dataframe(df_tickets)
        st.download_button(
            label="⬇️ Descargar Tickets en CSV",
            data=df_tickets.to_csv(index=False).encode('utf-8'),
            file_name='tickets.csv',
            mime='text/csv'
        )
    else:
        st.info("No hay tickets aún.")
