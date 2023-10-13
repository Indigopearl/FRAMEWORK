from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag
def current_date():
    return timezone.now().strftime("%Y")
