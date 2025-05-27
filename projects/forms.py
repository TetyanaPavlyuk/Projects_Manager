from django import forms

from projects.models import Project, Feedback


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["employee", "rating", "comment"]
