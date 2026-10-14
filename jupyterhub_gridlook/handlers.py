from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join
from tornado.web import authenticated


class HelloHandler(JupyterHandler):
    @authenticated
    def get(self):
        self.finish("Gridlook server extension is running")


def setup_handlers(web_app):
    host_pattern = ".*$"
    base_url = web_app.settings["base_url"]

    route_pattern = url_path_join(
        base_url, "jupyterhub-gridlook", "hello"
    )

    handlers = [
        (route_pattern, HelloHandler),
    ]

    web_app.add_handlers(host_pattern, handlers)