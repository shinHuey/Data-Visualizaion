import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import html, dcc

import os
cwd = os.getcwd()
df = pd.read_csv("COVID-19 Survey Student Responses.csv")

# Pre-Processing of the data
df['Time spent on TV'].replace('No tv', 0, inplace=True)
df['Time spent on TV'].replace('n', 0, inplace=True)
df['Time spent on TV'].replace('N', 0, inplace=True)
df['Time spent on TV'].replace(' ', 0, inplace=True)
df['Time spent on TV'] = df['Time spent on TV'].astype('float')
df['Prefered social media platform'] = df['Prefered social media platform'].replace('None', 'None')
df['Prefered social media platform'] = df['Prefered social media platform'].replace('Whatsapp', 'WhatsApp')

# Create Dash app
app = dash.Dash(__name__)

# Define the colors
colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']

# Filter out values
filtered_sb_values = df['Stress busters'].value_counts(normalize=True)
filtered_sb_values = filtered_sb_values[filtered_sb_values >= 0.01]

filtered_m_values = df['What you miss the most'].value_counts(normalize=True)
filtered_m_values = filtered_m_values[filtered_m_values >= 0.01]

# Filter out low correlation data
correlation_threshold = 0.3
corr_df = df.corr().abs()
mask = corr_df < correlation_threshold
corr_df[mask] = 0

