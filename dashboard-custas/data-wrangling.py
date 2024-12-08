import pandas as pd

import plotly.express as px

# import plotly.graph_objects as go

df = pd.read_csv('data/custas.csv')

df['data'] = pd.to_datetime(df['data'])

df2 = df[(df['data'] == '2024-10') & (df['tipo'] != 'renda')]

fig = px.pie(
    df2,
    values='valor', 
    names='tipo', 
    hole=0.5,   
    )

fig.update_layout(
    # Add annotations in the center of the donut pies.
    annotations=[
        dict(
            text=str(df2['data'].dt.month[1]), 
            x=sum(fig.get_subplot(1, 1).x) / 2, 
            y=0.55,
            font_size=20, 
            showarrow=False, 
            xanchor="center"
        ),
        dict(
            text=str(df2['data'].dt.year[1]), 
            x=sum(fig.get_subplot(1, 1).x) / 2, 
            y=0.45,
            font_size=20, 
            showarrow=False, 
            xanchor="center"
        )
    ]
)

fig.show()

