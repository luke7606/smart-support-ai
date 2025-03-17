from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento de ejemplo
X_train = [
    "Error 404 y caídas de servidor",
    "No puedo acceder al sistema",
    "Se corta la conexión",
    "Error 500 en la página web",
    "Actualización de software",
    "Instalación de parches de seguridad",
    "Problemas con el login de usuarios",
]
y_train = [
    "Conectividad",
    "Conectividad",
    "Conectividad",
    "Conectividad",
    "Software",
    "Software",
    "Acceso"
]

# Vectorizador y modelo
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

def analizar_ticket(texto):
    X_test_tfidf = vectorizer.transform([texto])
    prediccion = model.predict(X_test_tfidf)
    return prediccion[0]
