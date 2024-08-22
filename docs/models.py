from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Document(models.Model):
    """ Модель документа. """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', verbose_name='документ', **NULLABLE)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата обновления', **NULLABLE)
    is_approved = models.BooleanField(default=False, verbose_name='подтверждение документа', **NULLABLE)
    is_rejected = models.BooleanField(default=False, verbose_name='отклонение документа', **NULLABLE)

    def __str__(self):
        return f"Документ {self.file} загружен пользователем {self.user}"

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'
