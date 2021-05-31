#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app, server
import numpy as np
import tensorflow as tf
import plotly.express as px
import plotly.graph_objs as go
import dash

def generate_latent_points(latent_dim, n_samples, n_classes=10):
	x_input = randn(latent_dim * n_samples)
	z_input = x_input.reshape(n_samples, latent_dim)
	return z_input
 
def plot_generated(examples, n):
	for i in range(n * n):
		pyplot.subplot(n, n, 1 + i)
		pyplot.axis('off')
		pyplot.imshow(examples[i, :, :])
	pyplot.savefig("plot.png") 


model = tf.keras.models.load_model("generator.h5", custom_objects=None, compile=True, options=None)
model.compile() 
batch_size = 5
latent_dim = 128
random_latent_vectors = tf.random.normal(shape=(batch_size, latent_dim))


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to Avatar Generator", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/QkArNCT.jpg", height="300px")
                    , className="mb-4 text-center")
            ]),
     
        dbc.Row([
            dbc.Col(html.H5(children='Which Avatar for you?')                        
                    , className="mb-4")
            ]),
      

        dbc.Row([
            dbc.Button("Press to discover your avater",id= 'click-avatar', color="primary", block=True)
        ]),
        html.Span(id= 'output-avatar', style={"vertical-align": "middle"}),

        html.A("Get the full code of app on my github repositary",
                href="https://github.com/wiemHAD/")
])])

@app.callback(Output('output-avatar', 'children'),
              [Input('click-avatar', 'n_clicks')])
def on_button_click(n):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'click-avatar' in changed_id:

        image_random = np.random.normal(size=(batch_size,latent_dim))
        image_genereted = model.predict(image_random)
        fig = go.Figure(px.imshow((image_genereted * 255)[0].astype(np.uint8)))
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        return html.Div(dcc.Graph(
        id='Avatar', figure = fig))
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)
