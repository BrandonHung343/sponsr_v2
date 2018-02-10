from django.db import models
from .models import User, ItemList, Item
def get_contents(acc_name):
    user = User.objects.get(first_name__iexact=acc_name)
    items = user.item_list
    for thing in items.items:
        checkStatus(thing)



