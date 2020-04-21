#custom template filter
from django import template
#register the template
register = template.Library()

#using decorators to registering
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from string!
    """

    return value.replace(arg,'')

#registering the function --> 'cut' is a string that should be called in the html file , and cut is the actual function
#register.filter('cut',cut)
