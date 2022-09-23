from django import forms
from django.contrib.auth.models import User 

class KreyeKontForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','password')
        widgets={
            'password':forms.PasswordInput
        }

    def save(self, commit=True):
        user = super(KreyeKontForm, self).save(commit=False)
        if commit:
            user.save()
        return user

# class KonekteForm(forms.ModelForm):
    
#     class Meta:
#         model
#         fields = ("",)









# class KreyeKontForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields =  ('non','siyati','foto','imel','telefon')
#     def clean(self):
#         clean_data = super().clean()
#         non = self.cleaned_data['non']
#         siyati = self.cleaned_data['siyati']
#         imel = self.cleaned_data['imel']
#         telefon = self.cleaned_data['telefon']

#         if len(siyati) > 2:
#             self.add_error("siyati", "Ou paka gen 2 siyati an menm tan")
