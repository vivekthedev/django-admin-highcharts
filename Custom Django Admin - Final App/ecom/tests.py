from django.test import TestCase, Client
from .models import User

class CustomUserAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin', 'admin@example.com', 'password')

    def test_analytics_view(self):
        self.client.force_login(self.user)
        response = self.client.get('/admin/ecom/user/analytics/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Users by Country")

    
    def test_get_urls(self):
        self.client.force_login(self.user)
        response = self.client.get('/admin/ecom/user/analytics/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_analytics.html")
