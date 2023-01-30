from django.test import TestCase
from django.urls import reverse
from pages.models import Page

class HomepageTests(TestCase):
    """ Tests for the home page. """

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the home page is available by name. """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the home page uses the correct template. """
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_template_content(self):
        """ Test that the home page contains the correct content. """
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Opening Spring 2023")

    def test_template_content_after_db_update(self):
        """ Test that the home page contains the correct content after the db is updated. """
        # update the db:
        Page.objects.create(title="Test Title Home", handle="home", content="<p>Test content home</p>")
        # test the home page:
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Test content home")
        self.assertContains(response, "Test Title Home")

class WelcomePageTests(TestCase):
    """ Tests for the welcome page. """

    def test_url_exists_at_correct_location(self):
        """ Test that the welcome page is available at the correct location. """
        response = self.client.get("/welcome/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the welcome page is available by name. """
        response = self.client.get(reverse("welcome"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the welcome page uses the correct template. """
        response = self.client.get(reverse("welcome"))
        self.assertTemplateUsed(response, "welcome.html")

    def test_template_content(self):
        """ Test that the welcome page contains the correct content. """
        response = self.client.get(reverse("welcome"))
        self.assertContains(response, "Welcome to the Village")

    def test_template_content_after_db_update(self):
        """ Test that the welcome page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title Philosophy", handle="philosophy", content="<p>Test content philosophy</p>")
        response = self.client.get(reverse("welcome"))
        self.assertContains(response, "Test content philosophy")
        self.assertContains(response, "Test Title Philosophy")

class ClassroomsPageTests(TestCase):
    """ Tests for the classrooms page. """

    def test_url_exists_at_correct_location(self):
        """ Test that the classrooms page is available at the correct location. """
        response = self.client.get("/classrooms/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the classrooms page is available by name. """
        response = self.client.get(reverse("classrooms"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the classrooms page uses the correct template. """
        response = self.client.get(reverse("classrooms"))
        self.assertTemplateUsed(response, "classrooms.html")

    def test_template_content(self):
        """ Test that the classrooms page contains the correct content. """
        response = self.client.get(reverse("classrooms"))
        self.assertContains(response, "Classrooms")

    def test_template_content_after_db_update(self):
        """ Test that the classrooms page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title Classrooms", handle="classrooms", content="<p>Test content classrooms</p>")
        response = self.client.get(reverse("classrooms"))
        self.assertContains(response, "Test content classrooms")
        self.assertContains(response, "Test Title Classrooms")

class PreschoolPageTests(TestCase):
    """ Tests for the preschool page. """

    def test_url_exists_at_correct_location(self):
        """ Test that the preschool page is available at the correct location. """
        response = self.client.get("/preschool/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the preschool page is available by name. """
        response = self.client.get(reverse("preschool"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the preschool page uses the correct template. """
        response = self.client.get(reverse("preschool"))
        self.assertTemplateUsed(response, "preschool.html")

    def test_template_content(self):
        """ Test that the preschool page contains the correct content. """
        response = self.client.get(reverse("preschool"))
        self.assertContains(response, "Coming Fall 2023")

    def test_template_content_after_db_update(self):
        """ Test that the preschool page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title Preschool", handle="preschool", content="<p>Test content preschool</p>")
        response = self.client.get(reverse("preschool"))
        self.assertContains(response, "Test content preschool")
        self.assertContains(response, "Test Title Preschool")

class SchoolAgePageTests(TestCase):
    """ Tests for the school age page. """
    def test_url_exists_at_correct_location(self):
        """ Test that the school age page is available at the correct location. """
        response = self.client.get("/school-age/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the school age page is available by name. """
        response = self.client.get(reverse("school_age"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the school age page uses the correct template. """
        response = self.client.get(reverse("school_age"))
        self.assertTemplateUsed(response, "school_age.html")

    def test_template_content(self):
        """ Test that the school age page contains the correct content. """
        response = self.client.get(reverse("school_age"))
        self.assertContains(response, "School Age")

    def test_template_content_after_db_update(self):
        """ Test that the school age page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title School Age", handle="school_age", content="<p>Test content school age</p>")
        response = self.client.get(reverse("school_age"))
        self.assertContains(response, "Test content school age")
        self.assertContains(response, "Test Title School Age")

class SteamPageTests(TestCase):
    """ Tests for the steam page. """

    def test_url_exists_at_correct_location(self):
        """ Test that the steam page is available at the correct location. """
        response = self.client.get("/steam/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the steam page is available by name. """
        response = self.client.get(reverse("steam"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the steam page uses the correct template. """
        response = self.client.get(reverse("steam"))
        self.assertTemplateUsed(response, "steam.html")

    def test_template_content(self):
        """ Test that the steam page contains the correct content. """
        response = self.client.get(reverse("steam"))
        self.assertContains(response, "Science. Technology. Engineering. Art. Mathematics.")

    def test_template_content_after_db_update(self):
        """ Test that the steam page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title STEAM", handle="steam", content="<p>Test content STEAM</p>")
        response = self.client.get(reverse("steam"))
        self.assertContains(response, "Test content STEAM")
        self.assertContains(response, "Test Title STEAM")

class ContactPageTests(TestCase):
    """ Tests for the contact page. """

    def test_url_exists_at_correct_location(self):
        """ Test that the contact page is available at the correct location. """
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """ Test that the contact page is available by name. """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ Test that the contact page uses the correct template. """
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        """ Test that the contact page contains the correct content. """
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "Contact Us")

    def test_template_content_after_db_update(self):
        """ Test that the contact page contains the correct content after the db is updated. """
        Page.objects.create(title="Test Title Contact", handle="contact", content="<p>Test content contact</p>")
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "Test content contact")
        self.assertContains(response, "Test Title Contact")
