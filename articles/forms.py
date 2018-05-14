from django import forms
import datetime


class ArticleAdminForm(forms.ModelForm):

    def clean_pub_date(self):
        pub_date = self.cleaned_data['pub_date']
        if pub_date is not None:
            if pub_date > datetime.date.today():
                raise forms.ValidationError("The date must be past")
            return pub_date
