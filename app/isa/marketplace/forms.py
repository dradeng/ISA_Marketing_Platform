class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('image', 'duration', 'cost', 'url', 'site_title')