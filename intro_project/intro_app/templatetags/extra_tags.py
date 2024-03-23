from django import template

register = template.Library()

@register.filter(name="add_excl")
def add_exclamation(value):
    return str(value) + "!"