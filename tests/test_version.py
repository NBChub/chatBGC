import toml

import chatbgc


def test_version():
    """Check if version in pyproject.toml and __init__.py match"""
    toml_version = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
    app_version = chatbgc.__version__
    assert (
        toml_version == app_version
    ), "Version mismatch between pyproject.toml and chatbgc/__init__.py"
