from django import template
from portfolio.models import (
    InfoModel, SkillModel, DegreeModel, PortfolioModel, PackageModel
)

register = template.Library()

@register.simple_tag
def get_information(): 
    return InfoModel.objects.last()

@register.simple_tag
def nav_skill(): 
    return SkillModel.objects.first()

@register.simple_tag
def nav_degree(): 
    return DegreeModel.objects.first()

@register.simple_tag
def nav_portfolio(): 
    return PortfolioModel.objects.first()

@register.simple_tag
def nav_package(): 
    return PackageModel.objects.first()
