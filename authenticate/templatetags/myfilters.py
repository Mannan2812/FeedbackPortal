from django import template
register= template.Library()
@register.filter(name=  'addClass')
def addClass(value,arg1):
    arg = arg1.split(' ')
    if len(arg)==1:
        return value.as_widget(attrs = {'class':arg[0]})
    else:
        return value.as_widget(attrs = {'class':arg[0],'style':arg[1]})
@register.filter(name= 'addAttr')
def addAttr(value,arg):
    return value.as_widget(attrs = {'value':arg})
