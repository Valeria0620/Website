"""
Definition of forms.
"""

from django.db import models
from .models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class  BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}

class visitorfeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=3, max_length=100)
    name.widget.attrs.update({'class': 'form-control', 'id' : 'my1'})
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1', 'Мужской'), ('2', 'Женский')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Какую процедурой вы воспользовались в нашем салоне?',
                                 choices=(('1', 'Маникюр/педикюр'),
                                          ('2', 'Парикмахерские услуги'),
                                          ('3', 'Косметология'),
                                          ('4', 'Пирсинг'),
                                          ('5', 'Коррекция/окрашивание бровей'),
                                          ('6', 'Моментальный загар')), initial=1)
    internet.widget.attrs.update({'class': 'form-control', 'id' : 'my2'})
    massage = forms.CharField(label='Отзывы и предложения',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20,'class': 'form-control', 'id' : 'my3'}))
    notice = forms.BooleanField(label='Хотите получать новости салона на e-mail?',required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=4)
    email.widget.attrs.update({'class': 'form-control', 'id' : 'my4'})
    

