from django import forms
from django.forms import widgets
from webapp.models import Tasks, Statuses, Types


class TasksListForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        required=True,
        label='Status',
        queryset=Statuses.objects.all(),
        initial=[0]
    )

    type = forms.ModelMultipleChoiceField(
        required=True,
        label='Type',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
