from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={
                                "placeholder": "Your Description",
                                "class": "new-class-name two",
                                "rows": 20,
                                "id": "my-id-for-textarea",
                                "cols": "50"
                            }
                        )
                    )
    price = forms.DecimalField(initial=199.99)
    # Email = forms.EmailField() wanted to do form validation here

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    # Form Validations

    def clean_title(self, *args, **kwargs):
        #title multiple validation

        title = self.cleaned_data.get("title")
        if "daniel" in title:
            return title
        elif "New Product" in title:
            return title
        else:
            raise forms.ValidationError("Invalid")


    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get("description")
        if len(description) <= 20:
            raise forms.ValidationError("You need up to 20 characters")
        else:
            return description


class RawProductForm(forms.Form):
    title       = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={
                    "placeholder": "Your Description",
                    "class": "new-class-name two",
                    "rows" : 20,
                    "id"   : "my-id-for-textarea",
                    "cols" : "50"
                }))
    price       = forms.DecimalField()