from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import Services, Category
# Create your views here.


def AllPageRender(request):
    services = Services.status_objects.all()[:4]
    context = {
        'services': services,
    }
    return context


def HomePage(request):
    services = Services.status_objects.all()
    context = {
        'services': services,
    }
    return render(request, 'web/index.html', context)


def CategoryDetail(request, slug):
    obj = get_object_or_404(Category, slug=slug)
    services = Services.objects.filter(categories=obj)
    # Header categories list
    category = Category.objects.all()
    context = {
        'object': obj,
        'cats': category,
        'services': services,
    }
    return render(request, 'web/services.html', context)


def AboutPage(request):
    return render(request, 'web/about.html')


def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            find_us = form.cleaned_data['find_us']
            message = form.cleaned_data['message']
            # form.save()
            comment = 'Name: ' + name + " \nFrom: " + email + "\n\n" + message + "\n\n\nDepartment: " + find_us + "\nTEL: " + phone
            try:
                send_mail(
                    name,  # subject
                    comment,  # message
                    email,  # from email
                    [settings.EMAIL_HOST_USER],  # to email
                    fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            print('success')
            messages.success(request, f"{name} your message successfully sent!")
            return redirect("contact-page")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'web/contact.html', context)


def ServicesPage(request):
    services = Services.status_objects.all()

    return render(request, 'web/services.html', {'services': services})


def ServicesPageDetail(request, slug):
    obj = get_object_or_404(Services, slug=slug)
    services = Services.status_objects.all()[:6]
    return render(request, 'web/service-detail.html', {'object': obj, 'services': services})


def CoreValues(request):
    return render(request, 'web/core_values.html')


def VisionPage(request):
    return render(request, 'web/vision.html')


def BlogPage(request):
    return render(request, 'web/blog.html')


def BlogPostDetail(request):
    return render(request, 'web/news-detail.html')


# HTTP Error 400
def page_not_found(request):
    return render(request, 'web/404.html', status=404)
