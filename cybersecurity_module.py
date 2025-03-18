import streamlit as st

def analisis_ciberseguridad():
    st.title("🔒 Análisis de Ciberseguridad")

    descripcion = st.text_area("✍️ Descripción del Ticket")

    if st.button("🔍 Analizar Ticket"):
        amenazas_detectadas = []

        # Lista de palabras clave que indican posibles incidentes de ciberseguridad
        palabras_clave = [
            "hackeo",
            "phishing",
            "intrusión",
            "ransomware",
            "malware",
            "robo de datos",
            "ataque de denegación de servicio",
            "fuga de información",
            "vulnerabilidad",
            "exfiltración"
        ]

        # Analiza si alguna de las palabras clave está en la descripción del ticket
        for palabra in palabras_clave:
            if palabra in descripcion.lower():
                amenazas_detectadas.append(palabra)

        # Muestra el resultado
        if amenazas_detectadas:
            st.error(f"⚠️ Amenazas detectadas: {', '.join(amenazas_detectadas)}")
        else:
            st.success("✅ No se detectaron amenazas de ciberseguridad.")
