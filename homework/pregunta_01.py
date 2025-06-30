"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    
    plt.figure()
    
    # Diccionario de colores en español
    colores = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }
    
    # Orden de capas (z-order) en español
    orden_capas = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }
    
    # Ancho de líneas en español
    ancho_lineas = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }
    
    # Leer el archivo CSV
    df = pd.read_csv('files/input/news.csv', index_col=0)
    
    # Crear las líneas del gráfico
    for columna in df.columns:
        plt.plot(
            df[columna], 
            label=columna,
            color=colores[columna],
            zorder=orden_capas[columna],
            linewidth=ancho_lineas[columna]
        ) 
        
    # Configurar el título y los ejes
    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    # Agregar puntos y etiquetas al inicio y final de cada línea
    for columna in df.columns:
        primer_año = df.index[0]
        plt.scatter(
            x=primer_año,
            y=df[columna][primer_año],
            color=colores[columna],
            zorder=orden_capas[columna],
        )
        
        plt.text(
            primer_año - 0.2,
            df[columna][primer_año],
            columna + " " + str(df[columna][primer_año]) + '%',
            ha='right',
            va='center',
            color=colores[columna],
        )
        
        ultimo_año = df.index[-1]
        plt.scatter(
            x=ultimo_año,
            y=df[columna][ultimo_año],
            color=colores[columna],
        )
        
        plt.text(
            ultimo_año + 0.2,
            df[columna][ultimo_año],
            str(df[columna][ultimo_año]) + '%',
            ha='left',
            va='center',
            color=colores[columna],
        )
    
    # Configurar las etiquetas del eje x
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )
    plt.tight_layout()

    # Crear el directorio si no existe y guardar la imagen
    if not os.path.exists('files/plots'):
        os.makedirs('files/plots')
    plt.savefig('files/plots/news.png')
