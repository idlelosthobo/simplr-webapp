from django.forms import ModelForm
from app.container import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContainerAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContainerAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = models.Container
        exclude = [
        ]
