from django import forms
import datetime


class BlogAdminForm(forms.ModelForm):

    def clean_pub_date(self):
        pub_date = self.cleaned_data['pub_date']
        if pub_date is not None:
            if pub_date > datetime.datetime.now(datetime.timezone.utc):
                raise forms.ValidationError("The date must be past")
            return pub_date
