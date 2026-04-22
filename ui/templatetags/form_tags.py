from django import template
from django.forms.boundfield import BoundField
from django.utils.safestring import SafeString
from django.forms import PasswordInput

register = template.Library()

@register.simple_tag
def style_input(field: BoundField, css_class: str, input_type: str) -> SafeString:
    widget = field.field.widget

    if input_type == "password":
        widget = PasswordInput()

    return field.as_widget(widget=widget, attrs={
        **widget.attrs,
        "class": css_class,
    })