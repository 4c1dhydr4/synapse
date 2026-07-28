import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'synapse.settings')
import django
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
# from synapse.settings import DEPLOY_ALERT
# from apps.tools.devops import (send_deploy_message,)

from .routers import websocket_urlpatterns

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	"websocket": AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter(
				websocket_urlpatterns
			)
		)
	),
})

# send_deploy_message(DEPLOY_ALERT)