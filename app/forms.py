from django import forms
from .models import Blog, BlogImage

class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'tags', 'categories']

    featured_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False}))
    # The above field allows you to select one featured image.

    # Define a formset for multiple images
    blog_images = forms.formset_factory(
        BlogImageForm,
        extra=1,  # Set the initial number of empty forms as needed
        max_num=5,  # Set the maximum number of forms
        validate_max=True,
    )

