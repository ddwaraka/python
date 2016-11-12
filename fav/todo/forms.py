from django import forms
from datetime import date


class TaskForm(forms.Form):
    task_name = forms.CharField(label='Task Name', max_length=100, min_length=3)
    task_priority = forms.ChoiceField(label='Priority', choices=[("High", 'High'), ("Medium", "Medium",),('Low', "Low")])
    task_status = forms.ChoiceField(label='Status', choices=[('Complete', 'Complete'), ('Incomplete', 'Incomplete')])
    target_date = forms.DateField(label='Date')

    def clean_target_date(self):
        task_date = self.cleaned_data['target_date']
        print type(task_date)
        if task_date < date.today():
            raise forms.ValidationError("Date cannot be lesser than today's date")

        return task_date


