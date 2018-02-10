from django.db import models
from .models import User, ItemList, Item

def get_contents(acc_name):
    return (get_username(acc_name), get_items(get_itemlist(acc_name)))

def get_items(item_list):
    return item_list.items

def get_username(acc_name):
    return User.objects.get(first_name__iexact=acc_name)

def get_itemlist(acc_name):
    return User.objects.get(first_name__iexact=acc_name).item_list

def remove_object(item_num):
    item = Item.objects.get(item_num)
    item.delete()

def add_object(obj_ls, obj_ty, obj_nm, obj_des, quant):
    o = Item(obj_list=obj_ls, obj_type=obj_ty, obj_name=obj_nm, obj_description=obj_des, quantity=quant)
    o.save()

