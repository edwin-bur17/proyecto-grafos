"""
Filtros personalizados de Django para los templates
"""
from django import template

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Filtro para acceder a items de un diccionario en templates de Django.
    
    Uso: {{ mi_diccionario|get_item:mi_variable }}
    
    Args:
        dictionary: Diccionario del cual obtener el item
        key: Clave a buscar en el diccionario
        
    Returns:
        El valor correspondiente a la clave, o None si no existe
    """
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter(name='to_json')
def to_json(value):
    """
    Serializa un objeto a JSON para usar en JavaScript.
    """
    import json
    from django.utils.safestring import mark_safe
    return mark_safe(json.dumps(value))
