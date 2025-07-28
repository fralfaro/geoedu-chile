import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from code import plots  # Importa las funciones de visualización desde el módulo 'code.plots'

# Configuración de la página
st.set_page_config(
    page_title="GeoEdu Chile: Exploración Territorial Universitaria",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

class SidebarText:
    introduccion = """
    <h4>🌎 GeoEdu Chile</h4>
    Plataforma interactiva basada en el <b>Estudio de Contextualización Territorial Universitaria</b>, 
    desarrollado en el marco del proyecto <b>RED20993</b>.

    Esta aplicación permite explorar y analizar:
    <ul>
        <li>📊 La distribución territorial de instituciones educativas.</li>
        <li>🌍 La movilidad interregional de los estudiantes.</li>
        <li>📈 Las desigualdades regionales en puntajes, distancias y vulnerabilidad.</li>
    </ul>

    Todo con el propósito de fortalecer la toma de decisiones en educación superior con un enfoque territorial.
    """

    objetivos = """
    <h5>🎯 Objetivos del estudio</h5>
    <ul>
        <li>📌 Desarrollar un instrumento de contextualización territorial del ingreso universitario.</li>
        <li>📌 Analizar movilidad, puntajes, distancia y vulnerabilidad desde una perspectiva regional.</li>
        <li>📌 Apoyar la formulación de estrategias institucionales y políticas públicas.</li>
    </ul>
    """

    autores = """
    <h5>📄 Autores del estudio:</h5>
    <ul>
        <li><b>Francisco Alfaro</b> – UTFSM</li>
        <li><b>Gabriel Molina</b> – UTFSM</li>
        <li><b>Dorian Villegas </b> – UTFSM</li>
        <li><b>Valeska Canales</b> – UTFSM</li>
    </ul>
    <p><i>Fecha de publicación: diciembre de 2022</i></p>
    <p>🔗 <a href="https://centroestudios.mineduc.cl/datos-abiertos" target="_blank">Accede a la fuente de datos</a></p>
    """

class ImagesPath:
    logo = Path("images/logo.png")
    logo2 = Path("images/logo2.png")

def mostrar_sidebar():
    """
    Carga el contenido del panel lateral de la aplicación.
    """

    st.sidebar.image(ImagesPath.logo2, width=200)

    st.sidebar.title('🗺️ GeoEdu Chile: Exploración Territorial Universitaria')
    with st.sidebar:
        with st.expander("📘 Acerca de GeoEdu Chile"):
            st.markdown(SidebarText.introduccion, unsafe_allow_html=True)
            st.markdown(SidebarText.objetivos, unsafe_allow_html=True)
            st.markdown(SidebarText.autores, unsafe_allow_html=True)

def mostrar_cuerpo():
    """
    Cuerpo principal con tabs de navegación para GeoEdu Chile.
    """

    st.title("🗺️ GeoEdu Chile: Exploración Territorial Universitaria")

    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "🧭 Explorador Territorial",
        "🌍 Movilidad Interregional",
        "📊 Caracterización Regional"
    ])

    with tab1:
        st.header("🧭 Explorador Territorial")
        st.markdown("Explora la distribución de instituciones universitarias por tipo y dependencia.")

        df_tipo = pd.read_csv("data/plots/df_tipo_universidad.csv")
        df_dep = pd.read_csv("data/plots/df_tipodepen.csv")

        st.plotly_chart(plots.plotly_tipo_universidad_por_region(df_tipo), use_container_width=False)
        st.plotly_chart(plots.plotly_tipodepen_por_region(df_dep), use_container_width=True)

    with tab2:
        st.header("🌍 Movilidad Interregional")
        st.markdown("Analiza los flujos interregionales de estudiantes, tasas y distancias.")

        matriz = pd.read_csv("data/plots/df_matriz_movilidad.csv", index_col=0)
        df_tasas = pd.read_csv("data/plots/df_tasas_migracion.csv")
        df_dist = pd.read_csv("data/plots/df_migracion_distancia.csv")

        st.plotly_chart(plots.plotly_matriz_movilidad(matriz), use_container_width=True)
        st.plotly_chart(plots.plotly_tasas_migracion_recepcion(df_tasas), use_container_width=True)
        st.plotly_chart(plots.plotly_migracion_vs_distancia(df_dist), use_container_width=True)

    with tab3:
        st.header("📊 Caracterización Regional")
        st.markdown("Comparación regional de indicadores: puntajes, vulnerabilidad y distancia.")

        df_ivm = pd.read_csv("data/plots/df_ivm.csv")
        df_dist = pd.read_csv("data/plots/df_migracion_distancia.csv")

        st.plotly_chart(plots.plotly_ivm_por_region(df_ivm), use_container_width=True)
        st.plotly_chart(plots.plotly_tasa_vs_distancia(
            df_dist,
            col_x="DISTANCIA_PROMEDIO_RECEPCIÓN",
            col_y="Tasa Recepción (%)",
            titulo="Tasa de Recepción vs Distancia Promedio de Recepción",
            color="orange"
        ), use_container_width=True)

    # Estilos visuales
    estilos_css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.3rem;
        }
    </style>
    '''
    st.markdown(estilos_css, unsafe_allow_html=True)

def main():
    """
    Función principal que organiza la estructura de la aplicación.
    """
    mostrar_sidebar()
    mostrar_cuerpo()

# Ejecutar la aplicación si se llama directamente
if __name__ == "__main__":
    main()
