from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea
from django.core.exceptions import ValidationError
from .models import Genre
from datetime import date
import re

class PastDateField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Only past dates allowed here")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized")


class MovieForm(Form):
    title = CharField(max_length=128, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = PastDateField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data["description"]
        sentences = re.sub(r"\s*\.\s*", ".", initial).split(".")
        return ". ".join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result["genre"].name == "Comedy" and result["rating"] > 6:
            self.add_error("genre", ValidationError("Genre is comedy"))
            self.add_error("rating", ValidationError(f"Rating is {result['rating']}"))
            raise ValidationError("No comedy shall have a rating above 6")
        return result




