"""
WSGI config for mychatproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychatproject.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": URLRouter(
            chat.routing.websocket_urlpatterns
    ),
})
