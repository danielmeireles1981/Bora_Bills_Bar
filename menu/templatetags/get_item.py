from django import template

register = template.Library()

@register.filter
def get_item(obj, key):
    # Protege para evitar erro em caso de objeto não ser dicionário
    if isinstance(obj, dict):
        return obj.get(key)
    try:
        return getattr(obj, key)
    except Exception:
        return None
