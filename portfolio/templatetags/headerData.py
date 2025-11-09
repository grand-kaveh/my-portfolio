from django import template
from portfolio.models import InfoModel


register = template.Library()

@register.simple_tag
def get_information(): 
    return InfoModel.objects.last()
