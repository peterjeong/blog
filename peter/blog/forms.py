from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as CreateUser

from .models import Post

class PostForm(forms.ModelForm):
	def clean_title(self):
		title = self.cleaned_data.get('title', '')
		if '카지노' in title:
			raise forms.ValidationError(
				'스팸 처리된 단어입니다',
				code='strange_word'
			)

	class Meta:
		model = Post
		fields = ('category', 'title', 'content', )


class PostNormalForm(forms.Form):
	title = forms.CharField(label="글 제목")
	content = forms.CharField(
		widget=forms.Textarea
	)
	category = forms.IntegerField()
	email = forms.EmailField()


class CreateUser(CreateUser):
    email = forms.EmailField(required = True)
    user_name = forms.CharField(required = False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(CreateUser, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.user_name = self.cleaned_data['user_name']

        if commit:
            user.save()

        return user