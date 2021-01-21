from django import forms
from .models import Invoice
from django.utils import timezone

class InvoiceAddModelForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ['is_approved', 'is_completed', 'is_valid']
        widgets = {
            'serial_num': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True,
                    'value': timezone.now().astimezone().strftime('%Y%m%d%H%M%S'),
                }
            ),
            'employee': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'title': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'filldate': forms.DateInput(attrs={'class': 'form-control is-valid', 'type': 'date'}),
            'request_unit': forms.Select(attrs={'class': 'custom-select'}),
            'pay_comp': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'pay_methold': forms.Select(attrs={'class': 'custom-select'}),
            'pay_date': forms.DateInput(attrs={'class': 'form-control is-valid', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control is-valid'})
        }

class InvoiceUpdateModelForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ['serial_num', 'is_approved', 'is_valid']
        widgets = {
            'employee': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'title': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'filldate': forms.DateInput(attrs={'class': 'form-control is-valid', 'type': 'date'}),
            'request_unit': forms.Select(attrs={'class': 'custom-select'}),
            'pay_comp': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'pay_methold': forms.Select(attrs={'class': 'custom-select'}),
            'pay_date': forms.DateInput(attrs={'class': 'form-control is-valid', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control is-valid'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }