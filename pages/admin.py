from django.contrib import admin
from .models import Page
from .forms import HomePageForm

class PageAdmin(admin.ModelAdmin):
    # fieldsets = [(None, {"fields": ("title", "handle", "content",)})]
    form = HomePageForm
    class Media:
        js = (
            'js/tinymce/tinymce.min.js',
            'js/tinymce/custom.js',
        )

admin.site.register(Page, PageAdmin)