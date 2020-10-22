from django.contrib import admin
from results.models import billInfo, billResults

# Register your models here.
admin.site.register(billResults)
admin.site.register(billInfo)
