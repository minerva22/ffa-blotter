LONG = 'L'
SHORT = 'S'
FILL_SIDE_CHOICES = (
  (LONG, 'Long'),
  (SHORT, 'Short')
)

# Django docs: writing validators
# https://docs.djangoproject.com/en/1.10/ref/validators/#writing-validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import fields

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

# Inspired by django.forms.fields.py#FloatField
class PositiveFloatFieldForm(fields.FloatField):
  default_error_messages = {
    'invalid': _('Enter a positive number.'),
  }
  def validate(self, value):
    super(PositiveFloatFieldForm, self).validate(value)
    if value<0:
      raise ValidationError(self.error_messages['invalid'], code='invalid')
    return value

  def widget_attrs(self, widget):
    attrs = super(PositiveFloatFieldForm, self).widget_attrs(widget)
    attrs['min']=0
    return attrs