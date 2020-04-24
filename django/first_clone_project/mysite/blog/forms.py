from django import forms
from blog.models import Post,Comment

class PostFrom(froms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        #adding widigets
        #attrs is atrribute
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-text-area postcontent'}) #midum editor library  --> postcontent is our own class
        }

class CommentForm(froms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-text-area'}) #midum editor library  --> postcontent is our own class
        }
