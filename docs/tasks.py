from celery import shared_task
from django.core.mail import send_mail

from config import settings
from .models import Document


@shared_task
def send_admin_notification(document_id):
    """ Отправляет уведомление администратору о новом документе. """

    document = Document.objects.get(id=document_id)
    send_mail(
        subject='Загружен новый документ',
        message=f'Новый документ загружен пользователем {document.user.username}.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['admin@example.com'],
        fail_silently=False,
    )


@shared_task
def send_user_notification(document_id, status):
    """ Отправляет уведомление пользователю о смене статуса документа. """

    document = Document.objects.get(id=document_id)
    send_mail(
        subject='Обновление статуса документа',
        message=f'Ваш документ {status}.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[document.user.email],
        fail_silently=False,
    )
