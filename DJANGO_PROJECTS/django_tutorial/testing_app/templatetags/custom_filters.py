from django import template

register = template.Library()

@register.filter(name='capitalize_words')
def capitalize_words(value):
    return ' '.join(word.capitalize() for word in value.split())
