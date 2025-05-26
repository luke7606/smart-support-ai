
# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto 8501 que usa Streamlit por defecto
EXPOSE 8501

# Comando de ejecución para levantar la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
# Imagen base oficial de Node.js
FROM node:18-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias e instalarlas
COPY package*.json ./
RUN npm install

# Copiar el resto del código fuente
COPY . .

# Exponer el puerto usado por la app
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["node", "server.js"]


