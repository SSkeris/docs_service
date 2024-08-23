from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Document


class DocumentTest(TestCase):
    """ Тестирование загрузки документа с использованием Django REST Framework. """

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.login(username='testuser', password='12345')

    def test_upload_document(self):
        """ Эта функция тестирует загрузку документа с использованием Django REST Framework.
        Функция создает тестовый документ путем записи содержимого в файл.
        Затем она отправляет запрос POST в конечную точку API
        для загрузки документов с тестовым документом в виде файла. """

        with open('test_document.txt', 'w') as f:
            f.write('test document content')
        with open('test_document.txt', 'rb') as f:
            response = self.client.post('/api/documents/', {'file': f}, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().user, self.user)
