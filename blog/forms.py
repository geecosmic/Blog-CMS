from django import forms
from .models import Comment, Post, AuthorApplication

from django import forms
from django.contrib.auth.models import User, Group


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'featured_image', 'content']      





# class AdminUserCreationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     role = forms.ChoiceField(choices=(('Author', 'Author'), ('Editor', 'Editor')))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#             # Assign selected group
#             group_name = self.cleaned_data['role']
#             group = Group.objects.get(name=group_name)
#             user.groups.add(group)
#         return user





class AdminUserCreationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=(('Author', 'Author'), ('Editor', 'Editor')))

    class Meta:
        model = User
        fields = ['username', 'email', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_unusable_password()  # No password set by admin
        user.is_active = True
        if commit:
            user.save()
            # Assign selected group
            group_name = self.cleaned_data['role']
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        return user


class AuthorApplicationForm(forms.ModelForm):
    class Meta:
        model = AuthorApplication
        fields = ['name', 'email', 'message']
