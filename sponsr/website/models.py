from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=10)
    user_type = models.IntegerField(max_length=1)
    item_list = models.OneToOneField(ItemList, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Item(models.Model):
    obj_list = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    obj_type = models.IntegerField(max_length=1)
    obj_name = models.CharField(max_length=200)
    obj_description = models.CharField(max_length=200)
    quantity = models.IntegerField(max_length=1)

    def __str__(self):
        return "%s %s %s" % (self.obj_type, self.obj_name, self.obj_description)

class ItemList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



