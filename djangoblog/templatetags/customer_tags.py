from django.template import Library

register = Library()
@register.inclusion_tag('blog/page_html.html', takes_context=True)
def page_html(context):
    total_page = context['total_page']
    current_page = int(context['current_page'])
    num = 2

    page_list = []
    if current_page-num <= 0:
        for i in range(1, current_page+1):
            page_list.append(i)
    else:
        for i in range(current_page-num, current_page+1):
            page_list.append(i)
    if current_page+num >= total_page:
        for i in range(current_page+1, total_page+1):
            page_list.append(i)
    else:
        for i in range(current_page+1, current_page+num+1):
            page_list.append(i)
    return {
        'total_page': total_page,
        'per_page': context['per_page'],
        'current_page': current_page,
        'page_list': page_list,
    }
