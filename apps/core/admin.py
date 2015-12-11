from django.contrib import admin
from . import models as core_models
# Register your models here.

admin.site.register(core_models.Menu)
admin.site.register(core_models.SubMenu)
