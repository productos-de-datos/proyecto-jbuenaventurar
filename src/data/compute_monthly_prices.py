def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd
    import datetime
    
    df=pd.read_csv('data_lake/cleansed/precios-horarios.csv', index_col=None, header=0)
    df["fecha"]= pd.to_datetime(df["fecha"])
    df['mes'] = df['fecha'].dt.month
    df['año'] = df['fecha'].dt.year
    dfam= df[['año', 'mes', 'precio']]
    dfn = dfam.groupby(['año', 'mes']).mean({'precio': 'precios'})
    df = df[['fecha', 'año', 'mes']]
    dff= df.merge(dfn, left_on=['año', 'mes'], right_on=['año', 'mes'])
    df = dff[['fecha', 'precio']]
    df.to_csv("data_lake/business/precios-mensuales.csv", index=None, header=True)
    
   # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
