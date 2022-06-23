def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import pandas as pd
    import xlwt

    def descargar_archivo(ruta, file_name, extension):
        for año in file_name:
            url_rute= ruta + '/' + año + extension + "?raw=true"
            nombre_archivo= "data_lake/landing/" , '{}{}'.format(año, extension)
            descarga= pd.read_excel(url_rute)
        return

    ruta= "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/"
    file_name1 = [str(año) for año in range(1995, 2016)]
    file_name2 = [str(año) for año in range(2018, 2022)]

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
