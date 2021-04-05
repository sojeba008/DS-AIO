"""
Created on 05 avr. 17:44 2021

@author: HaroldKS
"""

import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,  suppress_callback_exceptions=False)
server = app.server
