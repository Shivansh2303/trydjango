from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content']

    def clean(self):
        data=self.cleaned_data
        title=data.get('title')
        qs=Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"{title} is alrerady in use. Please pick another title. ")
        return data


class ArticleFormOld(forms.Form):
    title=forms.CharField(max_length=255)
    content=forms.CharField(widget=forms.Textarea)

    # def clean_title(self):
    #     cleaned_data=self.cleaned_data
    #     title=cleaned_data.get('title')
    #     if title.lower().strip()=='the office':
    #         raise forms.ValidationError('This title is taken')
    #     print('title')
    #     return title

    def clean(self):
        cleaned_data=self.cleaned_data
        # print("all cleaned data ", cleaned_data)
        title = cleaned_data.get('title')
        content=cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title','this title is taken.')
            # raise forms.ValidationError('This title is taken')
        if "office" in content or "office" in title.lower():
            self.add_error('content','office cannot be in content')
            raise forms.ValidationError('office is not allowed')

        return cleaned_data
