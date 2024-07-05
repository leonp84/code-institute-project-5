from django import template

register = template.Library()


@register.filter
def index(sequence, position):
    '''
    A custom template tag that allows accessing items by index, within
    django templates.
    '''
    return sequence[position]
