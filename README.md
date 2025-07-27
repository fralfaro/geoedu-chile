
# Estudio de Contextualización Territorial Universitaria

Este repositorio contiene el código, análisis y visualizaciones del *Estudio de Contextualización Territorial Universitaria*, realizado en el marco del proyecto RED20993.

El objetivo del estudio es caracterizar el ingreso de estudiantes jóvenes a universidades chilenas, integrando datos de admisión, distancia entre establecimientos, movilidad interregional e índice de vulnerabilidad, con un enfoque geoestadístico y territorial.

## 🔍 Contenido

- Análisis exploratorio de datos educativos públicos
- Cálculo de distancias entre establecimientos y universidades
- Matriz de movilidad interregional
- Agrupamiento de regiones según características socioeducativas
- Visualizaciones interactivas

## 📁 Estructura

```
data/           → Bases de datos públicas utilizadas
notebooks/      → Jupyter notebooks con el análisis
scripts/        → Funciones auxiliares y procesamiento de datos
resultados/     → Gráficos y tablas del estudio
```

La carpeta `data` contiene los datos utilizados y generados en el proyecto.

```
data/
├── clean/
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   └── 2024/
└── raw/
    ├── 2021/
    │   ├── establecimientos/
    │   └── inmuebles_ies/
    ├── 2022/
    │   ├── establecimientos/
    │   └── inmuebles_ies/
    ├── 2023/
    │   ├── establecimientos/
    │   └── inmuebles_ies/
    └── 2024/
        ├── establecimientos/
        └── inmuebles_ies/
```

### Descripción

- `raw/`: Contiene los archivos originales entregados por distintas fuentes (matrícula, puntajes PSU/PAES, IVM, establecimientos escolares y universidades). Los datos están organizados por año.

- `clean/`: Contiene los archivos procesados y unificados por año. Se generan los siguientes conjuntos:
  - `set_a.csv` — Datos de matrícula.
  - `set_b.csv` — Datos de puntajes PSU/PAES.
  - `set_c.csv` — Datos de establecimientos escolares (coordenadas).
  - `set_d.csv` — Datos de universidades (coordenadas).
  - `set_e.csv` — Datos de IVM.
  - `set_ab.csv` a `set_abcde.csv` — Datos integrados entre los distintos conjuntos.

> **Observaciones**:
>
> - Los archivos `set_c` (establecimientos escolares) y `set_d` (universidades) corresponden al año 2021 y se utilizan de forma común para todos los años analizados (2021-2024).
>
> - A partir del año 2024, el archivo de puntajes cambia su nombre de `A_INSCRITOS_PUNTAJES_PAES_2024_PUB_MRUN.csv` a `A_INSCRITOS_PUNTAJES_2024_PAES_PUB.csv`.

## 🧩 Fuentes de datos

- [matricula](https://datosabiertos.mineduc.cl/matricula-en-educacion-superior/) - Matrícula en Educación Superior
- [puntajes](https://datosabiertos.mineduc.cl/pruebas-de-admision-a-la-educacion-superior/) - Resultados de admisión
- [ivm](https://www.junaeb.cl/medicion-la-vulnerabilidad-ivm/)- Índice de Vulnerabilidad Multidimensional (IVM)
- [establecimientos](https://www.geoportal.cl/geoportal/catalog/35408/Establecimientos%20Educaci%C3%B3n%20Escolar) - Georreferenciación de establecimientos
- [inmuebles_ies](https://www.geoportal.cl/geoportal/catalog/35408/Establecimientos%20Educaci%C3%B3n%20Escolar) - Georreferenciación de universidades



## 🛠 Requisitos

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Luego, ejecuta los siguientes notebooks según el flujo de trabajo:

- `notebooks/00_raw2clean.ipynb` — Limpieza y procesamiento de los datos originales (raw) a datos finales (clean).
- `notebooks/01_EDA.ipynb` — Análisis exploratorio de datos (EDA), donde se generan los gráficos utilizados en el artículo, diferenciados por año objetivo.



## 🚀 TO-DO

Aún quedan algunos temas pendientes por desarrollar en este proyecto:

* **📊 Visualización Interactiva**: Implementar una aplicación en `Streamlit` para explorar los datos de manera interactiva.
* **☁️ Almacenamiento en la Nube**: Guardar los datasets procesados (`clean`) en Google Cloud Storage (GCS) para facilitar el acceso y despliegue de los datos.

