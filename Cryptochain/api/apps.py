from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = 'Api'

    def ready(self):
        print("Starting Scheduler ...")
        
        # Setting up the Service Scheduler
        from .services import crypto_scheduler
        # crypto_scheduler.start_pull_ethereum_job()
        # crypto_scheduler.start_pull_neo_job()