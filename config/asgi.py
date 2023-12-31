"""
ASGI config for styleguide_example project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from .routing import websocket_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.base")

http_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": http_application,
        "websocket": websocket_application,
    }
)
