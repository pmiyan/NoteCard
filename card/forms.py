from django import forms
from .models import CardTitle, CardType
from django.contrib.auth.models import User

class CardCreationForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
    categories = forms.ModelMultipleChoiceField(queryset=CardType.objects.all())

    class Meta:
        model = CardTitle
        fields = ['title', 'content', 'categories']

    def save(self, commit=True, author=None):
        instance = super().save(commit=False)
        instance.author = User.objects.get(id=1) #TODO remove after users created  # Set the author field from the parameter
        if commit:
            instance.save()
            self.save_m2m()
        return instance
