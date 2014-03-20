from django.db import models

class InventoryItem(models.Model):
    serial_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    last_updated = models.DateTimeField()
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class InventoryEvent(models.Model):
    item = models.ForeignKey(InventoryItem)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return "Event:" + self.date
