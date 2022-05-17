from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product_type"].empty_label = "Тип товара не выбран"
        self.fields["address"].empty_label = "Адрес не выбран"

    class Meta:
        model = Products
        fields = [
            "title",
            "product_type",
            "delivery_date",
            "file_attachment",
            "address",
        ]


class AddTypeForm(forms.ModelForm):
    class Meta:
        model = Types
        fields = ["title",]


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Addreses
        fields = ["name",]
