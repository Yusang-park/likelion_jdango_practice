from django import forms
from .models import Write, Comment

#modelForm 상속받는다.
class WriteForm(forms.ModelForm): 
    #modelForm의 하위 클래스 meta
    class Meta:
        model = Write
        #모두 사용
        fields = '__all__'
        #명시된 것만 사용하기
        # fields = ['title', 'content',]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]