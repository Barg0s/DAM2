import pandas as pd
import csv

# Ruta del archivo CSV
csv_file = "ClasificacioText\\Exercici 0\\data\\engorother.csv"

# Función para probar varias soluciones
def test_csv_read():
    try:
        # 1. Leer las primeras 10 líneas del archivo para diagnosticar la línea problemática
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print("Primeras 10 líneas del archivo:")
            print("".join(lines[:10]))  # Imprime las primeras 10 líneas para revisión

        # 2. Intentar leer el CSV con varias configuraciones para diagnosticar problemas
        print("\nIntentando leer el CSV con diferentes configuraciones...")

        # Solución 1: Leer el CSV sin omitir nada
        print("\nLeyendo el archivo CSV con el delimitador por defecto (coma):")
        df = pd.read_csv(csv_file, encoding='utf-8')
        print(df.head(5))  # Muestra las primeras 5 filas para ver si se carga correctamente

        # Solución 2: Usar un delimitador explícito (por si hay un problema con las comas)
        print("\nLeyendo el archivo CSV con delimitador explícito (coma):")
        df = pd.read_csv(csv_file, encoding='utf-8', delimiter=',')
        print(df.head(5))

        # Solución 3: Ignorar espacios adicionales después de las comas
        print("\nLeyendo el archivo CSV ignorando espacios adicionales después de las comas:")
        df = pd.read_csv(csv_file, encoding='utf-8', skipinitialspace=True)
        print(df.head(5))

        # Solución 4: Especificar el tipo de comillas (si hay comillas que causan problemas)
        print("\nLeyendo el archivo CSV con QUOTING_MINIMAL para tratar comillas:")
        df = pd.read_csv(csv_file, encoding='utf-8', quoting=csv.QUOTE_MINIMAL)
        print(df.head(5))

        # Solución 5: Leer solo las primeras 5 filas
        print("\nLeyendo solo las primeras 5 filas del CSV:")
        df = pd.read_csv(csv_file, encoding='utf-8', nrows=5)
        print(df)

    except Exception as e:
        print("\nError al leer el archivo CSV:", str(e))

# Ejecutar la función de prueba
test_csv_read()
