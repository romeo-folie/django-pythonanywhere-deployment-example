from django import template

register = template.Library()

def cut(value, arg):
    """
    This removes the specified word from the string.
    """
    return value.replace(arg, '')

register.filter('cut', cut)
