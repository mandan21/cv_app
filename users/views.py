from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import CV
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    cv = request.user.cv if hasattr(request.user, 'cv') else None
    return render(request, 'users/dashboard.html', {'cv': cv})

@login_required
def upload_cv(request):
    if request.method == 'POST' and request.FILES['cv']:
        uploaded_file = request.FILES['cv']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        
        # Read the uploaded Excel file
        file_path = fs.path(filename)
        excel_data = pd.read_excel(file_path)
        excel_json = excel_data.to_json()

        # Save to the database
        CV.objects.update_or_create(user=request.user, defaults={'upload': uploaded_file, 'data': excel_json})
        return redirect('dashboard')
    return render(request, 'users/upload.html')