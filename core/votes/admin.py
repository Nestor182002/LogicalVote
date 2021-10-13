from django.contrib import admin
from votes.models import votesModel,category

# Register your models here.
admin.site.register(votesModel)
admin.site.register(category)