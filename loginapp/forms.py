from django import forms
class SearchCertificateForm(forms.Form):
    seria = forms.ChoiceField(choices=[
        ('MK', 'MK'),
        ('DS', 'DS'),
        ('SF', 'SF'),
        ('FS', 'FS'),
        ('BD', 'BD'),
        ('FD', 'FD'),
        ('CS', 'CS'),
        ('3D', '3D'),
        ('NA', 'NA'),
    ], required=True)
    sertificate_id = forms.CharField(max_length=300, required=True)