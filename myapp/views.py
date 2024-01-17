from django.shortcuts import render

# Create your views here.
# //myapp/views.py
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
  
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SignUpForm  # Import your custom signup form
from .models import SignUp

# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = SignUp
#         fields = ['username', 'password', 'confirm_password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords don't match.")


   
# def home(request): 
#     return render(request, 'index.html')
   
  
from django.shortcuts import render, redirect
from .forms import SignUpForm

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            email = form.cleaned_data['email']
            qq=form.cleaned_data['qq']

            # Create a new instance of SignUp model and save the data
            new_signup = SignUp(username=username, password=password, confirm_password=confirm_password, email=email,qq=qq)
            new_signup.save()

            return redirect('/profile')  # Redirect after successful signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


   
# def signout(request):
#     return redirect('/')