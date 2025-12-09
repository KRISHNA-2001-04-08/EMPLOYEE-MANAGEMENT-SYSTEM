from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EmployeeForm
from .models import Employee
from django.db.models import Q


# ---------------------- LOGIN ----------------------
def login_user(request):
   

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # After login go to home
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")  # Login page


# ---------------------- LOGOUT ----------------------
def logout_user(request):
    logout(request)
    return redirect("login")  # Go back to login


# ---------------------- HOME (SEARCH + LIST) ----------------------
@login_required(login_url="login")
def home(request):
    q = request.GET.get("q", "")

    employees = Employee.objects.filter(
        Q(name__icontains=q)
        | Q(email__icontains=q)
        | Q(department__icontains=q)
    )

    return render(request, "home.html", {"employees": employees})


# ---------------------- ADD EMPLOYEE ----------------------
@login_required(login_url="login")
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully")
            return redirect("home")
    else:
        form = EmployeeForm()

    return render(request, "add.html", {"form": form})


# ---------------------- EDIT EMPLOYEE ----------------------
@login_required(login_url="login")
def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully")
            return redirect("home")
    else:
        form = EmployeeForm(instance=emp)

    return render(request, "update.html", {"form": form})


# ---------------------- DELETE EMPLOYEE ----------------------
@login_required(login_url="login")

def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        emp.delete()
        return redirect("home")

    return render(request, "delete.html", {"emp": emp})
