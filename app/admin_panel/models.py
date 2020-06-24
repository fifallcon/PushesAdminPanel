from django.db import models

# две модели,
# поля строго по ТЗ
class Options(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название опции", max_length=200)
    value = models.BooleanField("Значение (Boolean)")


class Pushes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Заголовок уведомления", max_length=50)
    text = models.TextField("Текст уведомления")
    created = models.DateField("Дата создания", auto_now_add=True)
    released = models.DateField("Дата отправки")
    is_released = models.BooleanField("Отправлен", default=False)
    released_cnt = models.IntegerField("Кол-во отправленных пушей", default=0)
