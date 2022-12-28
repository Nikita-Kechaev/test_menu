from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Menu(models.Model):
    previous_level = models.ForeignKey(
        'Menu',
        blank=True,
        null=True,
        verbose_name="предыдущий пункт меню",
        related_name='previous',
        on_delete=models.CASCADE
    )
    label = models.CharField(
        max_length=255,
        verbose_name="Название пункта меню",
    )

    class Meta:
        verbose_name = "пункт меню"
        verbose_name_plural = "пункты меню"

    def __str__(self):
        return self.label
