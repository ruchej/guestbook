from django.db import models


class GuestResponseManager(models.Manager):
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(active=True)

    def get_count(self):
        return self.count()


class GuestResponse(models.Model):

    name = models.CharField(max_length=32, verbose_name="Имя пользователя")
    body = models.CharField(max_length=512, verbose_name="Тело отзыва")
    img = models.ImageField(
        upload_to="responses", null=True, blank=True, verbose_name="Иллюстрация отзыва"
    )
    active = models.BooleanField(
        default=True, db_index=True, verbose_name="Активен ли объект"
    )
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    objects = GuestResponseManager()

    def __str__(self):
        return f"{self.pk}_{self.name}"

    def delete(self):
        self.active = False
        self.save()