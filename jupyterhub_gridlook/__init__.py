"""Serve the Gridlook viewer through jupyter-server-proxy."""
import sys
from pathlib import Path

try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings

    warnings.warn("Importing 'jupyterhub_gridlook' outside a proper installation.")
    __version__ = "dev"

from .routes import setup_route_handlers


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "jupyterhub-gridlook"}]


def _jupyter_server_extension_points():
    return [{"module": "jupyterhub_gridlook"}]


def _load_jupyter_server_extension(server_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    name = "jupyterhub_gridlook"
    setup_route_handlers(server_app.web_app)
    server_app.log.info(f"Registered {name} server extension")

__version__ = "0.1.0"
STATIC_DIR = Path(__file__).parent / "static"


def setup_gridlook():
    if not (STATIC_DIR / "index.html").exists():
        raise RuntimeError(
            f"Gridlook assets missing in {STATIC_DIR}; run scripts/build_static.sh"
        )
    return {
        "command": [
            sys.executable, "-m", "http.server", "{port}",
            "--bind", "127.0.0.1",
            "--directory", str(STATIC_DIR),
        ],
        "absolute_url": False,
        "new_browser_tab": False,
        "launcher_entry": {
            "category": "Applications",
            "title": "Gridlook"
        },
    }
