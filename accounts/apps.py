from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # import all auth signal for profile formation
    def ready(self):
        from . import signals
