from django.forms import ModelForm
from .models import Listing
from cloudinary.forms import CloudinaryFileField

class ListingForm(ModelForm):
    class Meta:
        model = Listing
       
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "description",
            "address",
            "image"
        ]