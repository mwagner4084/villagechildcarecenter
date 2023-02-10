from django.contrib import admin

from .forms import HomePageForm
from .models import Contact, InformationRequest, Page


class PageAdmin(admin.ModelAdmin):
    """ Admin for the Page model. """

    fieldsets = [
        (None, {"fields": ("title", "handle", "content", "content_secondary")})]
    form = HomePageForm

    class Media:
        css = {
            'all': ('css/admin/edit-page.css',)
        }


admin.site.register(Page, PageAdmin)
admin.site.register(InformationRequest)
admin.site.register(Contact)
