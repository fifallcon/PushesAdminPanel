from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from admin_panel.models import Options, Pushes


@admin.register(Pushes)
class PushesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created', 'is_released', 'released_cnt')
    readonly_fields = ('is_released', 'released_cnt')


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


admin.site.unregister(User)
admin.site.unregister(Group)

