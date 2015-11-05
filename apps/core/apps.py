from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    name = 'apps.core'
    verbose_name = "User's Profile"

    def ready(self):
        from apps.core import signals


