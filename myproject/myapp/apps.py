from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        from myapp.models import Osoba

        content_type = ContentType.objects.get_for_model(Osoba)
        
        if not Permission.objects.filter(codename='can_view_other_persons').exists():
            Permission.objects.create(
                codename='can_view_other_persons',
                name='Can view other persons',
                content_type=content_type
            )
