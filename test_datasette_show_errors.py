from datasette_show_errors import asgi_wrapper, ServerErrorMiddleware


def test_asgi_wrapper():
    app = object()
    wrapper = asgi_wrapper()
    wrapped = wrapper(app)
    assert isinstance(wrapped, ServerErrorMiddleware)
