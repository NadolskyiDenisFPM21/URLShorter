from django.db import models

class ShortedURL(models.Model):
    name = models.CharField(max_length=120, verbose_name="Назва")
    url = models.URLField(verbose_name="Посилання")
    shorted_url = models.URLField(verbose_name="Коротке посилання")
    clicks = models.IntegerField(default=0, verbose_name="Переходи")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коротке посилання'
        verbose_name_plural = 'Короткі посилання'