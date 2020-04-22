from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, AllowedHostsOriginValidator
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                url(r"^messages/(?P<username>[\w.@+-]+)/$",ChatConsumer),
                ]
            )
        )
    )
})
