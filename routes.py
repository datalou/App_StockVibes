from flask import Blueprint, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification

main = Blueprint('main', __name__)

# Cargar el modelo preentrenado para clasificación de texto
tokenizer = AutoTokenizer.from_pretrained("RashidNLP/Finance-Sentiment-Classification")
model = AutoModelForSequenceClassification.from_pretrained("RashidNLP/Finance-Sentiment-Classification")

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/analizar_sentimiento', methods=['POST'])
def analizar_sentimiento():
    if request.method == 'POST':
        # Obtener el texto del formulario
        texto = request.form['texto']

        # Tokenizar el texto
        inputs = tokenizer(texto, return_tensors="pt")

        # Realizar la predicción de sentimiento
        outputs = model(**inputs)
        logits = outputs.logits
        probabilidad = logits.softmax(dim=1)
        sentimiento_predicho = probabilidad.argmax().item()

        # Mapear el índice de sentimiento predicho a etiqueta (o usar según tu necesidad)
        etiquetas = ["Negativo", "Neutral", "Positivo"]  # Modifica según las clases de tu modelo
        sentimiento_predicho_etiqueta = etiquetas[sentimiento_predicho]

        return render_template('resultado.html', sentimiento_predicho=sentimiento_predicho_etiqueta)

    return render_template('index.html')

