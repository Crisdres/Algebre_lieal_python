from funciones import *
from librerias import *
from estilos import *
from objeto import *

        
        
        
        
header =[
        dbc.Row(
                html.Img(src='https://i.postimg.cc/3JKzgQ3K/linkedin.png', className='img-fluid', style=estilo_imagen)
                ),
        dbc.Row(
                html.H1('Análisis de Series Temporales',  style=estilo_titulo)
                ,style={'backgroundColor': 'lightgray'}
                )
        ]

carga_informacon = [
        dbc.Row([
               dbc.Col([

                       html.H1('Ajuste y definición del modelo', style=estilo_subtitulo),
                       html.H5('Ajustar parámetros del modelo'),
                       dbc.Accordion(
                                        [
                                            dbc.AccordionItem(
                                                [
                                                    html.P("Seleccione la cantidad de retrasos"),
                                                    dcc.Dropdown(
                                                        id='autoregresivo',
                                                        options=[{'label': i, 'value': i} for i in range(0,11)],
                                                        value=1
                                                    ),
                                                ],
                                                title="Autoregresivo",
                                            ),
                                            dbc.AccordionItem(
                                                [
                                                    html.P("Seleccione la cantidad de integraciones"),
                                                    dcc.Dropdown(
                                                        id='integracion',
                                                        options=[{'label': i, 'value': i} for i in range(0,11)],
                                                        value=1
                                                    ),
                                                ],
                                                title="Integraciones",
                                            ),
                                            dbc.AccordionItem(
                                                 [
                                                     html.P("Seleccione la cantidad de retrasos"),
                                                     dcc.Dropdown(
                                                         id='memobiles',
                                                         options=[{'label': i, 'value': i} for i in range(0,11)],
                                                         value=1
                                                     ),
                                                 ],
                                                title="Medias Móviles",
                                            ),
                                        ], start_collapsed=True,
                                    ),
                       html.Hr(style=linea_doble),
                       html.H5('Orden del modelo'),
                       html.P(id = "Orden_Model"),
                       html.Hr(style=linea_doble),
                       html.H5('Cantidad de Valores a Pronosticar'),
                       dcc.Dropdown(
                           id='val_predit',
                           options=[{'label': i, 'value': i} for i in range(1,13)],
                           value=3
                       ),
                       ],className='col-3',  style=estilo_column_ge

                   ),
               dbc.Col([
                        html.H1('Gráficos descriptivos',  style=estilo_subtitulo),
                       
                       ],className='col-md-9', style=estilo_column_ge,
                       )
               ])]

descompocision= [
        dbc.Row([
               html.H1('Componenetes de la Serie temporal',  style=estilo_titulo),
               dbc.Col([
                       html.H1('Tendencia',  style=estilo_subtitulo)
                       ],className='col-4',  style=estilo_column_ge3
                       ),
               dbc.Col([
                       html.H1('Estacionalidad',  style=estilo_subtitulo)
                       ],className='col-4', style=estilo_column_ge3
                       ) ,
               dbc.Col([
                       html.H1('Componente Aleatorio',  style=estilo_subtitulo)
                       ],className='col-4', style=estilo_column_ge3
                       )
               ])]

modelo= [
        dbc.Row([
               html.H1('Modelamiento de la Serie Temporal',  style=estilo_titulo),
               dbc.Col([

                       html.H1('Ajuste y definición del modelo', style=estilo_subtitulo),
                       html.H5('Ajustar parámetros del modelo'),
                       dbc.Accordion(
                                        [
                                            dbc.AccordionItem(
                                                [
                                                    html.P("Seleccione la cantidad de retrasos"),
                                                    dcc.Dropdown(
                                                        id='autoregresivo',
                                                        options=[{'label': i, 'value': i} for i in range(0,11)],
                                                        value=1
                                                    ),
                                                ],
                                                title="Autoregresivo",
                                            ),
                                            dbc.AccordionItem(
                                                [
                                                    html.P("Seleccione la cantidad de integraciones"),
                                                    dcc.Dropdown(
                                                        id='integracion',
                                                        options=[{'label': i, 'value': i} for i in range(0,11)],
                                                        value=1
                                                    ),
                                                ],
                                                title="Integraciones",
                                            ),
                                            dbc.AccordionItem(
                                                 [
                                                     html.P("Seleccione la cantidad de retrasos"),
                                                     dcc.Dropdown(
                                                         id='memobiles',
                                                         options=[{'label': i, 'value': i} for i in range(0,11)],
                                                         value=1
                                                     ),
                                                 ],
                                                title="Medias Móviles",
                                            ),
                                        ], start_collapsed=True,
                                    ),
                       html.Hr(style=linea_doble),
                       html.H5('Orden del modelo'),
                       html.P(id = "Orden_Model"),
                       html.Hr(style=linea_doble),
                       html.H5('Cantidad de Valores a Pronosticar'),
                       dcc.Dropdown(
                           id='val_predit',
                           options=[{'label': i, 'value': i} for i in range(1,13)],
                           value=3
                       ),
                       ],className='col-3',  style=estilo_column_ge

                   ),
               dbc.Col([
                        html.H1('Predicción vs Valor Real',  style=estilo_subtitulo ),
                        
                       ],className='col-9', style=estilo_column_ge
                       ) ,
               ])]

footer =[html.Div([html.Footer(
            className="footer",
            style={
                "background-color": "#333333",
                "padding": "20px",
                "color": "white",
                "text-align": "center",
                "font-family": "Arial, sans-serif",
            },
            children=[
                html.Div(
                    className="footer-content",
                    style={
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "flex-wrap": "wrap",
                    },
                    children=[
                        html.Div(
                            className="footer-item",
                            style={
                                "margin": "10px",
                            },
                            children=[
                                html.Span(
                                    "",
                                    style={"font-weight": "bold"},
                                ),
                                html.Span(""),
                            ],
                        ),
                        html.Div(
                            className="footer-item",
                            style={
                                "margin": "10px",
                            },
                            children=[
                                html.Span(
                                    "Contacto Autor",
                                    style={"font-weight": "bold"},
                                ),
                                html.Br(),
                                html.Span(""),
                                html.Span("cristian.sanchez.fac33@gmail.com"),
                                html.Br(),
                                html.Span("https://www.linkedin.com/in/cristian-sanchez0490/"),
                            ],
                        ),

                        html.Div(
                            className="footer-item",
                            style={
                                "margin": "10px",
                            },
                            children=[

                                html.P(
                                    "La ciencia de datos es el arte de descubrir conocimiento oculto en los datos, el poder de transformar información en ideas revolucionarias y el impulso para desbloquear el potencial ilimitado de la innovación. Con cada análisis, cada modelo y cada visualización, desvelamos los secretos del universo digital y abrimos las puertas a un futuro impulsado por la inteligencia. En la intersección entre la curiosidad y la tecnología, la ciencia de datos nos invita a explorar, cuestionar y transformar el mundo que nos rodea. ¡Encendamos el fuego de la creatividad y hagamos que los datos nos revelen las respuestas que buscamos!",
                                    style={"margin-bottom": "0"},
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )], style={  'zIndex': 1,'display': 'inline-block'})]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = 'Time Series Analysis'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children = header+carga_informacon+descompocision+footer)

if __name__ == '__main__':
    app.run_server( #port="8476",
                    debug = True
                   )