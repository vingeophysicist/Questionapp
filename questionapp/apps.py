from django.apps import AppConfig


class QuestionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questionapp'
    
    
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        import questionapp.signals
