# jupyterhub_gridlook

[![Github Actions Status](https://github.com/SofianeB/jupyterhub-gridlook/workflows/Build/badge.svg)](https://github.com/SofianeB/jupyterhub-gridlook/actions/workflows/build.yml)

A JupyterLab extension.

This extension is composed of a Python package named `jupyterhub_gridlook`
for the server extension and a NPM package named `jupyterhub-gridlook`
for the frontend extension.

## Requirements

- JupyterLab >= 4.0.0

## Install

To install the extension, execute:

```bash
pip install jupyterhub_gridlook
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyterhub_gridlook
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

## Contributing

If you would like to contribute to this extension, please refer to the [Contributing Guide](CONTRIBUTING.md).
