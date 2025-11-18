from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    import re
    highlighted = re.sub(re.escape(query), lambda m: f'<mark class="highlight">{m.group()}</mark>', text, flags=re.IGNORECASE)
    return mark_safe(highlighted)
