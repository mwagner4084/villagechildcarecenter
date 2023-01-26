from django.test import SimpleTestCase
from django.urls import reverse
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")
    def test_template_content(self): 
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Opening Spring 2023")

class WelcomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/welcome/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("welcome"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("welcome"))
        self.assertTemplateUsed(response, "welcome.html")
    def test_template_content(self): 
        response = self.client.get(reverse("welcome"))
        self.assertContains(response, "Welcome to the Village")

class ClassroomsPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/classrooms/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("classrooms"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("classrooms"))
        self.assertTemplateUsed(response, "classrooms.html")
    def test_template_content(self): 
        response = self.client.get(reverse("classrooms"))
        self.assertContains(response, "Classrooms")

class PreschoolPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/preschool/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("preschool"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("preschool"))
        self.assertTemplateUsed(response, "preschool.html")
    def test_template_content(self): 
        response = self.client.get(reverse("preschool"))
        self.assertContains(response, "COMING FALL 2023")

class SchoolAgePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/school-age/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("school_age"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("school_age"))
        self.assertTemplateUsed(response, "school_age.html")
    def test_template_content(self): 
        response = self.client.get(reverse("school_age"))
        self.assertContains(response, "SCHOOL AGE")

class SteamPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/steam/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("steam"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("steam"))
        self.assertTemplateUsed(response, "steam.html")
    def test_template_content(self): 
        response = self.client.get(reverse("steam"))
        self.assertContains(response, "SCIENCE. TECHNOLOGY. ENGINEERING. ART. MATHEMATICS.")

class ContactPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")
    def test_template_content(self): 
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "CONTACT US")

