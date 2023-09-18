import dash
from dash import dcc, html, Input, Output
import scipy
import math

app = dash.Dash(__name__)

app.layout = html.Div([
  html.H1("Study sample size calculator"),

  # Input components
  dcc.Input(id='input-1', type='number', value=0.10),
  dcc.Input(id='input-2', type='number', value=5),
  dcc.Input(id='input-3', type='number', value=50),
  dcc.Input(id='input-4', type='number', value=50),
  dcc.Input(id='input-5', type='number', value=0.10),
  dcc.Input(id='input-6', type='number', value=0.8),

  # Output components
  html.Div(id='output-1'),
  html.Div(id='output-2'),
  html.Div(id='output-3')
])
@app.callback(
  Output('output-1', 'children'),
  Output('output-2', 'children'),
  Output('output-3', 'children'),
  Input('input-1', 'value'),
  Input('input-2', 'value'),
  Input('input-3', 'value'),
  Input('input-4', 'value'),
  Input('input-5', 'value'),
  Input('input-6', 'value')
)
def update_outputs(input1, input2, input3, input4, input5, input6):
  p_control = input1
  p_test = input1 * (1 + input2/100.)
  q_test = input3
  q_control = input4
  alpha = input5
  beta = 1 - input6
  kappa = q_test / q_control
  n_control = (p_test * (1 - p_test) / kappa + p_control * (1 - p_control)) \
              * ((scipy.stats.norm.ppf(1 - alpha/2) +
                  scipy.stats.norm.ppf(1 - beta)) / (p_test - p_control)) ** 2
  n_test = kappa * n_control
  output1 = f"Required study size is {math.ceil(n_test) + math.ceil(n_control)}"
  output2 = f"Required test group size is {math.ceil(n_test)}"
  output3 = f"Required control group size is {math.ceil(n_control)}"
  return output1, output2, output3


if __name__ == '__main__':
  app.run_server(debug=False)

