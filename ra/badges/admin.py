from django.contrib import admin
from badges.models import Badge, Member_x_Badge

admin.site.register((Badge, Member_x_Badge))
