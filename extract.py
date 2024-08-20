import pandas as pd
import glob
# lectura de archivos con formato * - ?
# sql like % y _
# %o -
# _o -

# Definición de funciones de extracción
def extract_from_csv(file_to_process):
    """Extrae datos de un archivo CSV."""
    #lectura del archivo
    dataframe=pd.read_csv(file_to_process)
    # Practica
    #origen
    #tipo
    return dataframe


def extract_from_json(file_to_process):
    """Extrae datos de un archivo JSON."""
    #lectura del archivo
    dataframe=pd.read_json(file_to_process)
    return dataframe


def extract_from_xml(file_to_process):
    """Extrae datos de un archivo XML."""
    #lectura del archivo
    dataframe=pd.read_xml(file_to_process)
    return dataframe


def extract():
    # Crea un dataset vacio con las columnas de nombre dentro del array
    extracted_data = pd.DataFrame(columns=['nombre', 'ventas1', 'ventas'])

    # Procesar todos los archivos CSV
    for csvfile in glob.glob("datos_unidad5/*.csv"):
        print(csvfile)
        data = extract_from_csv(csvfile)
        #une los datasets
        extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    # Procesar todos los archivos JSON
    for jsonfile in glob.glob("datos_unidad5/*.json"):
        print(jsonfile)
        data = extract_from_json(jsonfile)
        extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    # Procesar todos los archivos XML
    for xmlfile in glob.glob("datos_unidad5/*.xml"):
        print(xmlfile)
        data = extract_from_xml(xmlfile)
        extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    return extracted_data


# Ejecutar la extracción y mostrar los primeros registros
extracted_data = extract()
print('Proceso de extracción completado.')
print(extracted_data)

# Dar el siguiente formato y leer los archivos
# datos_unidad5
#   enero
#       source1.csv
#       source1.json
#       source1.xml

# Aplica la lectura de archivos a used_car_prices