from django.forms import ModelForm
from app.item import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ItemAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = models.Item
        exclude = [
        ]


class ItemEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = models.Item
        exclude = [
        ]
