# Zadanie 10 - Django Shell
1. Wyświetlenie wszystkich obiektów modelu Osoba:
```python
from myapp.models import Osoba
osoby = Osoba.objects.all()
print(osoby)