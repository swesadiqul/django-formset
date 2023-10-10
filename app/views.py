from django.shortcuts import render, redirect
from .forms import BlogForm, BlogImageForm
from .models import Blog, BlogImage

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the blog post
            blog = form.save(commit=False)
            # blog.author = request.user  # Assuming you have user authentication
            blog.save()

            # Handle the BlogImage formset
            BlogImageFormSet = form.formset_factory(BlogImageForm, extra=1)
            formset = BlogImageFormSet(request.POST, request.FILES, prefix='blog_images')
            if formset.is_valid():
                for img_form in formset:
                    if img_form.cleaned_data:
                        image = img_form.cleaned_data['image']
                        BlogImage.objects.create(blog_post=blog, image=image)

            return redirect('/')  # Redirect to the blog post detail page
    else:
        form = BlogForm()

    return render(request, 'index.html', {'form': form})

