from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update(
            {'class': 'textarea mb-2 border border-gray-300 text-gray-900 text-sm rounded-lg  block w-full p-2.5'}
        )
        self.fields['watchAgain'].widget.attrs.update({'class': 'toggle toggle-xs'})

    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {
            'watchAgain': ('Watch Again')
        }
        widgets = {
            'text': Textarea(attrs={'rows': 8})
        }