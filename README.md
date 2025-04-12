# Cloud Computing - Actividad 2: Bankrupcy Prediction

Este repositorio fue creado como parte de la clase de Cómputo en la Nube. El proyecto fue realizado por los equipos de Datos, Modelos y Cómputo en la Nube como parte de la actividad de la clase. El objetivo de la actividad es construir un servicio de predicción de bancarrota utilizando modelos de Machine Learning, para después desplegarlo como una API funcional en Microsoft Azure.

## Requisitos

- Python 3.10 o superior
- Librerías definidas en `requirements.txt`
- Acceso a Azure para el despliegue

## Datos utilizados

- **Fuente:** Kaggle – [Company Bankruptcy Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction)

Para descargar los datos:

```python
import kagglehub
import pandas as pd

path = kagglehub.dataset_download("fedesoriano/company-bankruptcy-prediction")
data = pd.read_csv(path + "/data.csv")

```

## Instrucciones de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/danyjimte0205/Actividad-2-Cloud-Computing.git
cd Actividad-2-Cloud-Computing
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Preprocesamiento de datos.

Antes de entrenar o enviar datos a la API, se deben procesar con el script `zorrouno.py`:

```python
from zorrouno import processor
df_procesado = processor.embbed(datos)
```

Este script elimina columnas no numéricas o no necesarias para el modelo, conserva todas las features financieras, y estandariza los nombres de las columnas.

### 4. Entrenamiento del modelo

Para entrenar el modelo se necesita ejecutar el notebook `Model.ipynb` con los datos preprocesados. Esto generará el archivo de modelo listo para ser desplegado.
