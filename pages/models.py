from django.db import models
# from tinymce import models as tinymce_models
# from tinymce.models import HTMLField

class Page(models.Model):

    HANDLE_CHOICES = (
        ('home', 'Home'),
        ('philosophy', 'Our Philosophy'),
        ('classrooms', 'Classrooms'),
        ('steam.', 'S.T.E.A.M.'),
        ('preschool', 'Preschool'),
        ('school_age', 'School Age'),
        ('contact', 'Contact'),
    )

    title = models.CharField(max_length=200)
    
    handle = models.CharField(
        choices=HANDLE_CHOICES, 
        blank=False,
        null=True,
        max_length=200,
    )

    default = '''
        <p>
            Our mission is to provide child-centered care focused on fostering children's creativity, educational development, 
            and independece. We provide a resource-rich, inclusive environment that allows each child to develop at his/her own pace.
            Our classrooms are designed to give children room to grow and express themselves in a safe space.
        </p>
    '''

    content = models.CharField(max_length=500000, default=default)
    image = models.ImageField(null=True)
