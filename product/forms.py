from . models import ProductReview
from django import forms




class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rate', 'review']