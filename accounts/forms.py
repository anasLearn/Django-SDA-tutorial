from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, Textarea
from django.db.transaction import atomic
from .models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name"]

    biography = CharField(
        label="Biography",
        widget=Textarea(attrs={'placeholder': 'Tell us your story with movies'}),
        min_length=20
    )

    @atomic
    def save(self, commit=True):
        result = super().save(commit)
        # self.instance.is_active = False
        written_bio = self.cleaned_data["biography"]
        profile = Profile(biography=written_bio, user=result)
        if commit:
            profile.save()
        return result
