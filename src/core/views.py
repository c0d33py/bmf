from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .models import Services, Category
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
# Create your views here.


def HomePage(request):
    queryset = Services.status_objects.all()[:6]
    context = {
        'services': queryset,
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
            comment = 'Name: ' + name + " \nFrom: " + email + "\n\n" + message + "\n\n\nFind us?: " + find_us + "\nTEL: " + phone
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

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            find_us = form.cleaned_data['find_us']
            message = form.cleaned_data['message']
            # form.save()
            comment = 'Name: ' + name + " \nFrom: " + email + "\n\n" + message + "\n\n\nFind us?: " + find_us + "\nTEL: " + phone
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
        'form': form,
        'services': services
    }
    return render(request, 'web/services.html', context)


def ServicesPageDetail(request, slug):
    obj = get_object_or_404(Services, slug=slug)
    services = Services.status_objects.all()[:6]
    return render(request, 'web/service-detail.html', {'object': obj, 'services': services})


def CoreValues(request):
    return render(request, 'web/core_values.html')


# HTTP Error 400
def page_not_found(request, *args, **kwargs):
    return render(request, 'web/404.html', status=404)