# Define the layout
app.layout = html.Div(children=[
    
    html.H1(children='IMPACT OF COVID-19 ON STUDENTS',
            style={'textAlign': 'center', 'color': '#941a18', 'fontSize': '36px'}),

    html.H3(children='Distribution of Students by Region of Residence',
),

    dcc.Graph(
        id='region',
        figure={
            'data': [
                go.Pie(
                    labels=df['Region of residence'].value_counts().index,
                    values=df['Region of residence'].value_counts().values,
                    hole=0.25,
                    marker=dict(colors=colors)
                )
            ],
            'layout': go.Layout(
                margin=dict(l=30, b=30, t=60, r=30)
            )
        }
    ),
    
    html.H3(children='Age-wise Distribution of Students'),
    dcc.Graph(
        id='age',
        figure={
            'data': [
                go.Bar(
                    x=df['Age of Subject'].value_counts().index,
                    y=df['Age of Subject'].value_counts().values,
                    marker=dict(color=colors[0])
                )
            ],
            'layout': go.Layout(
                margin=dict(l=100, b=100, t=50, r=100),
                xaxis=dict(title='Age'),
                yaxis=dict(title='Count')
            )
        }
    ),
    html.H3(children='Medium Used for Online Classes'),
    dcc.Graph(
        id='medium',
        figure={
            'data': [
                go.Pie(
                    labels=df['Medium for online class'].value_counts().index,
                    values=df['Medium for online class'].value_counts().values,
                    hole=0.25,
                    marker=dict(colors=colors)
                )
            ],
            'layout': go.Layout(
                margin=dict(l=30, b=30, t=60, r=30)
            )
        }
    ),
    html.H3(children='Time Spent on Various Activities'),
    dcc.Graph(
        id='time_spent',
        figure={
            'data': [
                go.Box(
                    y=df['Time spent on Online Class'],
                    name='Online Class',
                    marker=dict(color=colors[0])
                ),
                go.Box(
                    y=df['Time spent on self study'],
                    name='Self Study',
                    marker=dict(color=colors[1])
                ),
                go.Box(
                    y=df['Time spent on fitness'],
                    name='Fitness',
                    marker=dict(color=colors[2])
                ),
                go.Box(
                    y=df['Time spent on sleep'],
                    name='Sleep',
                    marker=dict(color=colors[3])
                ),
                go.Box(
                    y=df['Time spent on social media'],
                    name='Social Media',
                    marker=dict(color=colors[4])
                ),
                go.Box(
                    y=df['Time spent on TV'],
                    name='TV',
                    marker=dict(color=colors[0])
                )
            ],
            'layout':go.Layout(
            yaxis=dict(title='Time(in hours)'),
            margin=dict(l=100, b=100, t=50, r=100)
        )
    }
),

html.H3(children='Preferred Social Media Platform'),
dcc.Graph(
    id='social_media',
    figure={
        'data': [
            go.Bar(
                x=df['Prefered social media platform'].value_counts().index,
                y=df['Prefered social media platform'].value_counts().values,
                marker=dict(color=colors[0])
            )
        ],
        'layout': go.Layout(
            xaxis=dict(title='Social Media Platform'),
            yaxis=dict(title='Number of Students'),
            margin=dict(l=100, b=100, t=50, r=100)
        )
    }
),

# Favourite stress buster
html.H3(children='Favourite Stress Buster'),
dcc.Graph(
    id='stress_buster',
    figure={
        'data': [
            go.Pie(
                labels=filtered_sb_values.index,
                values=filtered_sb_values.values,
                hole=0.25,
                marker=dict(colors=colors)
            )
        ],
        'layout': go.Layout(
            margin=dict(l=30, b=30, t=60, r=30)
        )
    }
),

# What did they miss the most?
html.H3(children='What did they miss the most?'),
dcc.Graph(
    id='miss_most',
    figure={
        'data': [
            go.Bar(
                x=filtered_m_values.index,
                y=filtered_m_values.values,
                marker=dict(color=colors)
            )
        ],
        'layout': go.Layout(
            xaxis=dict(title='Missing Item'),
            yaxis=dict(title='Count'),
            margin=dict(l=100, b=100, t=50, r=100)
        )
    }
),

# Health impacted by various factors
html.H3(children='Health Impacted by Various Factors'),
dcc.Graph(
    id='health_impact_yes',
    figure={
        'data': [
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on Online Class'] / 60,
                name='Time spent on Online Class',
                marker=dict(color=colors[0], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on TV'] / 60,
                name='Time spent on TV',
                marker=dict(color=colors[1], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on social media'] / 60,
                name='Time spent on social media',
                marker=dict(color=colors[2], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on fitness'] / 60,
                name='Time spent on fitness',
                marker=dict(color=colors[3], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on self study'] / 60,
                name='Time spent on self study',
                marker=dict(color=colors[4], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'YES']['Time spent on sleep'] / 60,
                name='Time spent on sleep',
                marker=dict(color=colors[0], size=6, symbol='circle'),
            )
        ],
        'layout': go.Layout(
            xaxis=dict(title='Health issue during lockdown = YES', tickangle=10),
            yaxis=dict(title='Time Spent (hours)'),
            legend=dict(title='Activities', tracegroupgap=0),
            margin=dict(l=100, b=100, t=50, r=100)
        )
    }
),


dcc.Graph(
    id='health_impact_no',
    figure={
        'data': [
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on Online Class'] / 60,
                name='Time spent on Online Class',
                marker=dict(color=colors[0], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on TV'] / 60,
                name='Time spent on TV',
                marker=dict(color=colors[1], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on social media'] / 60,
                name='Time spent on social media',
                marker=dict(color=colors[2], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on fitness'] / 60,
                name='Time spent on fitness',     
                marker=dict(color=colors[3], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on self study'] / 60,
                name='Time spent on self study',
                marker=dict(color=colors[4], size=6, symbol='circle'),
            ),
            go.Box(
                y=df[df['Health issue during lockdown'] == 'NO']['Time spent on sleep'] / 60,
                name='Time spent on sleep',
                marker=dict(color=colors[0], size=6, symbol='circle'),
            )
        ],
        'layout': go.Layout(
            xaxis=dict(title='Health issue during lockdown = NO', tickangle=10),
            yaxis=dict(title='Time Spent (hours)'),
            legend=dict(title='Activities', tracegroupgap=0),
            margin=dict(l=100, b=100, t=50, r=100)
        )
    }
),


],
style={"backgroundColor": "lightgray", "padding": "20px"}
)

if __name__ == '__main__':
    app.run_server(debug=True)
