from django import template

register = template.Library()


@register.filter
def only_active_comments(comment):
    return comment.filter(active=True)
