class MyPostAdminForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data['content']
        words = ['심심하다','관리자', '금지어', ]
        error_message =
            '[{0}] {1}'.format(', '.join(words),'와…')
        if any(word in content for word in words):
            raise forms.ValidationError(error_message)
        return content 
