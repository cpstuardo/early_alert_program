import os
import pandas as pd

def xlsx_to_csv(input_path, output_path):
    # Leer el archivo Excel
    df = pd.read_excel(input_path)

    # Guardar como archivo CSV con codificación utf-8
    df.to_csv(output_path, index=False, encoding='utf-8')

if __name__ == "__main__":
    # Obtener la ruta del directorio actual del script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Iterar sobre todos los archivos en el directorio actual
    for filename in os.listdir(script_directory):
        # Verificar si el archivo es un archivo xlsx
        if filename.endswith(".xlsx"):
            # Construir rutas de entrada y salida
            input_excel_path = os.path.join(script_directory, filename)
            output_csv_path = os.path.join(script_directory, os.path.splitext(filename)[0] + ".csv")

            # Llamar a la función para convertir
            xlsx_to_csv(input_excel_path, output_csv_path)

            print(f"La conversión de {input_excel_path} a {output_csv_path} se ha completado.")
