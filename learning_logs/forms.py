from django.forms import ModelForm, Textarea
from .models import Topic, Entry

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Temat publiczny'}

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': Textarea(attrs={'cols': 80})}