from django.apps import AppConfig


class TicketAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket_app'

    def ready(self):
        import ticket_app.signals 
