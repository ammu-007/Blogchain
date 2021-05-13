from django.http import Http404
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .models import BlogPost

# Create your views here.
def blog_post_detail_view(request, post_slug):
    obj = get_object_or_404(BlogPost, slug=post_slug)
    context = {"object": obj}
    template_name = "blog/detail.html"
    return render(request, template_name, context)


def blog_contact_view(request):
    print(request.POST)
    template_name = "blog/form.html"
    return render(request, template_name, {"title": "Contact us"})


def blog_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "list.html"
    context = {"object": qs}
    return render(request, template_name, context)


# @login_required
@staff_member_required
def blog_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    template_name = "blog/form.html"
    context = {"form": form}
    return render(request, template_name, context)


def blog_retrieve_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/retrieve.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    template_name = "blog/form.html"
    context = {"form": form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)


def blog_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)
