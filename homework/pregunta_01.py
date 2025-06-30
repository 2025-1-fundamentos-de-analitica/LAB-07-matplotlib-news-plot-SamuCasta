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

    # Importar las librerías necesarias
    import pandas as pd          # Para manipulación de datos (DataFrames)
    import matplotlib.pyplot as plt  # Para crear gráficos
    import os                    # Para operaciones del sistema de archivos
    
    # Crear una nueva figura para el gráfico
    plt.figure()
    
    # PASO 1: Definir los estilos visuales para cada tipo de medio
    # Diccionario que asigna un color específico a cada medio de comunicación
    colores = {
        'Television': 'dimgray',     # Gris oscuro para TV
        'Newspaper': 'grey',         # Gris para periódicos
        'Internet': 'tab:blue',      # Azul para Internet (resaltar como principal)
        'Radio': 'lightgrey',        # Gris claro para radio
    }
    
    # Diccionario que define el orden de las capas (z-order) - mayor número aparece encima
    orden_capas = {
        'Television': 1,    # Capa inferior
        'Newspaper': 1,     # Capa inferior
        'Internet': 2,      # Capa superior (se ve por encima de las otras)
        'Radio': 1,         # Capa inferior
    }
    
    # Diccionario que define el grosor de las líneas para cada medio
    ancho_lineas = {
        'Television': 2,    # Línea normal
        'Newspaper': 2,     # Línea normal
        'Internet': 4,      # Línea más gruesa (enfatizar importancia)
        'Radio': 2,         # Línea normal
    }
    
    # PASO 2: Cargar y procesar los datos
    # Leer el archivo CSV con los datos de noticias, usando la primera columna como índice (años)
    df = pd.read_csv('files/input/news.csv', index_col=0)
    
    # PASO 3: Crear las líneas principales del gráfico
    # Iterar sobre cada columna (medio de comunicación) en el DataFrame
    for columna in df.columns:
        plt.plot(
            df[columna],                    # Datos del eje Y (porcentajes)
            label=columna,                  # Etiqueta para la leyenda
            color=colores[columna],         # Color específico del medio
            zorder=orden_capas[columna],    # Orden de la capa (cuál aparece encima)
            linewidth=ancho_lineas[columna] # Grosor de la línea
        ) 
        
    # PASO 4: Configurar la apariencia del gráfico
    # Establecer el título principal del gráfico
    plt.title('How people get their news', fontsize=16)
    
    # Ocultar los bordes del gráfico para un aspecto más limpio
    plt.gca().spines['top'].set_visible(False)      # Ocultar borde superior
    plt.gca().spines['right'].set_visible(False)    # Ocultar borde derecho
    plt.gca().spines['left'].set_visible(False)     # Ocultar borde izquierdo
    plt.gca().axes.get_yaxis().set_visible(False)   # Ocultar eje Y (sin números)
    
    # PASO 5: Agregar puntos y etiquetas en los extremos de cada línea
    # Esto hace que el gráfico sea más informativo mostrando valores exactos
    for columna in df.columns:
        # PUNTO Y ETIQUETA AL INICIO (primer año)
        primer_año = df.index[0]  # Obtener el primer año de los datos
        
        # Crear un punto circular al inicio de la línea
        plt.scatter(
            x=primer_año,                   # Posición X (año)
            y=df[columna][primer_año],      # Posición Y (porcentaje)
            color=colores[columna],         # Color del punto
            zorder=orden_capas[columna],    # Orden de la capa
        )
        
        # Agregar texto con el nombre del medio y su porcentaje inicial
        plt.text(
            primer_año - 0.2,               # Posición X (ligeramente a la izquierda)
            df[columna][primer_año],        # Posición Y (mismo nivel que el punto)
            columna + " " + str(df[columna][primer_año]) + '%',  # Texto: "Medio XX%"
            ha='right',                     # Alineación horizontal: derecha
            va='center',                    # Alineación vertical: centro
            color=colores[columna],         # Color del texto
        )
        
        # PUNTO Y ETIQUETA AL FINAL (último año)
        ultimo_año = df.index[-1]  # Obtener el último año de los datos
        
        # Crear un punto circular al final de la línea
        plt.scatter(
            x=ultimo_año,                   # Posición X (año)
            y=df[columna][ultimo_año],      # Posición Y (porcentaje)
            color=colores[columna],         # Color del punto
        )
        
        # Agregar texto solo con el porcentaje final
        plt.text(
            ultimo_año + 0.2,               # Posición X (ligeramente a la derecha)
            df[columna][ultimo_año],        # Posición Y (mismo nivel que el punto)
            str(df[columna][ultimo_año]) + '%',  # Texto: "XX%"
            ha='left',                      # Alineación horizontal: izquierda
            va='center',                    # Alineación vertical: centro
            color=colores[columna],         # Color del texto
        )
    
    # PASO 6: Configurar el eje X (años)
    # Mostrar todos los años disponibles en el eje X
    plt.xticks(
        ticks=df.index,     # Posiciones de las marcas (todos los años)
        labels=df.index,    # Etiquetas de las marcas (mismos años)
        ha='center',        # Alineación horizontal: centro
    )
    
    # Ajustar automáticamente el diseño para evitar solapamientos
    plt.tight_layout()

    # PASO 7: Guardar el gráfico como archivo PNG
    # Crear el directorio de destino si no existe
    if not os.path.exists('files/plots'):
        os.makedirs('files/plots')
    
    # Guardar el gráfico en el archivo especificado
    plt.savefig('files/plots/news.png')
