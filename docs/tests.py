from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from .models import Document

User = get_user_model()


class DocumentTest(TestCase):
    """ Тестирование загрузки документа с использованием Django REST Framework. """

    def setUp(self):
        self.user = User.objects.create(email='test@user.com', password='12345')
        self.client = APIClient()
        self.client.login(email='test@user.com', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_upload_document(self):
        """ Эта функция тестирует загрузку документа с использованием Django REST Framework.
        Функция создает тестовый документ путем записи содержимого в файл.
        Затем она отправляет запрос POST в конечную точку API
        для загрузки документов с тестовым документом в виде файла. """

        with open('test_document.txt', 'w') as f:
            f.write('test document content')
        with open('test_document.txt', 'rb') as f:
            response = self.client.post('/api/documents/', {'file': f, 'user': 1}, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().user, self.user)
