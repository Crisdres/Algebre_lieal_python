from funciones import *
from librerias import *
from estilos import *
from objeto import *

        
        
        
        
header =[
        dbc.Row(
                html.Img(src='https://i.postimg.cc/3JKzgQ3K/linkedin.png', className='img-fluid', style=estilo_imagen)
                ),
        dbc.Row(
                html.H1('Algebra lineal básica',  style=estilo_titulo)
                ,style={'backgroundColor': 'lightgray'}
                )
        ]

carga_informacion = [
    dbc.Row([
        dbc.Col([
            html.H1('Vector inicial', style=estilo_subtitulo),
            html.H5('Definir coordenadas'),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            html.P("Eje x"),
                            dcc.Dropdown(
                                id='eje_x',
                                options=[{'label': i, 'value': i} for i in range(-10, 11)],
                                value=1
                            ),
                        ],
                        title="Abscisas",
                    ),
                    dbc.AccordionItem(
                        [
                            html.P("Eje y"),
                            dcc.Dropdown(
                                id='eje_y',
                                options=[{'label': i, 'value': i} for i in range(-10, 11)],
                                value=1
                            ),
                        ],
                        title="Ordenadas",
                    ),
                ], start_collapsed=True,
            ),
            html.Div([
                    dcc.Graph(id="vector_inicial")
            ], 
                 style={'width': '99%', 'display': 'inline-block'}),            
        ], className='col-md-4', style=estilo_column_ge),
        dbc.Col([
            html.H1('Suma y multiplicación de vectores', style=estilo_subtitulo),
            html.Div([
                html.Div([
                    html.H5("Eje x (vector a sumar)"),
                    dcc.Slider(min=-10, max=10, id="corX_vec2", value=0, tooltip={"placement": "bottom", "always_visible": True})
                ], style={'width': '48%', 'display': 'inline-block'}),
                html.Div([
                    html.H5("Eje y (vector a sumar)"),
                    dcc.Slider(min=-10, max=10, id="corY_vec2", value=0, tooltip={"placement": "bottom", "always_visible": True})
                ], style={'width': '48%', 'display': 'inline-block'})
            ]),
            
            html.Div([
                html.Div([
                    html.H5("Multiplicar por un Escalar", style={'text-align': 'center'}),
                    dcc.Slider(min=-10, max=10, id="mult_vec2", value=1, tooltip={"placement": "bottom", "always_visible": True}),
                    html.Div([
                        dcc.Graph(id="vector_sum_mul")
                             ], style={'width': '99%', 'display': 'inline-block'})
                ], style={'width': '99%', 'display': 'inline-block'})])
        ], className='col-md-4', style=estilo_column_ge),
        dbc.Col([
            html.H1('Subespacio generado', style=estilo_subtitulo),
            html.Div([
                dcc.Graph(id="subespacio")
            ], style={'width': '99%', 'display': 'inline-block'}),
        ], className='col-md-4', style=estilo_column_ge)
    ])
]


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

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children = header+carga_informacion+descompocision+footer)


"""
@app.callback(
    [Output('vector_inicial', 'figure'),
     Output('vector_sum_mul', 'figure'),
     Output('subespacio', 'figure') 
      ],
    [Input('eje_x', 'value'),
     Input('eje_y', 'value'),
     Input('corX_vec2', 'value'),
     Input('corY_vec2', 'value'),
     Input('mult_vec2', 'value'),
    
    ]
)
def inicial(eje_x, eje_y,eje_x2, eje_y2, mult_2):
    vec_inicial = vector(eje_x,eje_y)
    vec_suma    = vector(eje_x2,eje_y2)*mult_2
    vec_result = vec_inicial+vec_suma
    
    fig_inicial = vec_inicial.fig
    #fig_inicial.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    
    fig_suma = vec_inicial.fig_suma
    #fig_suma.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    
    fig_subes = vec_inicial.subespacio(vec_suma)
    #fig_subes.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    
    return [fig_inicial,
            fig_suma,
            fig_subes]
"""

if __name__ == '__main__':
    app.run_server( #port="8476",
                    debug = True
                   )
    

