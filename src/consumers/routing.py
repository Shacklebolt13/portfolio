from channels.routing import URLRouter  # type: ignore
from django.urls import path

from .echo_consumer import EchoConsumer

routes = URLRouter([path("echo", EchoConsumer.as_asgi(), name="echo")])
