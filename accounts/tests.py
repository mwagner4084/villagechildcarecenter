from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        self.user = get_user_model().objects.create(
            username='testuser',
            email='testuser@email.com',
            password='Door1Stop2!'
        )
        response = self.client.post(
            reverse('signup'),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "Door1Stop2!",
                "password2": "Door1Stop2!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[
                         0].email, "testuser@email.com")
