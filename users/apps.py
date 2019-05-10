from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(save):
    	import users.signals