#coding=utf-8
import datetime
from django import template
from django.template.base import (Node, NodeList,TemplateSyntaxError)

register = template.Library()

from django.conf import settings

@register.filter
def time_beauty(value):
    '''
    将value转换为更友好的时间显示格式
    value: datetime
    '''
    now_time = datetime.datetime.now()
    delta_time = now_time - value
    delta_date = now_time.date() - value.date()
    if delta_time.seconds < 60 and delta_time.days < 1:
        return u'刚刚'
    elif delta_time.seconds < 60*60 and delta_time.days < 1:
        return u'%i分钟前' %(delta_time.seconds/60)
    elif delta_date.days < 1:
        return value.strftime('今天 %H:%M')
    elif delta_date.days < 2:
        return value.strftime('昨天 %H:%M')
    elif now_time.year == value.year:
        return value.strftime('%m月%d日 %H:%M')
    else:
        return value.strftime('%Y年%m月%d日')

@register.filter
def truncatechars(value, arg):
    if value is None:
        return value
    elif type(arg) != int:
        return value
    elif len(value) > arg:
        return "%s..." % value[:arg]
    else:
        return value

#@register.filter
#def stringformat(value, arg):
#    return arg % value

class StaticNode(template.Node):
    def __init__(self, path):
        self.path = path.replace("\"", "").replace("\'", "")
    def render(self, context):
        return '%s%s' %(settings.STATIC_URL, self.path)

@register.tag('static')
def do_static(parser, token):
    '''
    自动补全url的static前缀
    '''
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return StaticNode(path)


class IfInNode(Node):
    child_nodelists = ('nodelist_true', 'nodelist_false')

    def __init__(self, var1, var2, nodelist_true, nodelist_false, negate):
        self.var1, self.var2 = var1, var2
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.negate = negate

    def __repr__(self):
        return "<IfInNode>"

    def render(self, context):
        val1 = str(self.var1.resolve(context, True))
        val2 = self.var2.resolve(context, True).split(',')

        if (self.negate and val1 not in val2) or (not self.negate and val1 in val2):
            return self.nodelist_true.render(context)
        return self.nodelist_false.render(context)


def do_ifin(parser, token, negate):
    bits = list(token.split_contents())
    if len(bits) != 3:
        raise TemplateSyntaxError("%r takes two arguments" % bits[0])
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    val1 = parser.compile_filter(bits[1])
    val2 = parser.compile_filter(bits[2])
    return IfInNode(val1, val2, nodelist_true, nodelist_false, negate)

@register.tag
def ifin(parser, token):
    """
    Outputs the contents of the block if the two arguments equal each other.

    Examples::

        {% ifin user.id '1,2' %}
            ...
        {% endifin %}

        {% ifnotin user.id '1,2' %}
            ...
        {% else %}
            ...
        {% endifnotin %}
    """
    return do_ifin(parser, token, False)

@register.tag
def ifnotin(parser, token):
    """
    Outputs the contents of the block if the two arguments are not equal.
    See ifin.
    """
    return do_ifin(parser, token, True)


@register.filter
def division(value,arg):
    '''
    除法
    value: num
    '''
    value = value if value else 0
    arg = int(arg)
    return value*1.0/arg