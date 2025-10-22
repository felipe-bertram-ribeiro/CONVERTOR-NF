def safe_text(element):
    if element is None:
        return None
    if hasattr(element, 'text'):
        txt = element.text
    else:
        txt = str(element)
    if txt is None:
        return None
    return txt.strip()

def safe_float(value):
    if value is None:
        return None
    try:
        return float(str(value).replace(',', '.'))
    except Exception:
        return None
