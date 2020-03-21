from datasette import hookimpl
from starlette.middleware.errors import ServerErrorMiddleware
import importlib


@hookimpl
def asgi_wrapper():
    def wrap_with_class(app):
        return ServerErrorMiddleware(app, debug=True)

    return wrap_with_class
