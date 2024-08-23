from django.contrib import admin
from .models import Document
from .tasks import send_user_notification


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'uploaded_at', 'is_approved', 'is_rejected')
    actions = ['approve_document', 'reject_document']

    def approve_document(self, request, queryset):
        """ Подтверждение документа администратором. """

        queryset.update(is_approved=True)
        for document in queryset:
            send_user_notification.delay(document.id, 'подтвержден')
        self.message_user(request, "Выбранный документ подтвержден.")

    def reject_document(self, request, queryset):
        """ Отклонение документа администратором. """

        queryset.update(is_rejected=True)
        for document in queryset:
            send_user_notification.delay(document.id, 'отклонен')
        self.message_user(request, "Выбранный документ отклонен.")

    approve_document.short_description = 'Подтверждение выбранного документа'
