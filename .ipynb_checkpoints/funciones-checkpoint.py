from librerias import *


def fun_global_fig():
    fig = go.Figure()
    lista_vectores = []
    for i in range(-10,10):
            for j in range(-10,10):
                lista_vectores.append([i,j])
                x = [0, i]
                y = [0, j]
                fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines',
                                              line=dict(color='blue', width=0.5)))
                fig.update_layout(showlegend=False,xaxis=dict(range=[-10, 10], constrain="domain"),
                    yaxis=dict(range=[-10, 10], scaleanchor="x", scaleratio=1),width=800,height=600,)
    return fig
global_fig = fun_global_fig()

def fun_coli_fig():
    fig = go.Figure()
    lista_vectores = []
    for i in range(-10,10):
            for j in range(-10,10):
                if i == j:
                    lista_vectores.append([i,j])
                    x = [0, i]
                    y = [0, j]
                    fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines',
                                                  line=dict(color='blue', width=0.5)))
                    fig.update_layout(showlegend=False,xaxis=dict(range=[-10, 10], constrain="domain"),
                        yaxis=dict(range=[-10, 10], scaleanchor="x", scaleratio=1),width=800,height=600,)
    return fig
coli_fig = fun_coli_fig()

def crear_figura(vector, vector_base):
    fig = go.Figure()
    vector      = vector
    vector_base = vector_base
    print("Cordenadas..",vector)
    x = [0, vector[0]*vector_base[0]]
    y = [0, vector[1]*vector_base[1]]
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines'))
    fig.update_layout(showlegend=False,xaxis=dict(range=[-10, 10], constrain="domain"),
    yaxis=dict(range=[-10, 10], scaleanchor="x", scaleratio=1),width=800,height=600,)
    return fig
    
def crear_figura_suma(vector, otro_vector, vector_base):
    vector = vector
    otro_objeto = otro_vector
    fig_suma = go.Figure()
    
    vec_1      = np.array(vector)
    x_1 = [0      , vec_1[0]*vector_base[0]]
    y_1 = [0      , vec_1[1]*vector_base[1]]
    fig_suma.add_trace(go.Scatter(x=x_1, y=y_1, mode='lines',
                                  line=dict(color='blue', width=0.5)))
    
    vec_2      = np.array(otro_objeto.vector)
    x_2 = [vec_1[0], vec_1[0]+vec_2[0]*vector_base[0]]
    y_2 = [vec_1[1], vec_1[1]+vec_2[1]*vector_base[1]]
    fig_suma.add_trace(go.Scatter(x=x_2, y=y_2, mode='lines',
                                  line=dict(color='blue', width=0.5)))
    
    vec_final      = np.array(list(vector + otro_objeto.vector))
    x_f = [0, vec_final[0]*vector_base[0]]
    y_f = [0, vec_final[1]*vector_base[1]]
    fig_suma.add_trace(go.Scatter(x=x_f, y=y_f, mode='markers+lines',
                                  line=dict(color='red', width=2)))

    fig_suma.update_layout(showlegend=False,xaxis=dict(range=[-10, 10], constrain="domain"),
    yaxis=dict(range=[-10, 10], scaleanchor="x", scaleratio=1),width=800,height=600,)

    return fig_suma


def espacio_muestral(val = ""):
    global global_fig, coli_fig
    if val == "global":
        return global_fig

    else:
        return coli_fig
    
def eslamiento_cordenadas(x,y,vec_i,vec_j):    
    vector_1 = np.array([x[0],y[0]])
    vector_1 = vector_1[0]*vec_i + vector_1[1]*vec_j
    
    vector_2 = np.array([x[1],y[1]])
    vector_2 = vector_2[0]*vec_i + vector_2[1]*vec_j
    
    x = [vector_1[0],vector_2[0]]
    y = [vector_1[1],vector_2[1]]
    
    return x,y
    
def transformacion_lineal(vec_i = [1,0], vec_j = [0,1]):
    fig = go.Figure()
    for i in range(-10,11):
            x = [i,i]
            y = [-10,10]
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines',
                                  line=dict(color='blue', width=1)))
            x2 = [-10,10]
            y2 = [i,i] 
            fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines',
                                  line=dict(color='blue', width=1)))
            
    for i in range(-10,11):
            vec_i = np.array(vec_i)
            vec_j = np.array(vec_j)
            x = [i,i]
            y = [-10,10]  
            x,y = eslamiento_cordenadas(x,y,vec_i,vec_j)
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines',
                                  line=dict(color='red', width=2)))
            
            x2 = [-10,10]
            y2 = [i,i]
            x2,y2 = eslamiento_cordenadas(x2,y2,vec_i,vec_j)
            fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines',
                                  line=dict(color='red', width=1)))
    x = [0, vec_i[0]]
    y = [0, vec_i[1]]
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines',
                                              line=dict(color='black', width=0.5))) 
    
    x = [0, vec_j[0]]
    y = [0, vec_j[1]]
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines',
                                              line=dict(color='black', width=0.5))) 
    
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers',
                                  line=dict(color='black', width=3)))       
    fig.update_layout(showlegend=False,xaxis=dict(range=[-15, 15], constrain="domain"),
        yaxis=dict(range=[-15, 15], scaleanchor="x", scaleratio=1),width=800,height=600,)
    return fig

        
        

        