def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd 
    import matplotlib.pyplot as plt 
 
    path_file = r'data_lake/business/precios-diarios.csv' 
    datos = pd.read_csv(path_file, index_col=None, sep=',', header=0) 
 
    datos["fecha"] = pd.to_datetime(datos["fecha"]) 
    datos['mes'] = ((datos['fecha'].dt.month).astype(int)).astype(str) 
    datos['año'] = ((datos['fecha'].dt.year).astype(int)).astype(str)       
    input = datos.groupby("año").mean({"precio": "precio"}) 
    input.reset_index(inplace=True) 
 
    x=input.año 
    y=input.precio 
 
    plt.figure(figsize=(9, 6)) 
    plt.plot(x,y,'b',label='Promedio Anual') 
    plt.title('Promedio Anual') 
    plt.xlabel('Año') 
    plt.ylabel('Precio') 
    plt.legend() 
    plt.xticks(rotation="vertical") 
    plt.savefig("data_lake/business/reports/figures/daily_prices.png") 
    plt.show() 
 
    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
