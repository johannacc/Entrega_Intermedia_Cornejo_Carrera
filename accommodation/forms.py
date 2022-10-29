from ckeditor.widgets import CKEditorWidget
from django import forms

from accommodation.models import Accommodation


class AccommodationForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del alojamiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accommodation-name",
                "placeholder": "Nombre del alojamiento",
                "required": "True",
            }
        ),
    )
    Location = forms.CharField(
        label="Ubicación del alojamiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accommodation-location",
                "placeholder": "Ubicación del alojamiento",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "accommodation-description",
                "placeholder": "Descripcion del alojamiento",
                "required": "True",
            }
        ),
    )

    contact = forms.IntegerField(
        label="Contacto:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accommodation-contact",
                "placeholder": "Telefono de contacto",
                "required": "True",
            }
        ),
    )

    price = forms.FloatField(
        label="Precio:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accommodation-precio",
                "placeholder": "Precio promedio del alojamiento",
                "required": "True",
            }
        ),
    )




    class Meta:
        model = Accommodation
        fields = ["name", "location", "description"]
