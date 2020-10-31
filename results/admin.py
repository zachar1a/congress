from django.contrib import admin
from results.models import billInfo, billResults

# Register your models here.
myModels = [billResults,billInfo]

admin.site.register(myModels)
