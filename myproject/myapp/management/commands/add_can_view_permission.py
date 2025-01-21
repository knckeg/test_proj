from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Osoba  # Importowanie modelu Osoba

class Command(BaseCommand):
    help = 'Tworzy uprawnienie can_view_other_persons'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Osoba)  
        
        if not Permission.objects.filter(codename='can_view_other_persons').exists():
            Permission.objects.create(
                codename='can_view_other_persons',
                name='Can view other persons',
                content_type=content_type
            )
            self.stdout.write(self.style.SUCCESS('Uprawnienie can_view_other_persons zostało utworzone.'))
        else:
            self.stdout.write(self.style.SUCCESS('Uprawnienie can_view_other_persons już istnieje.'))
