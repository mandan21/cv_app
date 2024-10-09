from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, CVUploadForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import CV
import openpyxl
import json
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload_cv')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_cv')  # Redirect to desired view after login
        else:
            messages.error(request, 'Invalid username or password')  # Handle errors
    return render(request, 'users/login.html')

@login_required
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()

            try:
                # Read Excel file
                wb = openpyxl.load_workbook(cv.upload)
                sheet = wb.active
                data = {}
                for row in sheet.iter_rows(values_only=True):
                    data[row[0]] = row[1]  # Assuming your Excel has two columns
                cv.data = json.dumps(data)  # Save data as JSON
                cv.save()
                return redirect('view_cv')
            except Exception as e:
                return render(request, 'users/upload_cv.html', {'form': form, 'error': str(e)})
    else:
        form = CVUploadForm()
    return render(request, 'users/upload_cv.html', {'form': form})

@login_required
def view_cv(request):
    cv = get_object_or_404(CV, user=request.user)
    return render(request, 'users/view_cv.html', {'cv': cv})
