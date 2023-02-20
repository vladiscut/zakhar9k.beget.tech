from django import template
from bhome.models import *
from projects.models import *

register = template.Library()

# @register.simple_tag()
# def get_partners():
#     return Partners.objects.filter(is_published=True)

@register.inclusion_tag('bhome/list_partners.html')
def show_partners():
    partners= Partners.objects.filter(is_published=True)
    return {'partners':partners}

@register.inclusion_tag('bhome/first_tab_project.html')
def show_project_1tab(project_id):
    project =  Projects.objects.get(pk = project_id)
    return {'project':project}



