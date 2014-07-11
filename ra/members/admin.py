from django.contrib import admin
from members.forms import MemberModelForm
from members.models import Member, MemberType

admin.site.register((Member, MemberType))
