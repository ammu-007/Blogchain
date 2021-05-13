from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    return render(request, "hello_world.html", {"title": "Home"})


def about_view(request):

    return render(request, "about.html", {"title": "About us"})


def contact_view(request):
    context = {"title": "Contact"}
    template_name = "contact.html"
    template_obj = get_template(template_name)
    rendered_obj = template_obj.render(context)
    return HttpResponse(
        rendered_obj
    )  # render(request, "contact.html", {"title": "Contact"})
