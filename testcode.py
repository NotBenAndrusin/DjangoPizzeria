import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.all()

print(pizzas)

    # for pizza in pizzas:
    #     print(pizza.text)
        