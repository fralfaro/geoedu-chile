import pandas as pd
import plotly.graph_objects as go

# usar la función
orden_regiones = [
    'Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 'Coquimbo',
    'Valparaíso', 'Metropolitana', "Lib. Gral B. O'Higgins", 'Maule', 'Ñuble',
    'Biobío', 'La Araucanía', 'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes'
    'Biobío', 'La Araucanía', 'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes'
]

tipos_universidad = [
    'Universidades Estatales CRUCH', 
    'Universidades Privadas', 
    'Universidades Privadas CRUCH'
]

def plot_tipo_universidad_por_region_plotly(df, tipos_universidad, orden_regiones):
    """
    Gráfico de barras apiladas horizontal con Plotly, mostrando el porcentaje de tipos de universidad por región.


    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con las columnas 'cod_inst', 'region_sede' y 'tipo_inst_3'.
    tipos_universidad : list
        Lista con los tipos de universidad a filtrar.
    orden_regiones : list
        Lista con las regiones ordenadas de norte a sur.
    """
    # Filtrar y eliminar duplicados
    df_filtered = df[df['tipo_inst_3'].isin(tipos_universidad)].copy()
    df_filtered_unique = df_filtered.drop_duplicates(subset=['cod_inst', 'region_sede', 'tipo_inst_3'])

    # Ordenar regiones como categoría
    df_filtered_unique['region_sede'] = pd.Categorical(df_filtered_unique['region_sede'],
                                                       categories=orden_regiones,
                                                       ordered=True)

    # Agrupar y calcular porcentaje
    df_grouped = df_filtered_unique.groupby(['region_sede', 'tipo_inst_3'], observed=True).size().unstack(fill_value=0)
    df_grouped = df_grouped.div(df_grouped.sum(axis=1), axis=0) * 100
    df_grouped = df_grouped.reindex(orden_regiones)

    # Crear gráfico Plotly
    fig = go.Figure()

    # Definir colores (puedes personalizar si deseas)
    colores = {
        'Universidades Estatales CRUCH': '#1f77b4',  # Azul
        'Universidades Privadas': '#2ca02c',         # Verde
        'Universidades Privadas CRUCH': '#ff7f0e',   # Naranja
    }

    for tipo in df_grouped.columns:
        fig.add_trace(go.Bar(
            y=df_grouped.index,
            x=df_grouped[tipo],
            name=tipo,
            orientation='h',
            marker=dict(color=colores.get(tipo, None)),
            text=[f'{val:.0f}%' if val > 0 else '' for val in df_grouped[tipo]],
            textposition='inside',
            insidetextanchor='middle'
        ))

    fig.update_layout(
        barmode='stack',
        title='Porcentaje Tipo Universidad por Región',
        xaxis_title='Porcentaje',
        yaxis_title='Región',
        height=600,
        legend_title='Tipo de Universidad',
        margin=dict(l=100, r=20, t=50, b=50)
    )

    fig.show()
