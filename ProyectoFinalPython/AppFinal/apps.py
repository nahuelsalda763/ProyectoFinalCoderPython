from django.apps import AppConfig


class AppfinalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppFinal'

    def ready(self):
        import AppFinal.signals
