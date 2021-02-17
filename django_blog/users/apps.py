from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # This should be added to make signals work!
    def ready(self):
        import users.signals