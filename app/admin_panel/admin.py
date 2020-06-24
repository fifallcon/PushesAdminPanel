from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from admin_panel.models import Options, Pushes


# регистрируем самописную модель в админке
@admin.register(Pushes)
class PushesAdmin(admin.ModelAdmin):
    # определяем поля которые хотим видеть в списке обхектов,
    # и поля которые хотим запретить от редактирования
    list_display = ('title', 'text', 'created', 'is_released', 'released_cnt')
    readonly_fields = ('is_released', 'released_cnt')


# аналогично для опций
@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


admin.site.unregister(User)
admin.site.unregister(Group)

