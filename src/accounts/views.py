from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdate
from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from django.contrib import messages
# from core.models import Article


@unauthenticated_user
def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Account has been created!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'dash/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdate(instance=request.user.profile)
        # count = Article.objects.exclude(story_status='sn')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 'articles': count
    }
    return render(request, 'dash/profile.html', context)
