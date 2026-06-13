import pandas as pd

# Cargar el dataset
df = pd.read_csv('data/titanic.csv')

# Eliminar la columna Parch
if 'Parch' in df.columns:
    df.drop(columns=['Parch'], inplace=True)
    print("Columna 'Parch' eliminada.")
else:
    print("La columna 'Parch' no existe en el dataset.")

# Guardar el nuevo CSV
df.to_csv('data/titanic_clean.csv', index=False)
print("Archivo 'data/titanic_clean.csv' generado exitosamente.")
