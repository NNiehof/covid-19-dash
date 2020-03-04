from services import App, import_data
from layout import get_layout

# create a Dash app instance
app = App(name=__name__)
app.title = "COVID-19 dashboard"

# server is called by gunicorn when deployed
server = app.server

# retrieve data
[import_data(dtype=data_type) for data_type in ['confirmed', 'deaths', 'recovered']]

# load layout into the app
app.layout = get_layout()

if __name__ == '__main__':
    app.run_server()