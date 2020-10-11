from django import forms


class ReqisterForm(forms.Form):
    username=forms.CharField(min_length=3,required=True,error_messages={
        'required':'用户名不能为空',
        'min_length':'用户名至少3位字符'
    })
    password=forms.CharField(min_length=8,required=True,error_messages={
        'required':'密码不能为空',
        'min_length':'密码至少8位字符'
    })
    confirm=forms.CharField(min_length=8,required=True,error_messages={
        'required':'密码不能为空',
        'min_length':'密码至少8位字符'
    })
    is_staff=forms.BooleanField(required=False)
    # regtime=forms.DateTimeField(required=False,error_messages={
    #     'invalid':'时间格式错误'
    # })
    #全局验证
    def clean(self):
        password=self.cleaned_data.get('password',None)
        confirm=self.cleaned_data.get('confirm','')
        if confirm!=password:
            raise forms.ValidationError({'confirm':'两次密码输入不一致'})
        return self.cleaned_data
    