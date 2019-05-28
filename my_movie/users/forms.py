from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from .models import MyUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4, max_length=30,
                               error_messages={
                                   'min_length': '用户名不能少于4个字符',
                                   'max_length': '用户名不能多于30个字符',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'})
                               )
    password = forms.CharField(min_length=8, max_length=30,
                               error_messages={
                                   'min_length': '密码不能少于8个字符',
                                   'max_length': '密码不能多于30个字符',
                                   'required': '密码不能为空',
                               },
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码，3~11个字符'})
                               )

    # class Meta:
    #     model = MyUser
    #     fields = ['username', 'password']

    error_messages = {'invalid_login': '用户名或密码错误'}


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=4,
                               error_messages={
                                   'min_length': '用户名不能少于4个字符',
                                   'max_length': '用户名不能多于30个字符',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': '请输入用户名'})
                               )
    password1 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': '密码不能少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请输入密码，3~11个字符'})
                                )
    password2 = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': '密码不能少于8个字符',
                                    'max_length': '密码不能多于30个字符',
                                    'required': '密码不能为空',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': '请确认密码，3~11个字符'})
                                )

    class Meta:
        model = MyUser

        fields = ['username', 'password1', 'password2']

    error_messages = {'password_mismatch': '两次密码不一致'}
