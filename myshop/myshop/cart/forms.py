from django import forms
# from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # def __init__(self, pk, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(*args, **kwargs)
    #     print([(i, str(i)) for i in range(1, 10)])
    #     self.fields['quantity'].choices = Product.objects.get(pk=pk).quantity()
