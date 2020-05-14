from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    name = 'authenticate'
    def ready(self):
        from authenticate import updater
        updater.start()
