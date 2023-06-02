from django import template
from ..models import FrontendOptions

register = template.Library()

@register.filter
def get_hide_finished_tasks(user):
    frontend_options = FrontendOptions.get(user)
    return frontend_options.hide_finished_tasks
