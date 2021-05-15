from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from .models import User, ProductCategory, Product


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email',)
    #
    # def __init__(self, *args, **kwargs):
    #     super(UserRegistrationForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=255, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductCategory
        fields = ('category_name',)


class CategoryEditForm(forms.ModelForm):
    category_name = forms.CharField(max_length=255, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_code = forms.CharField(max_length=255, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductCategory
        fields = ('category_name', 'category_code')


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(max_length=255, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), required=True,
                                              widget=forms.Select(attrs={'class': 'form-control'}))
    product_unit_price = forms.CharField(max_length=255, required=True,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_stock = forms.CharField(max_length=255, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('product_name', 'product_category', 'product_unit_price', 'current_stock')
