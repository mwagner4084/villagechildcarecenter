from django.contrib import admin
from .models import Page
from .forms import HomePageForm

class PageAdmin(admin.ModelAdmin):
    """ Admin for the Page model. """

    fieldsets = [(None, {"fields": ("title", "handle", "content", "content_secondary")})]
    form = HomePageForm
    class Media:
        css = {
            'all': ('css/admin/edit-page.css',)
        }

admin.site.register(Page, PageAdmin)
