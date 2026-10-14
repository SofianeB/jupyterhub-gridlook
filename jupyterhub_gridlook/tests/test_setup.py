from jupyterhub_gridlook import setup_gridlook, STATIC_DIR


def test_static_present():
    assert (STATIC_DIR / "index.html").exists()


def test_setup_shape():
    cfg = setup_gridlook()
    assert "{port}" in cfg["command"]
    assert cfg["new_browser_tab"] is False
