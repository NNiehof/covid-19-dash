from services.app import App
from layout import get_layout

# create a Dash app instance
app = App(name=__name__)
app.title = "COVID-19 dashboard"

# server is called by gunicorn when deployed
server = app.server

app.layout = get_layout()

if __name__ == '__main__':
    app.run_server()