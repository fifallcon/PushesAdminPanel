from django.contrib import admin

# Register your models here.
from admin_panel.models import Options, Pushes

admin.site.register(Options)
admin.site.register(Pushes)
