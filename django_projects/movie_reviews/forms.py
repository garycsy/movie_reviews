from django.forms import ModelForm, Textarea
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})


    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'rows': 10}),
        }
        labels = {
            "text": _(""),
        }
        help_texts = {
            "text": _(""),
        }
        error_messages = {
            "text": {
                "max_length": _("This review too long."),
            },
        }
        validators=[MinLengthValidator(200)]