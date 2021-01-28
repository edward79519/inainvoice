from django import template

register = template.Library()

@register.filter
def moneycent(values):
    return format(float(values), ',')

@register.filter
def crncte(values):
    cte_dic = {
        '新台幣': 'NTD',
        '美金': 'USD',
        '歐元': 'EUR',
        '人民幣': 'RMB',
    }
    return cte_dic[values]