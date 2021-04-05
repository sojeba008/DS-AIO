"""
Created on 05 avr. 17:39 2021

@author: HaroldKS
"""
from dash.dependencies import Input, Output, State
from .upload_file_callback import parse_contents

from app import app

# @app.callback(
#     Output('app-1-display-value', 'children'),
#     Input('app-1-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
#
# @app.callback(
#     Output('app-2-display-value', 'children'),
#     Input('app-2-dropdown', 'value'))
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

