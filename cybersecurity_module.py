# cybersecurity.py

def analizar_ticket_ciberseguridad(descripcion):
    amenazas_detectadas = []
    
    # Lista de palabras clave que indican posibles incidentes de ciberseguridad
    palabras_clave = [
        "hackeo", "phishing", "intrusión", "ransomware", "malware",
        "robo de datos", "ataque de denegación de servicio", "fuga de información",
        "vulnerabilidad", "exfiltración"
    ]
    
    # Analiza si alguna de las palabras clave está en la descripción del ticket
    for palabra in palabras_clave:
        if palabra in descripcion.lower():
            amenazas_detectadas.append(palabra)
    
    if amenazas_detectadas:
        return {
            "resultado": "Amenaza detectada",
            "detalles": amenazas_detectadas,
            "prioridad": "Crítica"
        }
    else:
        return {
            "resultado": "Sin amenazas",
            "detalles": [],
            "prioridad": "Normal"
        }
