from django.template import Library

register = Library()

@register.filter()
def show_sex(sex, flag='zh'):
    change = {
        'zh': ('女', '男'),
        'en': ('Female', 'male'),
    }
    return change[flag][sex]
    # register.filter(show_sex)

