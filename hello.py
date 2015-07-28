# code from docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html#firstapp-chapter

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def goodbye_world(request):
    return Response('Goodbye %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()

    # add the 'hello' route matching the path '/hello/<any-string-you-like>':
    config.add_route('hello', '/hello/{name}')
    config.add_route('goodbye', '/goodbye/{name}')
    # give that route a view with the above defined hello_world:
    config.add_view(hello_world, route_name='hello')
    config.add_view(goodbye_world, route_name='goodbye')

    # after we finish all the config and setting up the we make a magical
    # "WSGI application object that can be used by any WSGI server to present
    # an application to a requestor.":
    app = config.make_wsgi_app()

    # Listen on all TCP interfaces with '0.0.0.0'
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
