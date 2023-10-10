from django.shortcuts import render, redirect
from .forms import *
from django.forms import modelformset_factory
from .models import *




def create_blog(request):
    categories = Category.objects.all()
    extra_forms = int(request.GET.get('extra_forms', 1))
    
    # AuthorFormSet = forms.modelformset_factory(Author, form=AuthorForm, extra=extra_forms, max_num=extra_forms)
    BlogImageFormSet = modelformset_factory(BlogImage, form=BlogImageForm, extra=extra_forms, max_num=extra_forms)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        image_formset = BlogImageFormSet(request.POST, request.FILES, queryset=BlogImage.objects.none())

        if blog_form.is_valid() and image_formset.is_valid():
            # Save the blog post
            blog = blog_form.save(commit=False)
            blog.author = request.user  # Assuming you have user authentication
            blog.save()

            # Associate images with the blog post
            for img_form in image_formset:
                if img_form.cleaned_data:
                    image = img_form.cleaned_data['image']
                    BlogImage.objects.create(blog_post=blog, image=image)

            return redirect('/')  # Redirect to the blog post detail page or another appropriate page

    else:
        blog_form = BlogForm()
        image_formset = BlogImageFormSet(queryset=BlogImage.objects.none())

    
    context = {
        'blog_form': blog_form, 
        'image_formset': image_formset, 
        'extra_forms': extra_forms,
        'categories': categories,
        }

    return render(request, 'index.html', context)
