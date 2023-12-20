from .models import Company
from django.db import connection, connections
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Company)
def create_company(sender, instance, created, **kwargs):
    if created:
        new_db_name = f"company_db_{instance.name.lower().replace(' ', '_')}"
       
        with connections['default'].cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {new_db_name}")

        new_db_config = connection.settings_dict.copy()
        new_db_config['NAME'] = new_db_name
        connections[new_db_name] = connections['default'].__class__(new_db_config)

        from django.core.management import call_command
        call_command('migrate', database=new_db_name)
        
        with connections[new_db_name].cursor() as cursor:
            cursor.execute(f"INSERT INTO company_company (name, employees) VALUES ('{instance.name}', {instance.employees})")
            cursor.execute(f"SELECT * FROM company_company")
            cursor.close()

          


