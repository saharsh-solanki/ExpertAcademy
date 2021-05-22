from django import template
from ..models import answer, question, quize_category

register=template.Library()



@register.filter
def tostr(id):
    return str(id)

@register.filter
def menu(id):
    ret = quize_category.objects.all()
    return ret