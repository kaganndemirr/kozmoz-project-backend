# Third-Party
from rest_framework import viewsets, mixins
from djoser.views import LoginView as _LoginView

# Local Django
from core.serializers import LoginSerializer


class LoginView(_LoginView):
    serializer_class = LoginSerializer

    def _action(self, serializer):
        action = super(LoginView, self)._action(serializer)

        action.data.update({
            'user_id': serializer.user.id,
        })

        return action
