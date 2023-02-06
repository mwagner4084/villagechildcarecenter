from django import template

register = template.Library()

@register.inclusion_tag('snippets/button.html')
def button(variant, href, title):
    return {'variant': variant, 'href': href, 'title': title}

@register.inclusion_tag('snippets/heading.html')
def heading(title, default="Default"):
    return {'title': title, 'default': default}
