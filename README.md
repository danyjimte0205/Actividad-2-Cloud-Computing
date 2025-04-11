# Cloud Computing - Actividad 2: Bankrupcy Prediction

Este repositorio fue creado como parte de la clase de Computación en la Nube. El proyecto fue realizado por los equipos de Datos, Modelos y Cómputo en la Nube como parte de la actividad de la clase. El objetivo de la actividad es construir un servicio de predicción de bancarrota utilizando modelos de Machine Learning, para después desplegarlo como una API funcional en Microsoft Azure.

## Requisitos

- Python 3.10 + 

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


