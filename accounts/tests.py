from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_signup_view_status_code(self):
        """Test signup page is accessible."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_signup_redirects_authenticated_user(self):
        """Test that logged-in users cannot access signup page."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('signup'))
        self.assertRedirects(response, '/', fetch_redirect_response=False)

    def test_login_view(self):
        """Test login page is accessible."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_successful_login(self):
        """Test user login process."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        # Default login success redirects to LOGIN_REDIRECT_URL ('/')
        self.assertRedirects(response, '/', fetch_redirect_response=False)
