from django.db import models

from members.models import Member

class Badge(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Member_x_Badge(models.Model):
    member = models.ForeignKey(Member)
    badge = models.ForeignKey(Badge)
    award_date = models.DateTimeField()
    expire_date = models.DateTimeField()


        
