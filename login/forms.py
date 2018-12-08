#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/15 22:56 
# @Author : Aries 
# @Site :  
# @File : forms.py 
# @Software: PyCharm


from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
    password2 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)