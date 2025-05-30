import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import os
import numpy as np
import xarray as xr
import pandas as pd
import plotly.express as px


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Proyecto Final: Anomalía en la temperatura"
server = app.server

# =====================================
# Paleta de Colores Mejorada
# =====================================
COLORS = {
    'background': '#1a2634',
    'card_background': '#243447',
    'text': '#ffffff',
    'accent': '#3cbaec',
    'highlight': '#ff6b6b',
    'accent_subtle': '#2c3e50'
}

# =====================================
# Componentes Personalizados
# =====================================
def create_section(title, content):
    return html.Div([
        html.H3(title, style={
            'color': COLORS['accent'],
            'borderBottom': f'2px solid {COLORS["highlight"]}',
            'paddingBottom': '10px',
            'fontFamily': 'Roboto, sans-serif'
        }),
        html.Div(content, style={'marginTop': '20px'})
    ], className='section-card', style={'padding': '25px'})

# =====================================
# Layout Principal Mejorado
# =====================================
app.layout = dbc.Container([
    
    # Encabezado con efecto glow
    html.Div([
        html.H1("PROYECTO FINAL: ANOMALÍAS TÉRMICAS",
                className='glow-title',
                style={
                    'color': COLORS['accent'],
                    'textAlign': 'center',
                    'padding': '40px',
                    'fontSize': '2.5rem',
                    'fontFamily': 'Roboto, sans-serif'
                }),
        html.Hr(style={'borderColor': COLORS['accent'], 'width': '60%', 'margin': 'auto'})
    ], style={'marginBottom': '40px'}),

    # Tabs con diseño mejorado
    dbc.Row([
        dbc.Col([
            dcc.Tabs(
                id='tabs-proyecto',
                value='tab-intro',
                children=[
                    dcc.Tab(label='1. Introducción', value='tab-intro', className='custom-tab'),
                    dcc.Tab(label='2. Contexto', value='tab-contexto', className='custom-tab'),
                    dcc.Tab(label='3. Planteamiento', value='tab-problema', className='custom-tab'),
                    dcc.Tab(label='4. Objetivos', value='tab-objetivos', className='custom-tab'),
                    dcc.Tab(label='5. Marco Teórico', value='tab-teorico', className='custom-tab'),
                    dcc.Tab(label='6. Metodología', value='tab-metodologia', className='custom-tab'),
                    dcc.Tab(label='7. Resultados', value='tab-resultados', className='custom-tab'),
                    dcc.Tab(label='8. Conclusiones', value='tab-conclusiones', className='custom-tab')
                ],
                colors={'border': 'none'}
            ),
            html.Div(id='main-content', style={'padding': '30px'})
        ], width=12)
    ]),

    # Footer estilizado
    html.Footer(
        "© 2024 Análisis Climático Avanzado - Universidad del Norte",
        style={
            'color': COLORS['text'],
            'textAlign': 'center',
            'padding': '30px',
            'marginTop': '50px',
            'borderTop': f'1px solid {COLORS["accent"]}'
        }
    )
], fluid=True, style={
    'backgroundColor': COLORS['background'],
    'minHeight': '100vh',
    'padding': '40px 20px',
    'fontFamily': 'Open Sans, sans-serif'
})

