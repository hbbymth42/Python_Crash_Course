import plotly.express as px
from plotly import graph_objects as go

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
fig = px.scatter(x=rw.x_values, 
                 y=rw.y_values).update_traces(marker=dict(color='blue',
                                                          size=5))

# Emphasise the first and last points.
fig.add_trace(go.Scatter(x=[rw.x_values[0]],
                         y=[rw.y_values[0]],
                         mode="markers",
                         marker=dict(color='green', size=20),
                         name="end"))
fig.add_trace(go.Scatter(x=[rw.x_values[-1]],
                         y=[rw.y_values[-1]],
                         mode="markers",
                         marker=dict(color='red', size=20),
                         name="end"))

# Remove the axes.
fig.update_layout(
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False)
)
fig.show()