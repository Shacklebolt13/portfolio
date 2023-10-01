from django.utils.translation import gettext_lazy as __


def _(text):
    if not text:
        return "-"
    return __(text) if len(text) <= 20 else f"{__(text)[:20]}..."
