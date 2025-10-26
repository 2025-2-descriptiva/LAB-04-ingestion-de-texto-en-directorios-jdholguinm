# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    import zipfile
    import os
    import pandas as pd

    os.getcwd()

    zip_path = "files/input.zip"
    extract_to = "input/"

    # Crea la carpeta destino si no existe
    os.makedirs(extract_to, exist_ok=True)

    # Descomprimir
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print("✅ Archivo descomprimido en:", extract_to)

    data = []
    base_path = r"input/input"

    # Recorre train y test
    for dataset in os.listdir(base_path):
        dataset_path = os.path.join(base_path, dataset)
        # print(dataset_path)

        # Recorre positive, negative, neutral
        for sentiment in os.listdir(dataset_path):
            folder_path = os.path.join(dataset_path, sentiment)
            # print(folder_path)

            # Recorre todos los archivos .txt dentro de cada carpeta
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                # print(file_path)

                # Leer el contenido del archivo
                with open(file_path, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()

                # Agregar a la lista como diccionario
                data.append({
                    "dataset": dataset,
                    "phrase": phrase,
                    "target": sentiment
                })

    df = pd.DataFrame(data)

    # Generar los dataset test y train
    test_dataset = df[df["dataset"]=="test"].reset_index(drop=True)
    train_dataset = df[df["dataset"]=="train"].reset_index(drop=True)

    # Eliminar la columna dataset de test y train
    test_dataset = test_dataset.drop("dataset", axis=1)
    train_dataset = train_dataset.drop("dataset", axis=1)

    # Crea la carpeta destino de los csv si no existe
    rutacsv = "files/output/" 
    os.makedirs(rutacsv, exist_ok=True)

    # Guardar csv en la ruta indicada
    ruta_train= "train_dataset.csv"
    ruta_test= "test_dataset.csv"

    train_dataset.to_csv(os.path.join(rutacsv,ruta_train), index=False, encoding="utf-8")
    test_dataset.to_csv(os.path.join(rutacsv,ruta_test), index=False, encoding="utf-8")

if __name__ == "__main__":
    pregunta_01()


