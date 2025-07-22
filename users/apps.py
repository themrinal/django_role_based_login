# Import the AppConfig base class from Django
from django.apps import AppConfig

# Define a configuration class for the 'users' app
# Django uses this class to configure some behaviors of your app
class UsersConfig(AppConfig):
    # Set the default type for automatically created primary key fields in models
    default_auto_field = 'django.db.models.BigAutoField'
    
    # This tells Django the name of the app this config belongs to
    name = 'users'

    # This method runs automatically when the app is ready (i.e., when Django starts up)
    def ready(self):
        # Import the signals module from this app
        # This is necessary to make sure your signal handlers are registered at startup
        import users.signals
