# Importar librerías necesarias
from flask import Flask, request, jsonify   # Flask para crear la API, request/jsonify para manejar datos JSON
import pickle                               # Para cargar el modelo entrenado guardado en archivo .pkl
import numpy as np                          # Para manejar arreglos numéricos

# Variable global para almacenar el modelo
modelo = None

# Cargar el modelo entrenado desde archivo .pkl
with open("models/modelo.pkl", 'rb') as file:
    modelo = pickle.load(file)

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir endpoint /predecir que recibe solicitudes POST
@app.route('/predecir', methods=['POST'])
def predict():
    # Obtener los datos enviados en formato JSON
    data = request.get_json(force=True)
    
    # Convertir los datos de entrada a un arreglo NumPy con forma (1, -1)
    input_data = np.array(data['input']).reshape(1, -1)
    
    # Usar el modelo cargado para hacer la predicción
    prediccion = modelo.predict(input_data)
    
    # Devolver la predicción como JSON (convertida a int para evitar problemas de serialización)
    return jsonify({'prediccion': int(prediccion[0])})

# Ejecutar la aplicación en modo debug si se corre directamente
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 

