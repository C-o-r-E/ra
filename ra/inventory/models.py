from django.db import models
from members.models import Member

class InventoryItem(models.Model):
    serial_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    last_updated = models.DateTimeField()
    description = models.CharField(max_length=200)
    
    owner = models.ForeignKey(Member, blank=True, null=True)

    def __unicode__(self):
        return self.name

class InventoryEvent(models.Model):
    item = models.ForeignKey(InventoryItem)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return "Event:" + self.date

class IMGFile(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(InventoryItem)
    file_size = models.IntegerField(default=0)
    full_path = models.CharField(max_length=200)
    the_file = models.FileField(upload_to='images/')

    def __unicode__(self):
        return self.name
