# Titanic Survival Predictor - Aprendizaje Supervisado

Este proyecto implementa una solución de aprendizaje supervisado de extremo a extremo para predecir la supervivencia de los pasajeros del Titanic. Incluye el análisis de datos, ingeniería de características automática, entrenamiento de modelos comparativos, exportación de pipelines y un servidor local en Flask con una interfaz de usuario minimalista y premium en tonos azules oscuros.

---

## 🛠️ Stack Tecnológico

* **Machine Learning / Preprocesamiento**: `Python 3.13`, `pandas`, `scikit-learn` (Pipeline, ColumnTransformer, StandardScaler, OneHotEncoder), `joblib`.
* **Servidor Local / API**: `Flask`.
* **Interfaz de Usuario (Frontend)**: `HTML5`, `CSS3` (diseño responsivo, escala de azules HSL, *glassmorphism* y micro-animaciones), `JavaScript` (Fetch API para comunicación asíncrona).
* **Entornos Exploratorios**: `Jupyter Notebook` (`.ipynb`).

---

## 📂 Estructura del Proyecto

La estructura del proyecto está organizada modularmente de la siguiente manera:

```text
aprendizaje_supervisado/
├── data/
│   ├── titanic.csv             # Dataset original crudo
│   ├── titanic_clean.csv       # Dataset limpio (nulos imputados)
│   └── titanic_feature.csv     # Dataset exploratorio de características
├── templates/
│   └── index.html              # Frontend minimalista en escala de azules
├── clean.ipynb                 # 1. Notebook de Limpieza e Imputación de Datos
├── EDA.ipynb                   # 2. Notebook de Análisis Exploratorio de Datos
├── feature_engineering.ipynb   # 3. Notebook explicativo de Ingeniería de Características
├── train.ipynb                 # 4. Notebook de Modelamiento y Pipelines Simplificados
├── train.py                    # Script de automatización para entrenar los pipelines
├── app.py                      # Servidor Flask local que expone la API y sirve la UI
├── model_rf.joblib             # Pipeline empaquetado del Random Forest entrenado
└── model_lr.joblib             # Pipeline empaquetado de la Regresión Logística entrenada
```

---

## ⚙️ Arquitectura del Pipeline Simplificado

En lugar de aplicar mapeos manuales propensos a errores en producción, implementamos un **Pipeline unificado de scikit-learn** compuesto por un **ColumnTransformer**:

* **Variables Numéricas** (`Pclass`, `Age`, `SibSp`, `Parch`, `Fare`): Preprocesadas en memoria mediante `StandardScaler` para centrar y escalar los valores.
* **Variables Categóricas** (`Sex`, `Embarked`): Mapeadas dinámicamente mediante `OneHotEncoder(handle_unknown='ignore')`.

Este pipeline se empaqueta junto con el estimador final en un archivo `.joblib` único. De esta forma, el backend de Flask en `app.py` recibe los datos crudos en formato JSON y los procesa directamente con `pipeline.predict(df)` sin necesidad de codificar lógica de negocio personalizada o transformaciones manuales.

---

## 📊 Comparación de Modelos

Ambos modelos fueron entrenados utilizando una partición de entrenamiento/prueba del 80/20 estratificada sobre la variable objetivo:

| Modelo | Exactitud (Accuracy) en Prueba | F1-Score (Sobrevive) | Estado |
| :--- | :---: | :---: | :---: |
| **Random Forest Classifier** | **82.12%** | **0.72** | Guardado como `model_rf.joblib` |
| **Logistic Regression** | **80.45%** | **0.72** | Guardado como `model_lr.joblib` |

---

## 🚀 Instrucciones de Uso

### 1. Instalación de Dependencias
Antes de comenzar, instala todas las dependencias (ejecución y desarrollo) ejecutando:

```bash
pip install -r requirements-dev.txt
```

### 2. Entrenamiento de Modelos
Puedes entrenar los modelos de dos maneras:
* **Notebook**: Abre y ejecuta todas las celdas de [train.ipynb](file:///Users/leonelmendiola/aprendizaje_supervisado/train.ipynb).
* **Script de Consola**: Ejecuta la automatización en terminal:
  ```bash
  python3 train.py
  ```
  Esto generará de nuevo los archivos `model_rf.joblib` y `model_lr.joblib` actualizados con sus respectivas métricas de precisión.

### 3. Iniciar el Servidor de Producción Local
Para levantar el servidor Flask local, ejecuta:
```bash
python3 app.py
```
El servidor cargará automáticamente los modelos y se iniciará en `http://127.0.0.1:5001`.

### 4. Usar el Frontend Minimalista
Abre tu navegador e ingresa a `http://127.0.0.1:5001`. Podrás:
* Seleccionar de forma interactiva entre el modelo **Random Forest** y **Regresión Logística**.
* Rellenar el formulario con características personalizadas de un pasajero.
* Obtener predicciones en tiempo real sobre si sobrevive o no, junto con el porcentaje de confianza calculado por el modelo seleccionado.
