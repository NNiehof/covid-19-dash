import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from services import import_data, read_data, get_date_col_names


# retrieve data from remote and save
[import_data(dtype=data_type) for data_type in ['confirmed', 'deaths', 'recovered']]

# read data from local file
confirmed, deaths, recovered = [
    read_data(dtype=data_type) for data_type in ['confirmed', 'deaths', 'recovered']
]

def get_layout():
    return html.Div(children=[
        dcc.Graph(
            figure=world_map(confirmed, title="Confirmed cases of COVID-19")
        )
    ])


def world_map(df, title=None):
    """
    World map graph with bubbles to show data frequency.
    """
    # get the column names that contain counts per date
    count_col = get_date_col_names(df)

    # turn wide data into long data (date columns into rows)
    df = df.melt(
        id_vars=['province/state', 'country/region', 'lat', 'long'],
        var_name='date', value_name="count"
    )

    # create combined location name column
    df['location_name'] = df['country/region']
    df.loc[
        df['province/state'].notnull(), ['location_name']
    ] = df['country/region'] + ', ' + df['province/state']

    return px.scatter_geo(
        df, lat='lat', lon='long', hover_name='location_name',
        size='count', animation_frame='date', projection='natural earth',
        height=800, title=title,
        color_discrete_sequence=['maroon']
    ).update_traces(marker=dict(
        sizeref=300, line=dict(width=0))
    )

