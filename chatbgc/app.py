"""Main module."""

import vanna
from vanna.flask import VannaFlaskApp
from vanna.remote import VannaDefault


def start_app(email, sqlite_path="https://vanna.ai/Chinook.sqlite"):
    vn = VannaDefault(model="chinook", api_key=vanna.get_api_key(email))
    vn.connect_to_sqlite(sqlite_path)
    VannaFlaskApp(vn).run()