# =====================================
# Callback con contenido de ejemplo
# =====================================
@app.callback(
    Output("main-content", "children"),
    [Input("tabs-proyecto", "value")]
)
def render_content(tab):
    print(f"DEBUG: Callback activado. Valor de la pestaña seleccionada: '{tab}'") # Para ver qué 'tab' se recibe

    text_style = {'color': COLORS['text'], 'textAlign': 'justify', 'lineHeight': '1.8'}
    
    if tab == "tab-intro":
        contenido_introduccion = [
            dbc.Row([
                dbc.Col([
                    
                    html.H3("Análisis y Predicción de Anomalías de Temperatura Global", 
                            style={'color': COLORS['accent'], 'textAlign': 'center', 'marginBottom': '25px'}),
            
                    html.Div([ 
                        html.P("""
                            El cambio climático es uno de los desafíos más apremiantes de nuestra era, manifestándose 
                            principalmente a través del aumento de las temperaturas globales. Comprender y predecir 
                            las anomalías de temperatura —las desviaciones respecto a los promedios climáticos históricos— 
                            es crucial para evaluar los impactos, diseñar estrategias de mitigación y adaptarse a 
                            un clima en constante evolución.
                            """, style=text_style),
                    ], style={'marginBottom': '20px'}), # Espacio después del párrafo
                    
                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),
                    
                    # Bloque 2: Objetivo del Proyecto
                    html.Div([ # Puedes añadir className='info-card' aquí si quieres este bloque como tarjeta
                        html.H5("Objetivo del Proyecto", style={'color': COLORS['highlight'], 'marginTop': '20px', 'marginBottom': '10px'}),
                        html.P("""
                            Este proyecto se enfoca en el desarrollo y la evaluación de un modelo de Machine Learning 
                            para predecir las anomalías mensuales de la temperatura superficial a escala global. 
                            Los objetivos principales son:
                            """, style=text_style),
                        html.Ul([
                            html.Li("Construir un modelo predictivo robusto utilizando datos históricos desde 1900.", style=text_style),
                            html.Li("Identificar los factores temporales y espaciales más influyentes en la variabilidad de las anomalías de temperatura.", style=text_style),
                            html.Li("Evaluar el rendimiento del modelo y comprender sus capacidades y limitaciones.", style=text_style),
                            html.Li("Proporcionar una plataforma interactiva (este dashboard) para visualizar los datos, la metodología y los resultados del análisis.", style=text_style)
                        ], style={'paddingLeft': '20px'}),
                    ], style={'marginBottom': '20px'}),
                    
                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),

                    # Bloque 3: Metodología y Análisis Realizado
                    html.Div([ # Puedes añadir className='info-card' aquí
                        html.H5("Metodología y Análisis Realizado", style={'color': COLORS['highlight'], 'marginTop': '20px', 'marginBottom': '10px'}),
                        html.P("""
                            Se utilizó un conjunto de datos de anomalías de temperatura que abarca desde 1900 hasta 2024. 
                            El proceso incluyó una exhaustiva limpieza y preprocesamiento de datos, seguido de una 
                            cuidadosa ingeniería de características para capturar la dependencia temporal (medias móviles, 
                            valores rezagados), estacionalidad y tendencias. Se consideraron también factores espaciales 
                            como la latitud, longitud e interacciones.
                            """, style=text_style),
                        html.P("""
                            Se seleccionó el algoritmo XGBoost, conocido por su alto rendimiento en problemas de regresión. 
                            Sus hiperparámetros fueron optimizados mediante la técnica de `RandomizedSearchCV` con validación 
                            cruzada. El conjunto de datos (previamente muestreado a 8 millones de registros) se dividió 
                            temporalmente, utilizando el 80% para entrenamiento (datos de ~1900 a ~2001) y el 20% para 
                            prueba (datos de ~2001 a ~2024), asegurando una evaluación realista del modelo.
                            """, style=text_style),
                    ], style={'marginBottom': '20px'}),

                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),

                    # Bloque 4: Principales Hallazgos
                    html.Div([ # Puedes añadir className='info-card' aquí
                        html.H5("Principales Hallazgos", style={'color': COLORS['highlight'], 'marginTop': '20px', 'marginBottom': '10px'}),
                        dcc.Markdown("""
                            El modelo XGBoost final demostró una capacidad predictiva notable, alcanzando en el conjunto 
                            de prueba un Error Absoluto Medio (MAE) de aproximadamente **0.52 °C** y un 
                            Coeficiente de Determinación (R²) del **68.13%**. Estos resultados indican que el modelo 
                            explica una porción significativa de la varianza en las anomalías de temperatura.
                            """, style=text_style),
                        html.P("""
                            El análisis de importancia de características reveló que las variables más influyentes son 
                            aquellas relacionadas con la historia reciente de la temperatura, como la media móvil de los 
                            últimos 3 meses, el valor del mes anterior y la media móvil de los últimos 12 meses.
                            """, style=text_style),
                    ], style={'marginBottom': '20px'}),
                    
                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),
                    
                    html.P("""
                        Le invitamos a explorar las diferentes secciones de este dashboard para profundizar en la 
                        metodología, los datos exploratorios y los resultados detallados del modelo.
                        """, style={**text_style, 'fontStyle': 'italic', 'textAlign': 'center', 'marginTop': '10px'})

                ], md=12) # <- Cambiado a md=12 para ocupar todo el ancho
            ])
        ]
        
        try:
            return create_section("Introducción General", contenido_introduccion)
        except Exception as e:
            print(f"ERROR al crear la sección de Introducción: {e}")
            return html.Div(f"Error al generar contenido para Introducción: {str(e)}")

        
    elif tab == "tab-contexto":
        print("DEBUG: Entrando en el bloque de 'tab-contexto'")
        # ... (tu código original para tab-contexto)
        return create_section("Contexto Científico", [
            html.Div([
                html.P("El cambio climático representa uno de los desafíos globales más críticos del siglo XXI, con implicaciones directas en:", style=text_style),
                html.Ul([
                    html.Li("Estabilidad de ecosistemas naturales", style=text_style),
                    html.Li("Seguridad alimentaria global", style=text_style),
                    html.Li("Salud poblacional", style=text_style),
                    html.Li("Economías nacionales", style=text_style)
                ], style={'marginBottom': '25px', 'paddingLeft': '20px'}),
                
                html.H4("Base de Datos: Berkeley Earth Surface Temperature (BEST)", style={
                    'color': COLORS['accent'],
                    'borderBottom': f'2px solid {COLORS["highlight"]}',
                    'paddingBottom': '10px',
                    'marginBottom': '20px'
                }),
                
                dbc.Row([
                    dbc.Col([
                        html.H5("Características Principales", style={'color': COLORS['accent']}),
                        html.Ul([
                            html.Li("Período temporal: 1850-2025", style=text_style),
                            html.Li("Resolución espacial: 1° × 1°", style=text_style),
                            html.Li("Frecuencia: Mensual", style=text_style),
                            html.Li("Cobertura: Global", style=text_style)
                        ], style={'paddingLeft': '20px'})
                    ], md=6),
                    
                    dbc.Col([
                        html.H5("Variables Clave", style={'color': COLORS['accent']}),
                        dbc.Table([
                            html.Thead(html.Tr([
                                html.Th("Variable", style={'color': COLORS['accent'], 'backgroundColor': '#2c3e50'}),
                                html.Th("Descripción", style={'color': COLORS['accent'], 'backgroundColor': '#2c3e50'})
                            ])),
                            html.Tbody([
                                html.Tr([
                                    html.Td("temperature", style={'color': '#e0f2fe', 'backgroundColor': '#243447'}),
                                    html.Td("Anomalía térmica (°C)", style={'color': '#e0f2fe', 'backgroundColor': '#243447'})
                                ]),
                                html.Tr([
                                    html.Td("climatology", style={'color': '#e0f2fe', 'backgroundColor': '#243447'}),
                                    html.Td("Climatología mensual de referencia", style={'color': '#e0f2fe', 'backgroundColor': '#243447'})
                                ]),
                                html.Tr([
                                    html.Td("land_mask", style={'color': '#e0f2fe', 'backgroundColor': '#243447'}),
                                    html.Td("Máscara tierra/océano (0-1)", style={'color': '#e0f2fe', 'backgroundColor': '#243447'})
                                ])
                            ])
                        ], bordered=True, style={
                            'backgroundColor': '#1e2a38',
                            'borderColor': COLORS['accent'],
                            'borderRadius': '8px',
                            'overflow': 'hidden'
                        })
                    ], md=6)
                ], className="mb-4"),
                
                html.H5("Relevancia Científica", style={'color': COLORS['accent'], 'marginTop': '20px'}),
                html.P("""
                    Este dataset permite el análisis de patrones espacio-temporales del calentamiento global mediante:
                    """, style=text_style),
                html.Ul([
                    html.Li("Identificación de tendencias seculares", style=text_style),
                    html.Li("Detección de anomalías regionales", style=text_style),
                    html.Li("Validación de modelos climáticos", style=text_style)
                ], style={'paddingLeft': '20px'})
            ], style={'padding': '20px', 'backgroundColor': COLORS['card_background'], 'borderRadius': '10px'})
        ])
    
    elif tab == "tab-problema":
        print("DEBUG: Entrando en el bloque de 'tab-problema'")
        # ... (tu código original para tab-problema)
        return create_section("Planteamiento del Problema", [
            html.Div([
                html.P("""
                    El aumento de eventos climáticos extremos por el calentamiento global demanda modelos predictivos 
                    precisos para anticipar anomalías térmicas —desviaciones críticas respecto a patrones históricos—, 
                    cuya complejidad radica en la interacción de factores naturales y humanos.
                    """, 
                    style=text_style
                ),
                html.Div([
                    html.Span("¿Cómo evolucionarán las anomalías térmicas ", style={'color': COLORS['text']}),
                    html.Span("y qué factores ", style={'color': COLORS['text']}),
                    html.Span("geográficos/estacionales ", style={'color': COLORS['highlight'], 'fontWeight': 'bold'}),
                    html.Span("las impulsarán?", style={'color': COLORS['text']}),
                ], style={'textAlign': 'center', 'margin': '25px 0', 'fontSize': '1.2rem', 'padding': '15px', 'backgroundColor': COLORS['card_background'], 'borderRadius': '8px'}),
                html.P("Desafíos clave identificados:", style={**text_style, 'marginTop': '20px', 'fontWeight':'bold'}),
                html.Ul([
                    html.Li("Limitaciones en modelos predictivos de alta resolución espaciotemporal.", style=text_style),
                    html.Li("Dificultad para desacoplar impactos naturales vs. antropogénicos en las anomalías.", style=text_style),
                    html.Li("Necesidad de proyecciones regionalizadas para la toma de decisiones y acciones concretas de adaptación.", style=text_style)
                ], style={
                    'color': COLORS['text'], 
                    'borderLeft': f'3px solid {COLORS["accent"]}', 
                    'paddingLeft': '20px',
                    'listStyleType': 'square'
                })
            ], style={'padding': '15px', 'backgroundColor': COLORS['card_background'], 'borderRadius': '10px'})
        ])
    
    elif tab == 'tab-objetivos':
        print("DEBUG: Entrando en el bloque de 'tab-objetivos'")
        # ... (tu código original para tab-objetivos)
        return create_section("Objetivos y Justificación", [
            html.Div([
                html.Div([
                    html.H4("Objetivo General", style={'color': COLORS['accent'], 'marginBottom': '10px'}),
                    html.P("""
                        Desarrollar un modelo predictivo espacio-temporal para proyectar anomalías térmicas globales 
                        basado en datos históricos, identificando los factores más influyentes y evaluando su 
                        rendimiento para apoyar la comprensión del cambio climático.
                    """, style=text_style)
                ], style={'marginBottom': '30px', 'padding': '15px', 'backgroundColor': COLORS['card_background'], 'borderRadius': '8px'}),
                html.Div([
                    html.H4("Objetivos Específicos", style={'color': COLORS['accent'], 'marginBottom': '20px'}),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H5("1. Análisis de Datos", style={'color': COLORS['highlight'], 'marginBottom': '15px'}),
                                html.P("Procesar y analizar datos climáticos históricos (desde 1900) para identificar patrones espaciotemporales relevantes, con foco en la ingeniería de características que capturen interacciones tierra-océano, tendencias y variabilidad estacional.", 
                                       style=text_style)
                            ], className='obj-card info-card'),
                            md=4
                        ),
                        dbc.Col(
                            html.Div([
                                html.H5("2. Modelado Predictivo", style={'color': COLORS['highlight'], 'marginBottom': '15px'}),
                                html.P("Diseñar, entrenar y optimizar un modelo de regresión basado en XGBoost que capture relaciones no lineales en las series temporales de anomalías de temperatura, incorporando las características geo-referenciadas, temporales y climáticas generadas.", 
                                       style=text_style)
                            ], className='obj-card info-card'),
                            md=4
                        ),
                        dbc.Col(
                            html.Div([
                                html.H5("3. Evaluación Rigurosa", style={'color': COLORS['highlight'], 'marginBottom': '15px'}),
                                html.P("Evaluar la capacidad predictiva del modelo XGBoost en la estimación de anomalías de temperatura utilizando métricas cuantitativas (MAE, RMSE, R²) y análisis cualitativos (visualización de errores y predicciones), analizando su robustez y generalización.", 
                                       style=text_style)
                            ], className='obj-card info-card'),
                            md=4
                        )
                    ], className="g-4")
                ], style={'marginBottom': '30px'}),
                html.Div([
                    html.H4("Justificación", style={'color': COLORS['accent'], 'marginBottom': '10px'}),
                    html.Div([
                        html.P("""
                            La predicción precisa de anomalías térmicas es fundamental para la planificación y 
                            adaptación al cambio climático. Este proyecto se justifica por la necesidad de:
                            """, style=text_style),
                        html.Ul([
                            html.Li("Mejorar la comprensión de los factores que modulan las anomalías de temperatura.", style=text_style),
                            html.Li("Proporcionar herramientas basadas en Machine Learning para el análisis climático.", style=text_style),
                            html.Li("Generar información útil que pueda apoyar la toma de decisiones informadas en diversos sectores.", style=text_style)
                        ], style={'marginBottom': '15px', 'paddingLeft': '20px'}),
                        html.P("""
                            Este proyecto aporta innovación mediante la aplicación de XGBoost con una ingeniería 
                            de características detallada sobre el dataset Berkeley Earth, y la creación de un dashboard 
                            interactivo para la diseminación de los resultados.
                            """, style=text_style)
                    ], style={'backgroundColor': COLORS['card_background'], 'padding': '20px', 'borderRadius': '10px'})
                ])
            ], style={'padding': '15px'})
        ])
    
    elif tab == "tab-teorico":
        print("DEBUG: Entrando en el bloque de 'tab-teorico'")
        # ... (tu código original para tab-teorico)
        return create_section("Marco Teórico", [
            html.Div([
                html.Div([
                    html.H5("1. Anomalías de Temperatura", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                    html.P("Las anomalías representan la diferencia entre la temperatura observada y un valor medio de referencia (climatología) para un periodo base. Este enfoque elimina efectos estacionales o regionales persistentes, permitiendo comparaciones consistentes entre épocas y lugares distintos. Son fundamentales para detectar tendencias de calentamiento global.", style=text_style),
                    html.P(["Referencias: NOAA (2021), IPCC Sixth Assessment Report (2021). Ver también: ", html.A("NASA GISS Surface Temperature Analysis", href="https://data.giss.nasa.gov/gistemp/", target="_blank")], className='referencia', style=text_style)
                ], className='info-card'),
                html.Div([
                    html.H5("2. Climatología y su Rol en el Modelo", style={'color': COLORS['accent'], 'marginBottom': '15px', 'marginTop': '30px'}),
                    html.P("La climatología mensual por celda espacial forma un tensor tridimensional que captura patrones estacionales típicos para cada ubicación. En este proyecto, la variable 'climatology' se utilizó como una característica predictora, permitiendo que el modelo aprenda cómo las desviaciones (anomalías) se relacionan con las condiciones promedio esperadas para un mes y lugar específico.", style=text_style),
                    html.P(["Fuente: Wilks, D. S. (2019). Statistical Methods in the Atmospheric Sciences. Elsevier.", html.A(" Más sobre climatologías", href="https://www.ncdc.noaa.gov/monitoring-references/dyk/climate-normals", target="_blank")], className='referencia', style=text_style)
                ], className='info-card', style={'marginTop': '30px'}),
                html.Div([
                    html.H5("3. Dependencia Espacio-Temporal y XGBoost", style={'color': COLORS['accent'], 'marginBottom': '15px', 'marginTop': '30px'}),
                    html.P("Los datos climáticos presentan inherentemente autocorrelación espacial (lugares cercanos se parecen) y temporal (momentos cercanos se parecen). XGBoost, al ser un modelo basado en árboles, puede manejar eficazmente estas interdependencias y la colinealidad entre features sin necesidad de transformaciones complejas, gracias a su proceso de construcción aditiva y la selección de variables en cada división de árbol.", style=text_style),
                    html.P(["Referencia: Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. ", html.A("Documentación de XGBoost", href="https://xgboost.readthedocs.io/", target="_blank")], className='referencia', style=text_style)
                ], className='info-card', style={'marginTop': '30px'})
            ], style={'padding': '15px'})
        ])
    
    elif tab == 'tab-metodologia':
        print("DEBUG: Entrando en el bloque de 'tab-metodologia'")
        final_mae_metodologia = 0.5249 # Usar un nombre diferente si es el mismo valor que en resultados
        final_r2_metodologia = 0.6813
        return create_section("Metodología", [
            dcc.Tabs(id='metodologia-tabs', value='subtab-definicion-problema', children=[ 
                dcc.Tab(label='a. Definición del Problema', value='subtab-definicion-problema', className='custom-tab', children=[
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.H5("Definición del Problema a Resolver", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                    html.Div([
                                        html.P("Tipo de problema: Regresión aplicada a series de tiempo con componente espacial.", style={'fontWeight': 'bold', 'color': COLORS['highlight']}),
                                        html.P("Variable objetivo o de interés: Anomalía de temperatura (desviación respecto a la climatología de referencia).", style={'fontWeight': 'bold', 'color': COLORS['highlight'], 'marginTop': '15px'}),
                                        html.P("Este proyecto busca desarrollar un modelo predictivo para las anomalías de temperatura global. Utilizando datos históricos desde 1900, el modelo pretende capturar las complejas interacciones entre la evolución temporal y la distribución espacial de las temperaturas para entender y predecir estas anomalías con la mayor precisión posible.", style=text_style),
                                        html.P("Relación modelada:", style={'fontWeight': 'bold', 'color': COLORS['highlight'], 'marginTop': '20px'}),
                                        html.Ul([
                                            html.Li("Factores temporales: Se modela la dependencia temporal a través de características rezagadas (lags de 1, 3 y 12 meses), estadísticas móviles (medias y desviaciones estándar de 3 y 12 meses), diferencias interanuales, el año como tendencia y la estacionalidad mensual (transformada con seno y coseno).", style=text_style),
                                            html.Li("Factores espaciales: Se incluyen las coordenadas (latitud, longitud), una máscara tierra-océano y se exploran interacciones entre la latitud y la estacionalidad.", style=text_style),
                                            html.Li("Contexto climático: Se utiliza la climatología base mensual para normalizar y contextualizar las anomalías.", style=text_style),
                                        ], style={'paddingLeft': '20px'}),
                                        html.P("El objetivo es construir un modelo robusto que explique la variabilidad observada y sirva como base para futuros análisis climáticos.", style=text_style)
                                    ], className='info-card')
                                ])
                            ], md=12),
                        ])
                    ], style={'padding': '15px'})
                ]),
                dcc.Tab(label='b. Preparación de Datos', value='subtab-preparacion-datos',className='custom-tab', children=[
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.H5("Fuente y Limpieza Inicial", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                    html.P("Se partió de datos de anomalías de temperatura en formato NetCDF. Tras una exploración inicial, se aplicó una interpolación temporal y espacial para manejar valores ausentes, aunque persistieron algunos NaNs, especialmente en zonas polares y periodos muy antiguos.", style=text_style),
                                    html.H5("Preprocesamiento para el Modelo", style={'color': COLORS['accent'], 'marginBottom': '15px', 'marginTop': '20px'}),
                                    html.P("Para el modelado, se seleccionaron datos desde 1900. Se generaron las características temporales y espaciales descritas anteriormente (lags, rolling stats, interacciones, etc.). Se imputó la 'climatology' con la mediana global y se eliminaron las filas iniciales de cada serie que contenían NaNs debido a la generación de lags (principalmente el lag de 12 meses).", style=text_style),
                                    html.H5("Muestreo", style={'color': COLORS['accent'], 'marginBottom': '15px', 'marginTop': '20px'}),
                                    html.P("Dado el gran volumen de datos (más de 90 millones de filas tras la limpieza inicial), se realizó un muestreo aleatorio simple para obtener un conjunto manejable de 8,000,000 de filas. Esta muestra se utilizó para la optimización de hiperparámetros y el entrenamiento final.", style=text_style),
                                ], className='info-card', style={'marginBottom': '30px'})
                            ])
                        ]),
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.H5("División en Entrenamiento y Prueba", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                    html.P("El conjunto de datos muestreado (8M filas) se ordenó cronológicamente y se dividió siguiendo un enfoque temporal: 80% para entrenamiento (aproximadamente 1900-2001) y 20% para prueba (aproximadamente 2001-2024). Esta división asegura que el modelo se evalúe sobre su capacidad para predecir datos no vistos en el futuro, replicando un escenario de pronóstico.", style=text_style),
                                ], className='info-card')
                            ])
                        ])
                    ], style={'padding': '15px'})
                ]),
                dcc.Tab(label='c. Selección del Modelo', value='subtab-seleccion-modelo', className='custom-tab', children=[
                     html.Div([
                        html.H5("Selección del Modelo", style={'color': COLORS['accent'], 'marginBottom': '20px'}),
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        html.H6("Modelo seleccionado", style={'color': COLORS['highlight'], 'marginBottom': '10px'}),
                                        html.P("Se seleccionó XGBoost (Extreme Gradient Boosting) como algoritmo de regresión. Este modelo es un ensamblado de árboles de decisión altamente eficiente y eficaz para problemas tabulares complejos.", style=text_style)
                                    ], className='info-card', style={'marginBottom': '20px'}),
                                    html.Div([
                                        html.H6("Justificación", style={'color': COLORS['highlight'], 'marginBottom': '10px'}),
                                        html.P("XGBoost fue elegido por su robustez, su capacidad para capturar relaciones no lineales complejas y su manejo interno de valores faltantes (aunque optamos por eliminarlos). Su popularidad y éxito en competiciones se deben a su rendimiento y a las técnicas de regularización (L1 y L2) que incorpora para mitigar el sobreajuste.", style=text_style),
                                        html.P("Se alimenta con un conjunto rico de características espaciales, temporales, rezagadas y de interacción, permitiéndole construir un modelo predictivo spatio-temporal.", style=text_style)
                                    ], className='info-card')
                                ])
                            ], md=6),
                            dbc.Col([
                                dcc.Markdown('''
                                #### Representación matemática
                                XGBoost estima la anomalía de temperatura \\(\\hat{y}_i\\) como una suma de árboles:
                                $$
                                \\hat{y}_i = \\sum_{k=1}^K f_k(x_i), \\quad f_k \\in \\mathcal{F}
                                $$
                                Minimizando una función objetivo regularizada:
                                $$
                                L(\\phi) = \\sum_{i=1}^n l(y_i, \\hat{y}_i) + \\sum_{k=1}^K \\left( \\gamma T_k + \\frac{1}{2} \\lambda \\|w_k\\|^2 + \\alpha \\|w_k\\|_1 \\right)
                                $$
                                donde \\(l\\) es la función de pérdida (error cuadrático), \\(f_k\\) es un árbol, \\(T_k\\) el número de hojas, y \\(\\gamma, \\lambda, \\alpha\\) son hiperparámetros de regularización.
                                ''', mathjax=True, style={**text_style, 'backgroundColor': COLORS['card_background'], 'padding': '20px', 'borderRadius': '10px', 'border': f'1px solid {COLORS["accent"]}'})
                            ], md=6)
                        ])
                    ], style={'padding': '15px'})
                ]),
                dcc.Tab(label='d. Entrenamiento y Evaluación', value='subtab-entrenamiento', className='custom-tab', children=[
                    html.Div([
                        html.H4("Entrenamiento, Optimización y Criterios de Evaluación del Modelo", # Título más general para la sub-pestaña
                                style={'textAlign': 'center', 'color': COLORS['accent'], 'marginBottom': '25px'}),
                        dbc.Row([
                            # Columna Izquierda: Proceso de Entrenamiento y Optimización
                            dbc.Col([
                                html.Div([
                                    html.H5("Proceso de Entrenamiento y Optimización de Hiperparámetros", style={'color': COLORS['highlight'], 'marginBottom': '15px'}),
                                    html.P("""
                                        El modelo XGBoost seleccionado fue entrenado utilizando el conjunto de datos de entrenamiento, 
                                        que comprende el 80% de la muestra de 8 millones de registros (aproximadamente 6.4 millones de observaciones). 
                                        Este conjunto contiene todas las características espaciales, temporales, rezagadas y de interacción 
                                        previamente generadas.
                                        """, style=text_style),
                                    html.P("""
                                        Para determinar la configuración óptima del modelo, se empleó la técnica de búsqueda aleatoria de 
                                        hiperparámetros (`RandomizedSearchCV`). Se exploró un espacio de búsqueda predefinido para 
                                        hiperparámetros cruciales como el número de estimadores (`n_estimators`), la tasa de aprendizaje 
                                        (`learning_rate`), la profundidad máxima de los árboles (`max_depth`), las fracciones de muestreo 
                                        de datos (`subsample`) y de características (`colsample_bytree`), el peso mínimo por hijo 
                                        (`min_child_weight`), el parámetro de regularización gamma (`gamma`), y los coeficientes de 
                                        regularización L1 (`reg_alpha`) y L2 (`reg_lambda`).
                                        """, style=text_style),
                                    html.P("""
                                        Se realizaron 20 combinaciones de hiperparámetros, evaluando cada una mediante validación 
                                        cruzada de 3 pliegues (`cv=3`) sobre el conjunto de entrenamiento. El objetivo de esta 
                                        búsqueda fue minimizar el Error Absoluto Medio (MAE), seleccionando así la combinación 
                                        que ofreciera el mejor rendimiento promedio en las validaciones.
                                        """, style=text_style)
                                ], className='info-card')
                            ], md=6),

                            # Columna Derecha: Métricas y Validación Final
                            dbc.Col([
                                html.Div([
                                    html.H5("Evaluación y Validación Final del Modelo", style={'color': COLORS['highlight'], 'marginBottom': '15px'}),
                                    html.P("""
                                        Una vez identificados los mejores hiperparámetros, el modelo XGBoost final se reentrenó 
                                        utilizando la totalidad del conjunto de entrenamiento. Posteriormente, su capacidad de 
                                        generalización y rendimiento predictivo se evaluó de forma rigurosa sobre el conjunto 
                                        de prueba (el 20% restante de los datos, no utilizado durante el entrenamiento ni la 
                                        optimización).
                                        """, style=text_style),
                                    html.P(
                                        "Las métricas clave utilizadas para esta evaluación final fueron:",
                                        style=text_style),
                                    html.Ul([
                                        html.Li([
                                            html.Span("Error Absoluto Medio (MAE): ", style={'fontWeight': 'bold', 'color': 'white'}),
                                            html.Span("Mide la magnitud promedio de los errores en las predicciones, sin considerar su dirección. Proporciona una medida directa del error en las unidades de la variable objetivo (°C).", style=text_style)
                                        ]),
                                        html.Li([
                                            html.Span("Raíz del Error Cuadrático Medio (RMSE): ", style={'fontWeight': 'bold', 'color': 'white'}),
                                            html.Span("Similar al MAE, pero penaliza en mayor medida los errores grandes debido al término cuadrático. También se expresa en las unidades de la variable objetivo (°C).", style=text_style)
                                        ]),
                                        html.Li([
                                            html.Span("Coeficiente de Determinación (R²): ", style={'fontWeight': 'bold', 'color': 'white'}),
                                            html.Span("Indica la proporción de la varianza en la variable objetivo que es predecible a partir de las características. Un valor cercano a 1 indica un mejor ajuste del modelo.", style=text_style)
                                        ])
                                    ], style={'paddingLeft': '20px'}),
                                    html.P("""
                                        La comparación del rendimiento en los conjuntos de entrenamiento y prueba permitió 
                                        diagnosticar el grado de sobreajuste y confirmar la capacidad del modelo para 
                                        generalizar a datos nuevos y no vistos.
                                        """, style=text_style)
                                ], className='info-card')
                            ], md=6)
                        ])
                    ], style={'padding': '15px'})
                ])
            ])
        ])

    elif tab == "tab-resultados":
        print("DEBUG: Entrando en el bloque de 'tab-resultados'")
        final_mae_resultados = 0.5249 # Usar un nombre diferente
        final_rmse_resultados = 0.9141
        final_r2_resultados = 0.6813
        # ... (tu código completo para tab-resultados, usando el contenido que te proporcioné antes)
        return create_section("Resultados y Análisis", [
            dcc.Tabs(
                id='tabs-resultados-internas', # ID diferente para estas sub-pestañas
                value='subtab-resultados-eda', 
                className='custom-tabs',
                children=[
                    dcc.Tab(label='a. EDA', value='subtab-resultados-eda', className='custom-tab', children=[
                        html.Div([
                            html.H4("Análisis Exploratorio de Datos (EDA)", style={'textAlign': 'center', 'color': COLORS['accent'], 'marginBottom': '25px'}),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.H5("Estadísticas Descriptivas (Datos Originales)", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                        html.P("A continuación se muestran las estadísticas descriptivas para la variable 'temperature' antes del muestreo y filtrados finales. Esto nos da una idea general de la distribución de las anomalías:", style=text_style),
                                        dbc.Table([
                                            html.Tbody([
                                                html.Tr([html.Td("Count"), html.Td(f"{1.202817e+08:,.0f}")]),
                                                html.Tr([html.Td("Mean"), html.Td(f"{7.450250e-02:.4f} °C")]),
                                                html.Tr([html.Td("Std"), html.Td(f"{1.263593e+00:.4f} °C")]),
                                                html.Tr([html.Td("Min"), html.Td(f"{-1.938505e+01:.4f} °C")]),
                                                html.Tr([html.Td("1%"), html.Td(f"{-3.810158e+00:.4f} °C")]),
                                                html.Tr([html.Td("25% (Q1)"), html.Td(f"{-5.642971e-01:.4f} °C")]),
                                                html.Tr([html.Td("50% (Median)"), html.Td(f"{-2.051336e-03:.4f} °C")]),
                                                html.Tr([html.Td("75% (Q3)"), html.Td(f"{6.133333e-01:.4f} °C")]),
                                                html.Tr([html.Td("99%"), html.Td(f"{4.800029e+00:.4f} °C")]),
                                                html.Tr([html.Td("Max"), html.Td(f"{2.223275e+01:.4f} °C")]),
                                            ])
                                        ], bordered=True, striped=True, hover=True, style={
                                            'backgroundColor': '#1e2a38', 'borderColor': COLORS['accent'],
                                            'borderRadius': '8px', 'overflow': 'hidden', 'color': '#e0f2fe'
                                        }),
                                        html.P("La media cercana a cero es esperada al trabajar con anomalías. La desviación estándar (1.26 °C) y los amplios rangos (Min/Max) indican una variabilidad considerable.", style=text_style),
                                    ], className='info-card')
                                ], md=4), 
                                dbc.Col([
                                    html.H5("Análisis Visual del EDA", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                    html.P("Los gráficos exploratorios revelan patrones clave:", style=text_style),
                                    dbc.Row([
                                        dbc.Col([html.P("Distribución:", style=text_style), html.Img(src='/assets/histograma.png', className='img-fluid rounded shadow')], md=6),
                                        dbc.Col([html.P("Descomposición Temporal:", style=text_style), html.Img(src='/assets/descomposición.png', className='img-fluid rounded shadow')], md=6),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([html.P("Tendencia Global:", style=text_style), html.Img(src='/assets/tendencia.png', className='img-fluid rounded shadow')], md=6, style={'marginTop': '20px'}),
                                        dbc.Col([html.P("Correlaciones (Ejemplo):", style=text_style), html.Img(src='/assets/correlacion.png', className='img-fluid rounded shadow')], md=6, style={'marginTop': '20px'}),
                                    ]),
                                    html.P("El histograma muestra una distribución aproximadamente normal centrada en cero. La descomposición revela una clara tendencia ascendente y patrones estacionales. El gráfico de correlación (si es de features) ayuda a entender las relaciones iniciales.", style={**text_style, 'marginTop': '20px'})
                                ], md=8) 
                            ])
                        ], style={'padding': '15px'})
                    ]),
                    dcc.Tab(label='b. Visualización del Modelo', value='subtab-resultados-modelo', className='custom-tab', children=[
                        html.Div([
                            html.H4("Visualización de Resultados del Modelo", style={'textAlign': 'center', 'color': COLORS['accent'], 'marginBottom': '25px'}),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.H5("Importancia de las Características", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                        html.Img(src='/assets/feature_importance_enhanced.png', className='img-fluid rounded shadow'),
                                        html.P("La importancia de características revela qué variables influyen más en las predicciones. Las medias móviles y lags temporales son dominantes, subrayando la dependencia con la historia reciente y anual.", style=text_style)
                                    ], className='info-card')
                                ], md=6),
                                dbc.Col([
                                    html.Div([
                                        html.H5("Valores Reales vs. Predichos (Test Set)", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                        html.Img(src='/assets/predictions_vs_actual_enhanced.png', className='img-fluid rounded shadow'),
                                        html.P("Compara valores reales y predichos. Idealmente, los puntos se alinean con la diagonal. Se observa buena correlación, con dispersión en extremos, y la mayoría de puntos cerca de la línea ideal.", style=text_style)
                                    ], className='info-card')
                                ], md=6),
                            ], style={'marginTop': '20px'}),
                            dbc.Row([
                                dbc.Col(html.Img(src='/assets/residuals_vs_predicted.png', className='img-fluid rounded shadow', style={'marginTop':'20px'}), md=6),
                                dbc.Col(html.Img(src='/assets/map_mae_error.png', className='img-fluid rounded shadow', style={'marginTop':'20px'}), md=6),
                            ], style={'marginTop':'20px'}),
                            dbc.Row([
                                dbc.Col(html.Img(src='/assets/timeseries_mae_error.png', className='img-fluid rounded shadow', style={'marginTop':'20px'}), md=12)
                            ])
                        ], style={'padding': '15px'})
                    ]),
                    dcc.Tab(label='c. Métricas de Desempeño', value='subtab-resultados-metricas', className='custom-tab', children=[
                         html.Div([
                            html.H4("Métricas de Desempeño del Modelo Final", style={'textAlign': 'center', 'color': COLORS['accent'], 'marginBottom': '25px'}),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.H5("Interpretación de las Métricas", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                        html.P(f"El Error Absoluto Medio (MAE) de {final_mae_resultados:.2f} °C indica que, en promedio, las predicciones se desvían ~0.52 °C del valor real, un nivel de precisión considerable.", style=text_style),
                                        html.P(f"El Coeficiente de Determinación (R²) de {final_r2_resultados:.2%} significa que el modelo explica el 68.13% de la varianza en las anomalías del conjunto de prueba, un resultado robusto.", style=text_style),
                                        html.P("La brecha entre métricas de entrenamiento (R² ≈ 79.6%) y prueba (R² ≈ 68.1%) sugiere un grado de sobreajuste, aunque el modelo generaliza razonablemente.", style=text_style)
                                    ], className='info-card')
                                ], md=6),
                                dbc.Col([
                                    html.Div([
                                        html.H5("Tabla Resumen (Conjunto de Prueba)", style={'color': COLORS['accent'], 'marginBottom': '20px'}),
                                        dbc.Table([
                                            html.Thead(html.Tr([html.Th("Métrica"), html.Th("Valor")]), style={'color': COLORS['accent']}),
                                            html.Tbody([
                                                html.Tr([html.Td("MAE"), html.Td(f"{final_mae_resultados:.4f} °C")]),
                                                html.Tr([html.Td("RMSE"), html.Td(f"{final_rmse_resultados:.4f} °C")]),
                                                html.Tr([html.Td("R²"), html.Td(f"{final_r2_resultados:.4f}")])
                                            ])
                                        ], bordered=True, striped=True, hover=True, className='metricas-table',
                                        style={'backgroundColor': '#1e2a38', 'borderColor': COLORS['accent'], 'borderRadius': '8px', 'color': '#e0f2fe'})
                                    ], className='info-card')
                                ], md=6)
                            ])
                        ], style={'padding': '15px'})
                    ]),
                    dcc.Tab(label='d. Limitaciones', value='subtab-resultados-limitaciones', className='custom-tab', children=[
                        html.Div([
                            html.H4("Limitaciones y Consideraciones (Contexto Resultados)", style={'textAlign': 'center', 'color': COLORS['accent'], 'marginBottom': '25px'}),
                            html.Div([
                                html.H5("Limitaciones del Proyecto", style={'color': COLORS['accent'], 'marginBottom': '15px'}),
                                html.Ul([
                                    html.Li("Complejidad en la Fusión de Datos Inicial: Dificultades al integrar datos interpolados con el formato NetCDF original.", style=text_style),
                                    html.Li("Muestreo: Se usó una muestra (8M filas, ~9% del total). Un dataset completo podría alterar resultados, con mayor coste computacional.", style=text_style),
                                    html.Li("Validación Cruzada: CV estándar en RandomizedSearchCV. CV temporal sería más pura pero costosa.", style=text_style),
                                    html.Li("Sobreajuste Residual: Aún existe una brecha entre rendimiento de entrenamiento y prueba.", style=text_style),
                                    html.Li("Complejidad Climática No Modelada: Factores como ENSO, aerosoles, etc., no fueron incluidos.", style=text_style),
                                ], style={'paddingLeft': '20px'}),
                                html.H5("Mejoras Futuras", style={'color': COLORS['accent'], 'marginBottom': '15px', 'marginTop': '20px'}),
                                html.Ul([
                                    html.Li("Explorar modelos más complejos (LSTMs, Transformers).", style=text_style),
                                    html.Li("Incluir más variables exógenas (ENSO, CO2).", style=text_style),
                                    html.Li("Implementar validación cruzada temporal más robusta.", style=text_style),
                                    html.Li("Análisis de errores más profundo.", style=text_style),
                                ], style={'paddingLeft': '20px'})
                            ], className='info-card')
                        ], style={'padding': '15px'})
                    ])
                ]
            )
        ])

    elif tab == "tab-conclusiones":
       

        contenido_conclusiones = [
            dbc.Row([
                dbc.Col([ 
                    html.H3("Conclusiones y Síntesis Final", 
                            style={'color': COLORS['accent'], 'textAlign': 'center', 'marginBottom': '25px'}),
                    
                    # Bloque 1: Resumen inicial
                    html.Div([
                        html.P("""
                            Este proyecto demostró con éxito la capacidad de un modelo XGBoost para predecir las 
                            anomalías de temperatura global, alcanzando una explicación de la varianza del 
                            aproximadamente 68.13% (R²) en el conjunto de datos de prueba.
                            """, style=text_style),
                    ], style={'marginBottom': '20px'}),

                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),
                    
                    # Bloque 2: Principales Descubrimientos
                    html.Div([ 
                        html.H5("Principales Descubrimientos Clave:", style={'color': COLORS['highlight'], 'marginTop': '20px', 'marginBottom': '10px'}),
                        html.Ul([
                            html.Li("""
                                La historia reciente y anual de la temperatura (capturada mediante valores rezagados 
                                y medias móviles de 3 y 12 meses) se consolidó como el factor más determinante 
                                para las predicciones del modelo.
                                """, style=text_style),
                            html.Li("""
                                El modelo evidencia una generalización razonable a periodos no observados previamente, 
                                aunque se identificó una variabilidad en la precisión espacial y un remanente de 
                                sobreajuste que podría explorarse más a fondo.
                                """, style=text_style),
                        ], style={'paddingLeft': '20px'}), 
                    ], style={'marginBottom': '20px'}),

                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),

                    # Bloque 3: Relevancia e Implicaciones
                    html.Div([
                        html.H5("Relevancia e Implicaciones:", style={'color': COLORS['highlight'], 'marginTop': '20px', 'marginBottom': '10px'}),
                        html.Ul([
                            html.Li("""
                                Los resultados obtenidos validan la efectividad del Machine Learning, específicamente 
                                XGBoost, para abordar la modelización de fenómenos climáticos complejos como las 
                                anomalías de temperatura.
                                """, style=text_style),
                            html.Li("""
                                La identificación de predictores clave, como la persistencia temporal, no solo mejora 
                                la predicción sino que también contribuye a la comprensión de los factores que impulsan 
                                las anomalías a corto y medio plazo, sentando una base para futuros estudios de impacto.
                                """, style=text_style),
                        ], style={'paddingLeft': '20px'}),
                    ], style={'marginBottom': '20px'}),

                    html.Hr(style={'borderColor': COLORS.get('accent_subtle', COLORS['accent']), 'margin': '20px 0'}),
                    
                    html.P("""
                        En conclusión, el modelo desarrollado representa un avance significativo en la comprensión 
                        y predicción de las anomalías de temperatura, ofreciendo una base sólida y resultados 
                        prometedores para futuras investigaciones y aplicaciones prácticas en el campo de la 
                        climatología y el análisis del cambio climático.
                        """, style={**text_style, 'fontStyle': 'italic', 'textAlign': 'center', 'marginTop': '25px'})

                ], md=12) 
            ])
        ]
        
        try:
            return create_section("Conclusiones del Proyecto", contenido_conclusiones)
        except Exception as e:
            print(f"ERROR al crear la sección de Conclusiones: {e}")
            
            return html.Div(f"Error al generar contenido para Conclusiones: {str(e)}")

if __name__ == '__main__':
    app.run(debug=False) 