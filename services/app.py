import os
import socket
import dash


class App(dash.Dash):

    def __init__(self, *args, **kwargs):
        """Create a Dash app instance."""

        stylesheet = list(os.environ.get(
            'EXTERNAL_STYLESHEET',
            'https://codepen.io/chriddyp/pen/bWLwgP.css'
        ))

        super().__init__(*args, external_stylesheets=stylesheet, **kwargs)

    def run_server(self, *args, **kwargs):
        """Run the server with mapping to the host IP and port."""

        # get host IP address
        host = socket.gethostbyname(socket.gethostname())

        # get PORT env var on Heroku, or standard port
        port = os.environ.get('PORT', 8050)

        super().run_server(*args, host=host, port=port, **kwargs)