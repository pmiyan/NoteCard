from django import forms
from .models import CardTitle, CardType, CardContent
from django.contrib.auth.models import User

class CardCreationForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
    categories = forms.ModelMultipleChoiceField(queryset=CardType.objects.all())

    class Meta:
        model = CardTitle
        fields = ['title', 'categories']

    def save(self, commit=True):
        content_data = self.cleaned_data['content']
        title_data = self.cleaned_data['title']
        type_data = self.cleaned_data['categories']

        content = CardContent.objects.create(content=content_data)
        card_title = CardTitle(title=title_data, content=content)
        card_title.author = User.objects.get(id=1) #TODO remove after users created

        if commit:
            card_title.save()
            card_title.categories.set(type_data)

        return card_title
