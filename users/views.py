from django.contrib.auth import logout
from django.shortcuts import redirect,render
from .forms import ProfileForm, ResetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def logout_user(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'users/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user, files=request.FILES)
        forms = ResetPasswordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        if forms.is_valid():
            old_password = forms.cleaned_data['old_password']
            new_password = forms.cleaned_data['new_password']
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('users:profile')
            else:
                forms.add_error('old_password', 'Incorrect old password')

    else:
        form = ProfileForm(instance=request.user)
        forms = ResetPasswordForm()

    return render(request, 'users/edit-profile.html',{"form":form, 'forms':forms})
