import streamlit as st
import pandas as pd

# Aquí simulamos una base de datos temporal con pandas (podrías conectar a una base real)
tickets = []

def generar_ticket():
    st.subheader("🎫 Generar Nuevo Ticket")

    # Formulario para crear el ticket
    with st.form("ticket_form"):
        nombre = st.text_input("Nombre del solicitante")
        email = st.text_input("Email de contacto")
        prioridad = st.selectbox("Prioridad", ["Baja", "Media", "Alta", "Crítica"])
        descripcion = st.text_area("Descripción del problema")
        
        submit = st.form_submit_button("Crear Ticket")

        if submit:
            nuevo_ticket = {
                "Nombre": nombre,
                "Email": email,
                "Prioridad": prioridad,
                "Descripción": descripcion
            }
            # Guardar ticket en la lista temporal
            tickets.append(nuevo_ticket)
            st.success("✅ Ticket creado con éxito")
            st.write("Resumen del ticket creado:", nuevo_ticket)


def ver_tickets():
    st.subheader("📄 Ver Tickets Existentes")

    # Si hay tickets, los muestra
    if tickets:
        df_tickets = pd.DataFrame(tickets)
        st.dataframe(df_tickets)

        # Exportar como CSV
        st.download_button(
            label="📥 Descargar Tickets en CSV",
            data=df_tickets.to_csv(index=False).encode('utf-8'),
            file_name='tickets.csv',
            mime='text/csv'
        )
    else:
        st.info("No hay tickets aún.")
