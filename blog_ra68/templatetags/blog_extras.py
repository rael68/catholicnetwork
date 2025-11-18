# blog_ra68/templatetags/blog_extras.py
from django import template
from django.utils.html import mark_safe
import re

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    highlighted = re.sub(
        re.escape(query),
        lambda m: f'<mark class="highlight">{m.group()}</mark>',
        text,
        flags=re.IGNORECASE
    )
    return mark_safe(highlighted)
